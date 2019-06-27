## RegEx (Regular Expressions)
All of these notes were taken from this resource, which was one of the most succint resources that I found online about RegEx.

```
https://www.machinelearningplus.com/python/python-regex-tutorial-examples/
```


Regular expressions (regex), is a syntax used to search, extract, and
manipulate specific string patterns from a larger text. It is used in projects
that involve text validation, NLP, and text mining.

Imported via the module **re**

**import re**

**regex patterns**: a special language used to represent generic text, number, or symbols so that it can be used to extract texts that conform to that pattern.

* **(' \s+ ')**: matches any whitespace character
* **(' \d+ ')**: matches any digits character
* **(' (( ?!\n ) \s+ )')**: all whitespace characters besides newlines
* **(' [0-9]+ ')**: matches all numbers from 0 to 9
    - **(' [0-9] {x} ')**: if you know the exact number of digits the string you are searching will have
* **(' [A-Z]+ ')**: matches all occurences of letters A-Z (caps)
    - **(' [A-Z] {x} ')**: if you know the exact number of letters the string you are searching will have
* **(' [A-Za-z]+ ')**: matches all occurences of letters A-Z and a-z (caps and lower)
    - **(' [A-Za-z] {x,} ')**: if you know the matches will have x or more characters


**regex = re.compile(' \s+ ')**
compiles a regular expression pattern that can be used to match at least one more more space characters.

Input:
```
text = """101 COM    Computers
205 MAT   Mathematics
189 ENG   English"""
```

**re.split(' \s+ ', text)**: splits the text around 1 or more space patterns and outputs to list

**regex.split(text)**: does the same as the above

Output:
```
#> ['101', 'COM', 'Computers', '205', 'MAT', 'Mathematics', '189', 'ENG', 'English']
```

**re.findall()**: extracts all occurences of the compiled regex and returns them in a list

**re.search()**: searches for a pattern in a given text and returns a particular match object that contains the starting and ending positions of the first occurence of the pattern (indices)

**re.match()**: also searches for a pattern in a given text, similar to re.search(). However, it requires the pattern to be present at the beginning on the text itself.

**re.sub()**: replace a regex with a given string, can be done one of two ways.

**print(re.sub(' \s+ ', ' ', text)**
or
**regex = recompile(' \s ')**
**print(regex.sub(' ', text))**

#### RegEx Groups

```
text4 = """101   COM   Computers
205   MAT   Mathematics
189   ENG    English"""

1. extract all course numbers
re.findall('[0-9]+', text4)

2. extract all course codes
re.findall('[A-Z]{3}', text4)

3. extract all course names
re.findall('[A-Za-z]{4,}', text4)

#> ['101', '205', '189']
#> ['COM', 'MAT', 'ENG']
#> ['Computers', 'Mathematics', 'English']
```

Instead of writing 3 separate lines to get the individual items, you can use regex groups to write just one unified pattern.

```
course_pattern = '([0-9]+)\s*([A-Z]{3})\s*([A-Za-z]{4,})'

re.findall(course_pattern, text)

#> [('101', 'COM', 'Computers'), ('205', 'MAT', 'Mathematics'), ('189', 'ENG', 'English')]
```
#### Greedy Matching in RegEx

By default, regular expressions will try to extract as many matches as it possibly can, even if you don't need all of it.

For example, in the given HTML tag:
```
text = "< body>Regex Greedy Matching Example < /body>"

re.findall('<.*>', text)

#> ['< body>Regex Greedy Matching Example < /body>']

```

The opposite of greedy matching is **lazy matching**, which will take as little as possible.

```
re.findall('<.*?>', text)
#> ['< body>', '< /body>']
```

If you only want the first match to be retrieved, use the **search** mathod instead.
```
re.search('<.*?>', text).group()
#> '< body>'
```

#### Common Regular Expression Syntax and Patterns
```
BASIC SYNTAX

.             One character except new line
\.            A period. \ escapes a special character.
\d            One digit
\D            One non-digit
\w            One word character including digits
\W            One non-word character
\s            One whitespace
\S            One non-whitespace
\b            Word boundary
\n            Newline
\t            Tab

MODIFIERS

$             End of string
^             Start of string
ab|cd         Matches ab or de.
[ab-d]	    One character of: a, b, c, d
[^ab-d]	   One character except: a, b, c, d
()            Items within parenthesis are retrieved
(a(bc))       Items within the sub-parenthesis are retrieved

REPETITIONS

[ab]{2}       Exactly 2 continuous occurrences of a or b
[ab]{2,5}     2 to 5 continuous occurrences of a or b
[ab]{2,}      2 or more continuous occurrences of a or b
+             One or more
*             Zero or more
?             0 or 1
```
