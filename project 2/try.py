#key = [1,2,3,4,5,2,4,4,5,1]
#value= [2,3,4,5,6,3,5,5,6,2]
#dicti = dict(zip(list(set(key)),list(set(value))))
#print(dicti)
from urllib.parse import unquote

x = ['%D0%BF%D1%80%D0%B8%D0%B2%D0%B5%D1%82','%D0%BA%D0%B0%D0%BA','%D0%B4%D0%B5%D0%BB%D0%B0']
x2 = []
for i in x:
    x2.append(unquote(i))
print(x2)