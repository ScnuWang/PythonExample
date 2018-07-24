from pymongo import MongoClient
# 定义链接地址和端口
host = 'localhost'
port = 27017
# 获取连接
client = MongoClient(host=host,port=port)
# 定义数据库
db = client.douban
# 定义存储文档（类似关系数据库表）
movies = db.movies
# 定义存储内容
movie = {"movie_name":"勇闯夺命岛","year":1996}
# 插入数据
rs = movies.insert_one(movie)
# 获取插入数据编号
print('one insert:{0}'.format(rs.inserted_id))