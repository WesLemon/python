# .index returns the index of the first value equal to the parameter
spam = ['hello', 'hi', 'howdy', 'heya']
print('Index: "howdy" is at index ' + str(spam.index('howdy')))

# .insert inserts value at the index and moves all after up 1
spam.insert(1, 'yo')
print('Insert: ' + str(spam))

# .append adds the value to the end
spam.append('sup')
print('Append: ' + str(spam))

# .remove removes only the first value, whereas del removes at the index
spam.remove('sup')
print('Delete: ' + str(spam))
del spam[1]
print('Del: ' + str(spam))

# .sort can take an optional parameter
spam.sort()
print('Sort (ASCII-betical) : ' + str(spam))
spam.sort(reverse=True)
print('Reverse: ' + str(spam))
spam.sort(key=str.lower)
print('Alphabetical order: ' + str(spam))
