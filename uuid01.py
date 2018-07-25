import uuid
print(str(uuid.uuid1()))
list = []

for i in range(1,100001):
    list.append(str(uuid.uuid1()).split('-')[0])
print(len(list))
print(len(set(list)))