## Lists

#### Lists are mutable and are subject to common and mutable sequence types

### Creating Lists
list_1 = [ ]  
list_2 = list()  
list_3 = [1, "Hi", 3.4]  

### Creating Nested List 
list_4 = [list_2, list_3, "Hi", 4]

### Indexing Lists
Method One: list_name[i]
Method Two: list_name[start:stop:step]
    
+ sign will concatenate a list instead of adding elements together
* sign will repeat a list n times instead of multiplying elements together

### Simple Actions 
len(my_list)
min(my_list)
max(my_list)
my_list.index(x) # outputs index of first instance of x in list
my_list.count(x) # outputs total number of occurrences of x in list

### Sorting Lists
sorted(): function, does not modify original list, returns copy of original list
list.sort(): method, modifies the original list and returns it sorted

### Adding Elements to end of list
append method: my_list.append(x)
manual append: my_list[len(my_list):len(my_list)] = ['New']

extend method: my_list.extend(['New']) : must added as a list or will add N,e,w
manual extend via slicing: same as manual append
manual extend via concatenation:
	my_list = [1,4,36.3,"G",True]
	new_list = ["New"]
	my_list += new_list
Difference between extend and append
Append adds the new element(if list) as a nested list
Extend adds the new element(if list) as individual elements

### Inserting Elements
my_list.insert(index position, element)
my_list[2:2]=['New']
.insert method will add elements as an item
slicing insert will add elements as a sequence

.insert is similar to .append in this sense
slicing is similar to .extend in this sense

### Removing Elements
manual delete via slicing
del my_list[1:3]

.remove method
my_list.remove('element') : delete 'element' in place; will only remove first item that matches

.pop method
my_list.pop(3): retrieves item at element 3 and removes it in place

### Copying Lists
View, Shallow Copy, Deep Copy


## String Methods

Strings can only be sorted()

str.lower()
str.upper()
str.capitalize()
str.isalpha()
str.isdigit()
str.find('string'): search string object for given string and returns first index of where it begins
str.replace('string','replacement_string') replaces all occurences of string with replacement
str.split(): returns of list of substrings separated by default delimiter (space)
    .split(';'): can set the delimiter
str.join(list): joins list without space by default, can indicate space
    " ".join(list)


str.format

Cannot apply .sort() to tuples, only sorted()
