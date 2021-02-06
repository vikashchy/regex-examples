## Regex : Special Sequences
```` 
 \d -> Single character 0-9
 \D -> Non digic characer
 \s  -> White space
 \S  -> Non white space
 \w  -> Any alphanumeric characet a-z
 \W  -> Non alphanumeric word
 \b  -> Space around words
 \A -> Match at the start of the string
 \Z -> Match at the end of the string.
 \B -> Returns a match where the specified characters are present, 
but NOT at the beginning (or at the end) of a word
````
## Regex Quantifiers: Multiple characters matching

````
+     -> One or more repetition
*     -> Zero or more
?     -> 0 or 1
{m}   -> exactly m no of regular expression
{m,n} -> minimum no of occurrences, n is the max no occurrences
````
## Regex functions
###### findall
```` 
Returns a list containing all matches 
````
###### search
````
Returns a Match object if there is a match anywhere in the string
````
###### split
```` 
Returns a list where the string has been split at each match
````
###### sub
````
Replaces one or many matches with a string
````

## Regex : Metacharacters
````
[]  A set of characters	        "[a-m]" 
\   Signals a special sequence (can also be used to escape special characters)	"\d"
.   Any character (except newline character)            "he..o"
^   Starts with                 "^hello"
$   Ends with                   "world$"
*   Zero or more occurrences	"aix*"
+   One or more occurrences     "aix+"
{}  Excactly the specified number of occurrences	"al{2}"
|   Either or	                                        "falls|stays"
()  Capture and group
````

# Regex : Sets
````
[arn]	Returns a match where one of the specified characters (a, r, or n) are present
[a-n]	Returns a match for any lower case character, alphabetically between a and n
[^arn]	Returns a match for any character EXCEPT a, r, and n
[0123]	Returns a match where any of the specified digits (0, 1, 2, or 3) are present
[0-9]	Returns a match for any digit between 0 and 9
[0-5][0-9]  Returns a match for any two-digit numbers from 00 and 59
[a-zA-Z]    Returns a match for any character alphabetically between a and z, lower case OR upper case
[+]         In sets, +, *, ., |, (), $,{} has no special meaning, so [+] means: return a match for any + character in the string
````

# Regex : Functions of Match Object
````
.span() returns a tuple containing the start-, and end positions of the match.
.string returns the string passed into the function
.group() returns the part of the string where there was a match
````
