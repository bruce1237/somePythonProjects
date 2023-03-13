from lib.product import product
from lib.asset import asset


product = product()
product.set_price('apple', 4.56)
product.set_price('banana', 4.56)
product.set_price('strawberry', 4.56)
product.set_price('caramel', 4.56)
product.set_price('mint', 4.56)

product.calculate_sales(100)

profit = product.get_sales()
print(profit)
product.set_price_percent(900)
product.calculate_sales(100)

profit = product.get_sales()
print(profit)




asset = asset()
asset_cost = asset.monthly_cost()
print("asset cost: ", asset.monthly_cost())

print("---------------------")
print("total Profit:", profit - asset_cost)