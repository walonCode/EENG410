## a dictionary is a key value pair

## intializing a dictionary with value
mydict = {
    "name":'Walon',
    "age": 24,
    "address":"123 Kortright FBC"
}
print(mydict)

## get value from a dictionary
print(mydict["name"])

## getting value from a dictionary using the .get() method
print(mydict.get('surname','Not found'))

## getting the keys  in a dictionary using .key() method
dict_key = mydict.keys()
print(list(dict_key))

## getting the values in a dictionary using the .value() method
dict_value = mydict.values()
print(list(dict_value))

## convert to a tuple, later print as a list
dict_item = mydict.items()
print(list(dict_item))

## adding to a dictionary
mydict['sex'] = 'male'
print(mydict)

##updating a dictionary
mydict['name'] = 'Walon-Jalloh'
print(mydict)

## updating using the .update()
updated_dic = mydict.update({"age":34,"address":'K7 Kortright'})

## deleting a value from a dictionary

## .pop() remove and return value

delete_value = mydict.popitem()
print(delete_value)
