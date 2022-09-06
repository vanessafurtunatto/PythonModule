phrase = str(input('Type a phrase: ')).upper().strip()
print('the letter A appears {} times'.format(phrase.count('A')))
print('the first letter A appears in {} place'.format(phrase.find('A')+1))
print('the last letter A appears in {} place'.format(phrase.rfind('A')+1))