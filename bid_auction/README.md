# Problem Statement

**Implement an auction system**

A bid describes the maximum amount a bidder
is willing to pay for a product. The price of the
product is generally increased in 1 Euro steps, or
in larger steps depending on the bids.


# Assumptions

*The inputs consist only of valid bids (no bids with amounts that are lower than the current price)*


# Input

*s,{b,g}* 

**s** is the initial price

a list of bids consisting of the **bidder‘s name (b)**, and the **maximum bid (g, integer value)**.

*Example Input* : 1,A,5,B,10,A,8,A,17,B,17

# Output

**Return Auction price + Highest bidder**

*b,p* 

**b** the name of the highest bidder, 

**p** is the auction price at which b wins the auction.

*Result of the example above* : A,17