from product import Product
from warehouse import Warehouse
from stock_move import StockMove

item1 = Product(1, "Гурил", "Хүнсний бараа", 3000.0, 100)
item2 = Product(2, "Өндөг10ш", "Хүнсний бараа", 5500.0, 50)
item3 = Product(3, "Талх", "Хүнсний бараа", 4000.0, 200)

warehouse = Warehouse(101, "Төв агуулах", 5)
warehouse.add_product(item1)
warehouse.add_product(item2)
warehouse.add_product(item3)

print("\nАгуулах дахь бараанууд:")
warehouse.list_products()

move1 = StockMove(1, item1, 20, "Орсон")
move2 = StockMove(2, item2, 10, "Гарсан")
move3 = StockMove(3, item3, 30, "Орсон")

print("\nБарааны хөдөлгөөн:")
print(move1)
print(move2)
print(move3)

