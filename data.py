import json

class Product:
    def __init__(self, productId, productNumber, categoryLevel1, categoryLevel2, apk, price, productNameBold, productNameThin, isTemporaryOutOfStock):
        self.productId = productId
        self.productNumber = productNumber
        self.categoryLevel1 = categoryLevel1
        self.categoryLevel2 = categoryLevel2
        self.apk = apk
        self.price = price
        self.productNameBold = productNameBold
        self.productNameThin = productNameThin
        self.isTemporaryOutOfStock = isTemporaryOutOfStock


        self.productName = self.createProductName()

    def createProductName(self):
        if self.productNameThin is not None:
            return self.productNameBold + " " + self.productNameThin
        else:
            return self.productNameBold

class ProductDatabase:
    def __init__(self, json_file):
        self.products = []
        self.load_products(json_file)

    def load_products(self, json_file):
        with open(json_file, 'r', encoding='utf-8') as f:
            data = json.load(f)
            for product in data:
                self.products.append(Product(
                    product.get('productId', None),
                    product.get('productNumber', None),
                    product.get('categoryLevel1', None),
                    product.get('categoryLevel2', None),
                    product.get('apk', None),
                    product.get('price', None),
                    product.get('productNameBold', None),
                    product.get('productNameThin', None),
                    product.get('isTemporaryOutOfStock', None)
                ))



    def getIndexParameter(self, index, parameter):
        if parameter == "price": return self.products[index].price
        elif parameter == "productNumber": return self.products[index].productNumber
        elif parameter == "categoryTypeOne": return self.products[index].categoryLevel1
        elif parameter == "categoryTypeTwo": return self.products[index].categoryLevel2
        elif parameter == "apk": return self.products[index].apk
        elif parameter == "productId": return self.products[index].productId
        elif parameter == "productNameBold": return self.products[index].productNameBold
        elif parameter == "productNameThin": return self.products[index].productNameThin
        elif parameter == "productName": return self.products[index].productName
        else: return 2


# Usage
db = ProductDatabase('products.json')

def getIndexParameter(parameter, index):
    return db.getIndexParameter(index, parameter)
