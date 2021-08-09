# namedtouple()
# import collections

# employees=collections.namedtuple('employees',["name","empId","salary"])

# e1=employees("Raju","10001","25000")

# print(e1[0])


# OrderedDict()
# import collections

# d1=collections.OrderedDict()
# d1['name']="Anoop"
# d1['rollno']="22"
# d1['admno']="100001"

# for key,value in d1.items():
#     print(key,value)




#Counter()
# import collections

# x=collections.Counter(["Hello","Hello","Hai"])

# print(x)

# DefaultDict

# import collections

# x=collections.defaultdict(str)

# x["name"]="Rahul"
# x["Rollno"]="12"

# print(x)
# print(x["Admnooo"])

#Deque - Doubly Ended Queue

# import collections

# x=collections.deque([1,2,3,4,5])

# x.pop()
# x.popleft()
# print(x)


# ChainMap
import collections

dict1={"name":"Rahul","age":22}
dict2={"name":"Sooraj","age":23}

comb_dict= collections.ChainMap(dict1,dict2)

print(comb_dict.maps)

# print(list(comb_dict.values()))







