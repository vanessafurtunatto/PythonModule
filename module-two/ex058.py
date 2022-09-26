phrase = str(input('Type a phrase: ')).strip().upper()
words = phrase.split()
tgt = ''.join(words)
inverse = ''
print('You typed the phrase: {}'.format(phrase))
for words in range(len(tgt) - 1, -1, -1):
    inverse += tgt[words]
if inverse == tgt:
    print('We have a palindrome')
else:
    print('We dont have a palindrome')


