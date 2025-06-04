class Warehouse:
    def __init__(self, id, location, capacity):
        self.id = id
        self.location = location
        self.capacity = capacity
        self.products = []

    def add_product(self, product):
        if len(self.products) < self.capacity:
            self.products.append(product)
            print("Бүтээгдэхүүн агуулахад нэмэгдлээ.")
        else:
            print("Агуулах дүүрэн байна!")

    def list_products(self):
        for p in self.products:
            print(p)
