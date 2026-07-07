mydict = {'rajan':54,'pranay':52,'ketan':43,'ishant':40,'hardik':38}
print(mydict)
print(mydict.items())
print(mydict.keys())
print(mydict.values())
mydict.pop('ketan')
print(mydict)
youdict= mydict.copy()
print(youdict)
print(mydict.values())
mydict.update({'anuj':30})
print(mydict)

for key,value in mydict.items():
    print(key,value)

keys= mydict.keys()
values= mydict.values()
print(keys)
print(values)

newkey=['banana','apple','mango','orange']
value={40,50}
dict1=mydict.fromkeys(newkey,value)
print(dict1)