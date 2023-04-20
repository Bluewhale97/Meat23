#RegEx regular expression
# is a sequence of chars that forms a search pattern
# a built in package called re
import re
txt="The x in Spain"
#search the first match
x=re.search('^The.*Spain$',txt) # x is a nonetype or a re.Match object, NoneType means no matched string
type(x)
if x:
  print('yes')
else:
  print('no')

#findall
#return all the matchs otherwise return empty list, not the complete values, just 'i'
x=re.findall('i',txt)
x

#split your string using split()
x=re.split('\s',txt)
x

# sub() replace a str with another str, do not input numeric values
x=re.sub("\s","9", txt)
x

# span() to return a tuple containing the start- and end positions of the first match
x=re.search('i',txt)
x.span()

#search() to pass into the function
x=re.search('i',txt)
x.string


#group() to return the part of the string where there was a match
x=re.search(r"\bS\w+",txt)
x.group()
