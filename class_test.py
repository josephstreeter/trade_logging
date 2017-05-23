
class account(object):
    def set_balance(self, x):
        self.balance = float(x)

    def set_max_risk(self, x):
        self.max_risk = float(x)

class trade(object):
    def set_entry(self, x):
        self.entry = float(x)

    def set_target(self, x):
        self.target = float(x)

    def set_stop(self, x):
        self.stop = float(x)

    def set_symbol(self,x):
        self.symbol = x

    def set_shares(self,x):
        self.shares = x
    
    def set_entry_type(self,x):
        if x == 1:
            self.entry_type = "Limit"
        elif x == 2:
            self.entry_type = "Market"
        else :
            return "Enter 1 or 2"

    def set_order_type(self,x):
        if x == 1:
            self.order_type = "Long"
        elif x == 2:
            self.order_type = "Short"
        else :
            return "Enter 1 or 2"
        
    def set_order_status(self, x):
        if x == 1:
            self.status = "Pending"
        elif x == 2:
            self.status = "Open"
        elif x == 3:
            self.status = "Closed"
        else :
            return "Enter 1, 2, or 3"

    def calc_position_size(self):
        self.position_size = self.entry * self.shares
        
    def calc_risk(self):
        self.reward = abs(self.target - self.entry)
        self.risk = abs(self.stop - self.entry)
        self.risk_ratio = int(round(self.reward) / round(self.risk))

a = trade()
a.set_entry(10.50)
a.set_target(15.20)
a.set_stop(9.10)
a.set_shares(10)
a.set_order_status(1)
a.set_symbol("MSFT")
a.set_order_type(1)
a.set_entry_type(1)
a.calc_risk()
a.calc_position_size()


print a.entry
print a.target
print a.stop
print a.shares
print a.status
print a.symbol
print a.order_type
print a.entry_type
print a.risk
print a.risk_ratio
print a.position_size
