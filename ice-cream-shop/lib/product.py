class product:
    ice_cream = {
        'apple': {
            'rrp': 2.50,
            'cost':1.50,
            'price': 0.00,
            'sales': 0,
            'sale_rate': 10,
            'price_sales_rate_per_10p': 10
        },
        'banana': {
            'rrp': 2.35,
            'cost':1.50,
            'price': 0.00,
            'sales': 0,
            'sale_rate': 15,
            'price_sales_rate_per_10p': 10
        },
        'strawberry': {
            'rrp': 2.65,
            'cost':1.50,
            'price': 0.00,
            'sales': 0,
            'sale_rate': 30,
            'price_sales_rate_per_10p': 10
        },
        'caramel': {
            'rrp': 2.65,
            'cost':1.50,
            'price': 0.00,
            'sales': 0,
            'sale_rate': 25,
            'price_sales_rate_per_10p': 10
        },
        'mint': {
            'rrp': 2.65,
            'cost':1.50,
            'price': 0.00,
            'sales': 0,
            'sale_rate': 20,
            'price_sales_rate_per_10p': 10
        },
    }
    customers=0
    sales = 0.00


    def set_price(self, flavor: str, price: float):
        self.ice_cream[flavor]["price"] = price

    def set_price_percent(self, percent:float):
        for flavor in self.ice_cream:
            self.ice_cream[flavor]["price"] = self.ice_cream[flavor]["cost"] * (1+percent/100)

    def get_product(self, flavor: str):
        return self.ice_cream[flavor]

    def calculate_sales(self, customer):
        self.customers = customer
        self.check_selling_price()
        return self.calculate_profit()


    def check_selling_price(self):
        for flavor in self.ice_cream:
            price = float(self.ice_cream[flavor]["price"])
            cost = float(self.ice_cream[flavor]["cost"])
            if price <= 0:
                print(flavor, " selling price is lower or equal to 0.00")
            if price < cost:
                print(flavor, " selling price is lower then cost")

    def calculate_profit(self):
        self.sales = 0.00
        for flavor in self.ice_cream:
            price = float(self.ice_cream[flavor]["price"])
            cost = float(self.ice_cream[flavor]["cost"])
            sold = int(self.ice_cream[flavor]["sale_rate"]) * self.customers / 100
            profit = round( (price - cost) * sold, 2)

            self.ice_cream[flavor]["profit"]=profit
            self.sales+=profit
            print("profit- ", flavor, ": ", profit)

    def get_sales(self):
        return self.sales