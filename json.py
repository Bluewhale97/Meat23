#json
#json is a syntax for storing and exchanging data
#is a text written with JavaScript object notation

#python has buil-in package called json
import json

#so you can convert any python types into json objects
y = json.dumps({'s':1})
type(y)
#all of py datatypes that convert to json could be a string
#there are some rules of convertion
## python datatype           ##JSON datatype
#  dict                        object
#  list                        array
#  tuple                       array
#  str                         string
#  int                         number
#  float                       number
#  boolean                     boolean
#  None                        null               

#convert json objects to python objects
y_convert = json.loads(y)
type(y_convert)

#mkae your json string more readable, adding the indentation
y2 = json.dumps(y,indent=4)
y2

y3 = json.dumps({'a':1,'b':2}, indent=2, separators=(',','='))#in separators, first one to separate objects, second one to separate key and values
y3

#order the keys
json.dumps(y3, indent=2, sort_keys=True)
