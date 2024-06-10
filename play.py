import pymongo

class product:
    def __init__(self, name, qnt):
        self.quantity = qnt
        self.name = name
    def add(self, quantity):
        self.quantity = self.quantity+quantity

client = pymongo.MongoClient("mongodb://localhost:27017/")
db = client['e-shop']
collection = db['products in stock']

data = collection.find_one({"_id": 1})
d = data
data = (data['products_available'])

insert_cond = input('do you want to do insert, delete or nothing "say y , d or n": ')
if insert_cond == 'y':
    name = input("which product: ")
    qnt = int(input("quantity: "))
    n = 1
    for i in data:
        if i == data.name:
            n = 0
            data.quantity = data.quantity+qnt
            collection.update_one(d, {'$set':{"products_available":data}})
    if(n == 1):
        p = product(name, qnt)
        data.append(p)
        collection.update_one(d, {'$set': {"products_available": data}})
        #insert in product

#check if product exists
#if it does then only change quantity
#else create new product
# elif insert_cond == 'd':
#

#import data dynamically


# data = {
#     "_id" : 1,
#     "products_available": [],
# }
#
# collection.insert_one(data)

#


