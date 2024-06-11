import pymongo

client = pymongo.MongoClient("mongodb://localhost:27017/")
db = client['e-shop']
prod_aval = db['products in stock']
transaction = db['products sold']


insert_cond = input('do you want to do insert, delete or nothing "say i , d or n": ')
if insert_cond == 'i':
    name = (input("which product: ")).lower().strip()
    qnt = int(input("quantity: "))
    d = prod_aval.find_one({"name":name})
    if d != None:
        d_qnt = d["qnt"]
        prod_aval.update_one({"name":name}, {"$set" :{"qnt": qnt + d_qnt}})
    if d==None:
        prod_aval.insert_one({"name": name, "qnt": qnt})
elif insert_cond == "d":
    name = (input("which product: ")).lower().strip()
    qnt = int(input("quantity: "))
    d = prod_aval.find_one({"name": name})
    if(d != None):
        threshold_q = d["qnt"]
        if threshold_q > qnt:
            prod_aval.update_one({"name": name}, {"$set": {"qnt": threshold_q - qnt}})
        elif threshold_q == qnt:
            prod_aval.delete_one({"name": name})
        else:
            print(f"this is not possible there are only {threshold_q} {d['name']} available")



