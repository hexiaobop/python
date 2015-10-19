#encoding:utf=8
import pymongo

connection=pymongo.MongoClient('127.0.0.1',27017)

#选择myblog库
db=connection.myblog

# 使用users集合
collection=db.users

# 添加单条数据到集合中
user = {"name":"cui","age":"10"}
collection.insert(user)

#同时添加多条数据到集合中
users=[{"name":"cui","age":"9"},{"name":"cui","age":"11"}]
collection.insert(users)

#查询单条记录
print collection.find_one()

#查询所有记录
for data in collection.find():
	print data

#查询此集合中数据条数
print collection.count()

#简单参数查询
for data in collection.find({"name":"1"}):
        
        
	print data

#使用find_one获取一条记录
print collection.find_one({"name":"1"})


#高级查询
print "__________________________________________"
print '''collection.find({"age":{"$gt":"10"}})'''
print "__________________________________________"
for data in collection.find({"age":{"$lt":"12"}}).sort("age"):
	print data

# 查看db下的所有集合
print db.collection_names()
