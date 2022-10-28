# Problem Statement

**Implement an auction system**

A bid describes the maximum amount a bidder
is willing to pay for a product. The price of the
product is generally increased in 1 Euro steps, or
in larger steps depending on the bids.


# Assumptions

The inputs consist only of valid bids (no bids with amounts that are lower than the current price)


# Input

s,{b,g} where 
- `s` is the initial price
- `{b, g}` A list of bids consisting of the `bidder‘s name (str)` and the `maximum bid (int)`

Example Input : `1,A,5,B,10,A,8,A,17,B,17`

# Output

**Return Auction price + Highest bidder**

b,p where

- `b` is the name of the highest bidder 
- `p` is the auction price at which b wins the auction.

Result of the example above : `A,17`