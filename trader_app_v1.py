def calc_risk(trade_entry,trade_stop,trade_type):
    if trade_type == 1:
        risk = (trade_entry - trade_stop)
    elif trade_type == 2:
        risk = (trade_stop - trade_entry)
    else:
        print "Bad option"
    return risk

def calc_reward(trade_exit,trade_entry,trade_type):
    if trade_type == 1:
        reward = (trade_exit - trade_entry)
    elif trade_type == 2:
        reward = (trade_entry - trade_exit)
    else:
        print "Bad option"
    return reward

def calc_risk_reward(trade_risk,trade_reward):
    ratio = trade_reward / trade_risk
    return round(ratio)

def calc_position_size(trade_entry, trade_size):
    position_size = trade_entry * trade_size
    return position_size

def calc_odds_enhancers(OE1, OE2, OE3, OE4):
    OE_total = OE1 + OE2 + OE3 + OE4
    return OE_total
    
security_symbol = raw_input("Enter symbol ")
security_atr = raw_input("Enter Average True Range: ")

trade_size = int(raw_input("Number of shares: "))
trade_order = int(raw_input("1=Limit or 2=Market order: "))
trade_type = int(raw_input("1=Long or 2=Short? "))
trade_entry = float(raw_input('Enter Enter price: '))
trade_exit = float(raw_input('Enter Exit price: '))
trade_stop = float(raw_input('Enter Stop price: '))

#OE1 = int(raw_input("Odds Enhancer 1: "))
#OE2 = int(raw_input("Odds Enhancer 2: "))
#OE3 = int(raw_input("Odds Enhancer 3: "))
#OE4 = int(raw_input("Odds Enhancer 4: "))

trade_risk = calc_risk(trade_entry,trade_stop,trade_type)
trade_reward = calc_reward(trade_exit,trade_stop,trade_type)
trade_ratio = calc_risk_reward(trade_risk, trade_reward)
#odds = calc_odds_enhancers(OE1, OE2, OE3, OE4)
position_size = calc_position_size(trade_entry,trade_size)

print "\n%s shares of %s at %s ($%s)" % (trade_size, security_symbol, trade_entry, position_size)
print "%s to 1 Risk/Reward (Risk: $%s Reward: $%s)" % (trade_ratio, trade_risk, trade_reward)
#print "Odds Enhancer total = %s" % odds
