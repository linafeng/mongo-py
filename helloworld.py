# -*- coding: utf-8 -*-
import pymongo

print(pymongo.version)
uri = "mongodb://127.0.0.1:27017"
client = pymongo.MongoClient(uri)
print(client)

# 初始化数据库和集合
db = client["eshop"]
user_coll = db["users"]
# 插入一条新的用户数据
new_user = {"username": "nina2", "password": "123", "email": "123456@qq.com "}
result = user_coll.insert_one(new_user)
print(result)

# 需求变化，要求修改用户属性，增加字段phone
result = user_coll.update_one({"username": "nina2"}, {"$set": {"phone": "123456789"}})
print(result)
