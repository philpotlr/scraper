import re
 
# Using * asterisk - multiple occurrences of the character preceding it
print re.findall("ab*c", "ac")     # ['ac']
print re.findall("ab*c", "abcd")   # ['abc']
print re.findall("ab*c", "acc")    # ['ac']
print re.findall("ab*c", "abcac")  # ['abc', 'ac']
print re.findall("ab*c", "abdc")   # []
print re.findall("ab*c", "ABC")    # [] case sensitive

print re.findall("ab*c", "ABC", re.IGNORECASE)


# Using a period - any single occurance
print re.findall("a.c", "abc")
print re.findall("a.c", "abbc")
print re.findall("a.c", "ac")
print re.findall("a.c", "acc")


#combining . with *
print re.findall("a.*c", "abc")
print re.findall("a.*c", "abbc")
print re.findall("a.*c", "ac")


# Using re.search()
results = re.search("ab*c", "ABC", re.IGNORECASE)
print results.group()


a_string = "Everything we do is <replaced> if it is indeed inside <tags>."
# Substitute the tags with 'coming up roses' using the re.sub() method
a_string = re.sub("<.*>", "coming up roses", a_string)
print a_string