# string methods
'assa'.capitalize() # capitalize the index 0 of a string, it will not do anything if the index 0 is not a letter

'i am GOOD'.casefold() # make all the letters into lower case in a string

'banana'.center(10,'0') # center(lenth, character), length is the total length of the str 'o' is the character, default character is "".

'banana'.count('a', 1,2) # count(value, start, end), value can be a string, start at index 1, end at index 3, exclusively

'My name is stale'.encode(encoding="ascii",errors="backslashreplace") #encode(encoding=encoding, errors=errors), default encoding is UTF-8, errors methods can be "backslashreplace", "ignore", 'namereplace', "strict", 'replace', 'xmlcharrefreplace'

"hello!".endswith("!",1,) # endswith(value, start, end), check if the str ends with the value

"H\te\tl\tl\to".expandtabs(tabsize=2) # expand tab size, it's like copy all the tabs to 2 times of original 

"hello, it is me".find('it', 2,) # find(value, start, end), find first occurence of the value location in a string, it will return -1 means the value is not found, the difference between find() and index() is that index() will raise an error while not found

"hell{}, i{} is me".format('o','t')#format(val1, val2, ...valn)

"hello, {a} is {b}".format_map({"a":"it","b":"me"})#format_map(dict), format_map() method can get the values from keys of a dict

"hello, it is me".index("it", 2, )# difference between find() and index() is that index() will raise an error while not found it but find() returns -1

"i am good at that".isalnum()#isalnum() method returns True if all the chars are alphanumeric, in this case it's false because it contains whitespaces

"iamgood".isalpha() #isalpha() method returns True if all the chars are alphabet

"i am good".isascii() # returns True if all the chars are ascii

"\u0030232".isdecimal() # returns True if the chars/str in unicode are decimals(0-9)

"3121".isdigit() # returns True if the chars in str are all digits, ² is digit too

"a_ewhi".isidentifier() # returns True if the string is a valid identifier, identifier is the str that meet the principles of naming an object

"asf \ed".islower() # returns True if all the letters are lower case, not include escape chars like whitespace and slash

"2133 321".isnumeric() # returns True if all the chars are all numeric, this one includes whitespace and so on escape chars

"32\r".isprintable() # carriage return and lind feed included strs are considered as not printable

' '.isspace() # returns True if all the chars are whitespaces

'I Am Good'.istitle() # returns True if the str follows the rule of a title that is each word start with an upper case letter

'SDAID SD'.isupper() # returns True if all the chars are upper case, not include escape chars like whitespace and slash

'hello how are you'.join('as is good') # join(iterable), join the str with an interable, so the str is like a separator. When passing a dict in join method, the returned values are the keys not the values

myDict = {"name": "John", "country": "Norway",'a':1}
mySeparator = "TEST"
x = mySeparator.join(myDict)
print(x)

'banana'.ljust(20,'o')# ljust(length, character), character is to fill the missing space to the right of the string, the default is "", length is required for the length of the returned string

'base_A C'.lower() # returns a string where all the chars are lower case, symbols and numbers are ignored

",,,,,ssaaww.....banana".lstrip(',saw.') # lstrip(characters), characters to remove as leading characters, the default is space ""


#maketrans(x,y,z), x is a str for chars that need to be replaced, y is chars to replace with, and y should have the same length as x, z is to descirbe chars to remove from the original string. To be noticed, if only one param is specified, x should be a dictionary like {'a':'b',"f":"c"}, means that a is replaced by b
table = str.maketrans({"a":"b"})
"as".translate(table)# use translate() with

table = str.maketrans("a",'b',"c")
"abc".translate(table) # use translate() with

"I could eat bananas all day".partition('bananas')#partition(value), if value is not found, returns a tuple containing 1. the whole string, 2. an empty string 3. an empty string. If the value found, part it into three parts, the value str is the second one. 

"I like dragon".replace('drag','lem')#replace(oldvalue, newvalue, count), old value is the string to search for, newvalue is the string to replace the old value with, and the count is a number of how many occurrences of the old value you want to replace, default is all occurrences.

'i like dragon, dragon, drag'.rfind('dragon', 4,) # rfind(value, start, end), right find, to find the last occurrence(index) of a value in the string from the starting point to the end. If it doesnt find, return -1

"i like dragon".rindex('i') #rindex(value, start, end), right index, find the last occurrece almost same as rfind(), but it will raise exceptin if not found

'a'.rjust(5,'0')#rjust(length, character), like ljust(), length is total length and character is the padding character, then right align the string

"i could like that, because that is my favorite".rpartition('that')#rpartition(value), searchs for the last occurrence a specified string and splits into a tuple of three elements. If the value not found, return a tuple containing 1. an empty string. 2. an empty string 3. the whole string

"apple, banana, cherry".rsplit(',',-1)#rsplit(separator, maxsplit), find the last occurrence of the separator and start from the right side to split the string, the maxsplit -1 means split all

"  baababa   ".rstrip('a ')#rstrip(), remove any specfied set of characters at the end of the string, the default is whitespace

"i like that, yes it is,".split("i",1)#split(separator, maxsplit)

'i like it, yes i like \nit'.splitlines(True)#splitlines(keeplinebreaks) splits a string into a lits, the splitting is done at line breaks. keeplinebreaks choosed to be True or False

'hello, i am good'.startswith('hello')#startswith(value, start, end), returns True if the string starts with the specified value, otherwise False

"  i like them     ".strip(" ")#strip(characters), remove any leading and trailing chars in the string

"i Like it SO much".swapcase() # swap upper and lower case

"i love that *so 3much".title() #title() returns a string where the first char in every word is upper case, if the word contains a number or a symbol,the first letter after that will be converted to upper case

'ad23*"'.upper() # convert a string to upper, symbols and numbers are ignored

"aer  ".zfill(10) #zfill(len), fill the string a specified number of 0 values at the begining. len is desired length of the string, and if len is less than the len of original str, it will just return the original str
