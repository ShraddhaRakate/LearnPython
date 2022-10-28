def bid_auction_winner(initial_price, bids):
    """
    Auction logic
    """
    current_price = initial_price
    max_bid = int(bids[1])
    highest_bidder = bids[0]
    for x in range(3, len(bids), 2):
        current_bid = int(bids[x])
        if current_bid > max_bid:
            current_price = max_bid + 1
            highest_bidder = bids[x - 1]
            max_bid = current_bid
        elif current_bid < max_bid:
            current_price = max_bid + 1
        else:
            current_price = current_bid
    return [highest_bidder, max_bid]

def main():
    """
    Description for main
    """
    with open("samples/test_input.txt") as f:
        for line in f:
            line_list = line.strip().split(",")
            # First element is initial price
            initial_price, *bids = line_list
            initial_price = int(initial_price)
            winner_name, winner_bid = bid_auction_winner(initial_price, bids)
            # Write result of each bid in output file
            with open("samples/test_output.txt", "a") as w:
                w.write(f"{winner_name}, {winner_bid}\n")


if __name__ == "__main__":
    main()
