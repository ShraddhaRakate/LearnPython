
# Function to determine the auction logic
def bid_auction_winner(initial_price, bids):
    current_price = initial_price
    max_bid = int(bids[1])
    highest_bidder = bids[0]
    winner=[]
    l = len(bids)
    for x in range(3,l,2):
        if int(bids[x]) > max_bid:
            current_price = max_bid + 1
            highest_bidder = bids[x-1]
            max_bid = int(bids[x])
        elif int(bids[x]) < max_bid:
            current_price = max_bid + 1
        else:
            current_price = int(bids[x])
    winner = [highest_bidder,max_bid]
    return winner

def main():
    # Read file containing bid data
    with open("samples/test_input.txt") as f:
        line = f.readline().strip()
        while line != "":
            line_list = line.split(",")
            initial_price = int(line_list[0])
            del line_list[0]
            winner = bid_auction_winner(initial_price, line_list)
            winner[1] = str(winner[1])
            # Write result of each bid in output file
            with open("samples/test_output.txt","a") as w:
                w.write(",".join(winner) + "\n")
            line = f.readline().strip()


if __name__ == "__main__":
    main()




