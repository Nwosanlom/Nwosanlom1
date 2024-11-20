#str
s1 = "Hello World"
b1 ="dog" not in s1
print(b1)

#int
int1 = 3
int2 = 2
print(int1+int2)
#int divivsion
print(2//1)

#float
x = 3.5
y = 2.1
print(x+y)
print(int(x+y))

#boolean
bool1 = True
bool2 = False
print(bool(1))
print(bool(0))

#list
collection = [1,2,3]
print(len(collection))
print(collection[1])
print(collection[-1])
print(collection[0:2])
collection[2] = 4
print(collection)
for i in range(len(collection))
    print(collection[i])
if 1 in collection:
    print("1 is in the list")
collection.append(3)
collection.clear()
collection.sort()
collection.reverse()
collection2 = [4,5,6]
collection.extend(collection2)
print(collection)
print(collection.index(1))
collection.insert(0,9)
print(collection)
collection.pop(1)
print(collection)
collection.remove(0)
print(collection)

#tuples
collect = (1,2,3)
print(collect[0])
#tuple are immutable
#but can be converted as follows
collect2 = list(collect)
collect2[0] = 4
collect = tuple(collect2)
print(collect)
for i in collect:
    print(collect)
if 2 in collect:
    print('2 is in the tuple')
print(collect.count(1))

#Dictionaries
coll = dict()
coll['key1']= 'value1'
coll['key2']= 'value2'
coll['key3']= 'value3'

coll2 = {'key1':'value1','key2':'value2','key3':'value3'}
coll2.clear()
print(coll2.get('key1'))
coll.pop('key2')
print(coll2)

for i in coll2.keys():
    print(i)
for i in coll2.values():
    print(i)

#set
col = {'a','b','c'}
col.add('d')
print(col)
col.discard('a')
print(col)
col.pop()
print(col)
col2 = {"c","d","e"}
print(col.intersection(col2))
print(col.union(col2))
col3 = {'a','b'}
print(col2.issubset(col))

#None
#immutable keyword in python

x = None

if x is None:
    pass

