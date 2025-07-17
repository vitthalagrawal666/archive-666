# modules/products.py

class Product:
    def __init__(self, product_id, name, description, raw_materials_required, quantity_in_stock, price):
        self.product_id = product_id
        self.name = name
        self.description = description
        self.raw_materials_required = raw_materials_required  # Dict of raw material name -> quantity per unit
        self.quantity_in_stock = quantity_in_stock
        self.price = price

    def update_stock(self, quantity):
        self.quantity_in_stock += quantity

    def reduce_stock(self, quantity):
        if quantity <= self.quantity_in_stock:
            self.quantity_in_stock -= quantity
            return True
        else:
            return False

    def get_details(self):
        return {
            "ID": self.product_id,
            "Name": self.name,
            "Description": self.description,
            "Required Materials": self.raw_materials_required,
            "Stock": self.quantity_in_stock,
            "Price": self.price
        }


class ProductManager:
    def __init__(self):
        self.products = []

    def add_product(self, product: Product):
        self.products.append(product)

    def get_product_by_id(self, product_id):
        for product in self.products:
            if product.product_id == product_id:
                return product
        return None

    def remove_product(self, product_id):
        product = self.get_product_by_id(product_id)
        if product:
            self.products.remove(product)
            return True
        return False

    def update_product_stock(self, product_id, quantity):
        product = self.get_product_by_id(product_id)
        if product:
            product.update_stock(quantity)
            return True
        return False

    def list_all_products(self):
        return [product.get_details() for product in self.products]
