
# Converts given string to pig latin and prints it 
# Takes first letter of word, moves it to end and adds 'ay'
# If word begins with a vowel, simply ends in 'ay'
# Prints the total number of words along with the number of words starting with vowels


wordList = input('Sentences to convert to pig latin: ').lower().split()
length = len(wordList)
print(' > Number of words: %d\n' % length)
vowels = ('a', 'e', 'i', 'o', 'u')
voWo = 0
regW = 0

for word in wordList:
    if ('.') in word:
        if word[0] in vowels:
            voWo += 1
            vowel_end = word.find('.')
            print(word[:vowel_end] + '-ay.')
        else:
            regW += 1
            normal_end = word.find('.')
            print(word[1:normal_end] + '-' + word[0] + 'ay.')
    else:
        if word[0] in vowels:
            voWo += 1
            print(word + '-ay', end=' ')
        else:
            regW += 1
            print (word[1:] + '-' + word[0] + 'ay', end=' ')

print('\n > Number of words beginning with vowel: %d\n > Number of regular words: %d\n' % (voWo, regW))
quit()