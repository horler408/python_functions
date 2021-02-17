# re.match() checks for a match at the beginning of the string
# re.search() checks for a match anywhere in the string

# . matches a single character (except the new line character)
# \w matches any alphanumeric character ([a-zA-Z0-9_])
# \W matches any non-alphanumeric character
# \d matches any digit
# \D matches anything that’s not a digit
# \s matches whitespace
# \S matches anything that’s not whitespace

# ^ matches the beginning of a line
# $ matches the end of a line

# ? means “zero or one” occurrences
# * means “zero or more” occurrences
# + means “one or more” occurrences
# {n} means “exactly n” occurrences
# {n,} means “at least n” occurrences
# {n, m} means “at least n and at most m” occurrences
# Parentheses, (<expression>),
# create a group. Groups are interesting because we can capture the content of a group.

re.match('^.*Roger', 'My dog name is Roger')
re.match('.*', 'My dog name is Roger')

result = re.match('^.*Roger', 'My dog name is Roger')
print(result.group())  # My dog name is Roger

result = re.search('name is (.*)', 'My dog name is Roger')
result.group() will
