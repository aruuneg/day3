from datetime import datetime

class StockMove:
    def __init__(self, id, product, quantity, move_type):
        self.id = id
        self.product = product
        self.quantity = quantity
        self.move_type = move_type  # "Орсон " or "Гарсан"
        self.timestamp = datetime.now()

    def __str__(self):
        return f"[{self.id}] {self.move_type.upper()} - {self.product.name}, Тоо: {self.quantity}, Цаг: {self.timestamp}"
