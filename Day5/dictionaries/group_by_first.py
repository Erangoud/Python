# Given a list of words, group them by their first letter into a dictionary.
# Example Input: ['apple', 'banana', 'apricot', 'blueberry', 'avocado']
# Output:{'a': ['apple', 'apricot', 'avocado'], 'b': ['banana', 'blueberry']}

data=['apple', 'banana', 'apricot', 'blueberry', 'avocado']

letter={}

for word in data:
    first_word=word[0]
    if first_word not in letter:
        letter[word]=[]
    letter[first_word].append(word)

print(letter)