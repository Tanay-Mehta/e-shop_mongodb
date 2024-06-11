import pymongo

client = pymongo.MongoClient("mongodb://localhost:27017/")
db = client['e-shop']
prod_aval = db['products in stock']
transaction = db['products sold']


insert_cond = input('do you want to do restore stock, sale or exit "say r , s or e": ')
if insert_cond == 'r':
    name = (input("which product: ")).lower().strip()
    qnt = int(input("quantity: "))
    d = prod_aval.find_one({"name":name})
    if d != None:
        d_qnt = d["qnt"]
        prod_aval.update_one({"name":name}, {"$set" :{"qnt": qnt + d_qnt}})
    if d==None:
        prod_aval.insert_one({"name": name, "qnt": qnt})
elif insert_cond == "s":
    name = (input("which product: ")).lower().strip()
    qnt = int(input("quantity: "))
    d = prod_aval.find_one({"name": name})
    if(d != None):
        threshold_q = d["qnt"]
        if threshold_q > qnt:
            prod_aval.update_one({"name": name}, {"$set": {"qnt": threshold_q - qnt}})
            n = transaction.find_one({"name": name})
            if n == None:
                transaction.insert_one({"name": name, "qnt": qnt})
            else:
                n_qnt = n["qnt"]
                transaction.update_one({"name": name}, {"$set": {"qnt": qnt + n_qnt}})
        elif threshold_q == qnt:
            prod_aval.delete_one({"name": name})
            n = transaction.find_one({"name": name})
            if n == None:
                transaction.insert_one({"name": name, "qnt": qnt})
            else:
                n_qnt = n["qnt"]
                transaction.update_one({"name": name}, {"$set": {"qnt": qnt + n_qnt}})
        else:
            print(f"this is not possible there are only {threshold_q} {d['name']} available")


