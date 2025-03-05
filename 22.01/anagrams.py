def is_anagram(word, keyword):
    return sorted(word)==sorted(keyword)

words = ['listen', 'silent', 'enlist', 'google', 'inlets', 'banana']
keyword = 'listen'

result = filter(lambda word: is_anagram(word, keyword), words)
print(list(result))