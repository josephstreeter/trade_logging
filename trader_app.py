#!/usr/bin/python

class Trade:
    pass

trade = Trade()  # Create an empty employee record

# Fill the fields of the record
trade.symbol = "MSFT"
trade.price_entry = round(float(35.43), 2)
trade.price_exit = round(float(39.25), 2)
trade.price_stop = round(float(34.20), 2)
trade.shares = 1000
trade.type = "long"
trade.entry_type = "market"
trade.profit = round((trade.price_exit - trade.price_entry), 2)
trade.risk = round((trade.price_entry - trade.price_stop), 2)
trade.risk_reward = round((trade.profit / trade.risk))
trade.status = "Pending"

print """
%s of %s at %s
Exit: $%s Stop: $%s
%s to 1 risk/reward (Profit: $%s Risk: $%s
""" % (trade.shares, trade.symbol, trade.price_entry,
 trade.price_exit, trade.price_stop, trade.risk_reward,
 trade.profit, trade.risk)
