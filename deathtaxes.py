# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at https://mozilla.org/MPL/2.0/.

event = input().split() # Seperate input into lists

# Initialize variables
share_price = 0
num_shares = 0

while event[0] != "die":
    shares = int(event[1])
    if event[0] == "buy": # If Mittens bought stocks, keep track of total number of stocks and how much she purchased them for
        share_price += shares * int(event[2])
        num_shares += shares
    elif event[0] == "sell": # If Mittens sold stocks, subtact from running total
        if num_shares !=0:
            share_price *= (num_shares - shares) / num_shares # Selling shares affects the price proportionally
            num_shares -= shares
    elif event[0] == "split": # Fairly self explainatory - multiply number of stocks by provided x value
        num_shares *= shares
    else: # Honestly, merging stocks is just a modified selling process
        if shares != 0 and num_shares != 0:
            share_price *= (num_shares - (num_shares % shares)) / num_shares # Selling only the number of shares that can't be merged
            num_shares -= (num_shares % shares)
            num_shares /= shares
    event = input().split()

total = int(event[1]) * num_shares
if total > share_price: # If selling at a profit, calculate and subtract capital gains tax
    total -= (total - share_price) * 0.3
print(total)


# A better implementation using Python 3.8, which introduced walrus case, but Kattis is using PyPy version Python 3.6.9 so this will not be accepted but is better.

# Initialize variables
share_price = 0
num_shares = 0

while (event:=input().split())[0] != "die":
    shares = int(event[1])
    if event[0] == "buy": # If Mittens bought stocks, keep track of total number of stocks and how much she purchased them for
        share_price += shares * int(event[2])
        num_shares += shares
    elif event[0] == "sell": # If Mittens sold stocks, subtact from running total
        if num_shares !=0:
            share_price *= (num_shares - shares) / num_shares # Selling shares affects the price proportionally
            num_shares -= shares
    elif event[0] == "split": # Fairly self explainatory - multiply number of stocks by provided x value
        num_shares *= shares
    else: # Honestly, merging stocks is just a modified selling process
        if shares != 0 and num_shares != 0:
            share_price *= (num_shares - (num_shares % shares)) / num_shares # Selling only the number of shares that can't be merged
            num_shares -= (num_shares % shares)
            num_shares /= shares

total = int(event[1]) * num_shares
if total > share_price: # If selling at a profit, calculate and subtract capital gains tax
    total -= (total - share_price) * 0.3
print(total)
