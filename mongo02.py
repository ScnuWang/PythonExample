from pymongo import MongoClient

host = 'localhost'

port = 27017
# 获取连接
client = MongoClient(host=host,port=port)

db = client.wangyi

comments = db.comments

print(db.comments.find({ }))