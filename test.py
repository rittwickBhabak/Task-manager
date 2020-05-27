import json
myList = '{"1":1,"2":1,"3":1,"5":1,"10":3,"x":14}'
x = json.loads(myList)
print(x['1'])