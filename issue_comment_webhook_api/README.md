# Problem Statement

Create a Github Bot which can use the [issue_comment](https://docs.github.com/en/developers/webhooks-and-events/webhooks/webhook-events-and-payloads#issue_comment) webhook to merge requests.
- Additionally restricts the merge to happen if the issue comment contains magic phrase "#merge" AND the pull request is in the "SomeOrganization" organization


# Assumptions


```
POST /api/v4/repos/:owner/:name/pulls/:num/merge
Where:
:owner - the repository owner or organization
:name - the repository name
:num - the pull request number
```

Additionally, the following data should be provided as part of the request payload, in JSON
format:
```
pull[base_ref] - base ref of the pull request
pull[head_sha] - head SHA of the pull request
requester - the login name of the user who requested the merge
```

The `:owner`, `:name`, `:num` and `requester` are available in the webhook response payload.

For Pull Request Metadata, we use [Pulls API](https://docs.github.com/en/rest/pulls/pulls#get-a-pull-request) using the `pull_number` of the PR.

# Sample execution
```bash
$ python3 main.py
$ cat bot.log
2022-10-17 18:24:52,418 - INFO - Parsing webhook body to extract repository and PR information
2022-10-17 18:24:52,419 - INFO - Requesting pull request metdata for PR number 2
2022-10-17 18:24:52,419 - INFO - https://api.github.com/repos/Codertocat/Hello-World/pulls/2
2022-10-17 18:24:52,940 - INFO - Pull request information retrieved
2022-10-17 18:24:52,940 - INFO - Merge URL is https://www.merger.example.com/api/v4/repos/Codertocat/Hello-World/pulls/2/merge
2022-10-17 18:24:52,940 - INFO - {'base_ref': 'master', 'head_sha': 'ec26c3e57ca3a959ca5aad62de7213c562f8c821', 'requester': 'Codertocat'}
2022-10-17 18:24:52,941 - ERROR - The comment 'You are totally right! I'll get this fixed right away.' does not contain magic phrase #merge
```

In order to see full success, one can manipulate the `webhook_sample.json` file to contain the right Comment body.
# Deployment Options

Option 1: [AWS Lambda](https://docs.aws.amazon.com/lambda/latest/dg/python-package.html) can accept zip files containing Python modules which can run on events.

Option 2: [Docker Container](https://hub.docker.com/_/python) deployed on any node as part of standalone or as a Kubernetes cluster.
