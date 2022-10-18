from urllib.request import Request, urlopen
from urllib.error import URLError, HTTPError
from urllib.parse import urlencode
import json
import logging

MERGE_SERVICE_URL = "somemerger.example.com"
TRIGGER_PHRASE = "#merge"
ORGANIZATION_NAME ="SomeOrganization"

def process_url(req_obj):
    """
        Makes a web request to the given Request object.  
        Returns: Response text if success. None if error
    """
    try:
        logging.info(req_obj.full_url)
        with urlopen(req_obj) as response:
            result = response.read().decode("utf-8")
    except HTTPError as e:
        logging.error("The server could not fulfill the request.")
        logging.error("Error code: ", e.code)
        return None
    except URLError as e:
        logging.error('We failed to reach a server.')
        logging.error('Reason: ', e.reason)
        return None
    else:  
        return result

def process_issue_comment(webhook_body):
    """
        Process an issue_comment event from GitHub.
        Called whenever GitHub sends a webhook as a result of a comment on a pull request thread.
        Params:
            webhook_body: Full text string containing response of an issue_comment API call
        Returns: None
    """
    logging.info("Parsing webhook body to extract repository and PR information")
    payload = json.loads(webhook_body)
    repo_owner = payload["repository"]["owner"]["login"]
    repo_name = payload["repository"]["name"]
    pull_number = payload["issue"]["number"]
    merge_user = payload["comment"]["user"]["login"]
    comment_body = payload["comment"]["body"]
    pull_url = payload["repository"]["pulls_url"].replace("{/number}",f"/{pull_number}")
    pull_header = {'Accept' : 'application/vnd.github+json'}
    get_pull_req = Request(pull_url, headers=pull_header)
    logging.info(f"Requesting pull request metdata for PR number {pull_number}")
    get_pull_response = process_url(get_pull_req)
    if get_pull_response is not None:
        logging.info("Pull request information retrieved")
        get_pull_response = json.loads(get_pull_response)
        pull_base_ref = get_pull_response["base"]["ref"]
        pull_base_sha = get_pull_response["head"]["sha"]
        pull_user = get_pull_response["user"]["login"]
        values = {'base_ref': pull_base_ref,
                'head_sha': pull_base_sha,
                'requester': merge_user }
        url = f"https://www.{MERGE_SERVICE_URL}/api/v4/repos/{repo_owner}/{repo_name}/pulls/{pull_number}/merge"
        logging.info(f"Merge URL is {url}")
        logging.info(values)
        data = urlencode(values)
        data = data.encode('UTF-8')
        req = Request(url, data)
        relevant_comment = TRIGGER_PHRASE in comment_body.lower()
        relevant_org = pull_user == ORGANIZATION_NAME 
        if relevant_org and relevant_comment:
            logging.info("Proceeding to merge request")
            resp_API = process_url(req)
            if resp_API is not None:
                logging.info(f"SUCCESS: Request to {url} successful")
            else:
                logging.error(f"Request to {url} failed")
        else:
            if not relevant_comment:
                logging.error(f"The comment '{comment_body}' does not contain magic phrase {TRIGGER_PHRASE}")
            else:
                logging.error(f"The PR {pull_number} organization {pull_user} does not match {ORGANIZATION_NAME}")
    else:
        logging.error("Request to Github failed")

def main(webhook_body):
    # initialize logging
    logging.basicConfig(filename='bot.log', filemode='w', format='%(asctime)s - %(levelname)s - %(message)s', level=logging.INFO)
    # call bot
    process_issue_comment(webhook_body)

if __name__ == "__main__":
    # Load the default example
    with open("samples/webhook_sample.json") as f:
        main(f.read())
