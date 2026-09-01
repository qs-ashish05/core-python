class Product:
    total_products = 0

    def __init__(self, name, product_id, price, discount=0.0):
        self.name = name  # Public
        self._product_id = product_id  # Protected

        self.__price = None  # Private (set via property below)
        self.__discount = None  # Private (set via property below)

        # self.price = price
        # self.discount = discount

        Product.total_products += 1

    @property
    def price(self):
        return self.__price

    @price.setter
    def price(self, value):
        if value <= 0:
            print(f"Invalid price: {value}. Price must be greater than 0. 'negative'")
        else:
            self.__price = value

    @property
    def discount(self):
        return self.__discount

    @discount.setter
    def discount(self, value):
        if value < 0.0 or value > 50.0:
            print(f"Invalid discount: {value}. Must be between 0.0 and 50.0. 'invalid'")
        else:
            self.__discount = value

    def final_price(self):
        if self.__price is None:
            return 0
        discount_amt = (self.__discount or 0) / 100 * self.__price
        return round(self.__price - discount_amt, 2)

    def display_info(self):
        print(f"[{self._product_id}] {self.name} | "
              f"Price: ${self.__price} | Discount: {self.__discount}% | "
              f"Final Price: ${self.final_price()}")


p1 = Product("Laptop", "P001", 55000, 10)
p2 = Product("Mouse", "P002", 500, 5)

p1.display_info()
p2.display_info()

p1.price = -100  # invalid -> prints error, keeps old price
p1.discount = 75  # invalid -> prints error, keeps old discount
p1.display_info()

print(f"\nTotal products created: {Product.total_products}")