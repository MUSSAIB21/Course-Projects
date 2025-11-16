#1
"""
sentence=input("Enter a sentence: ")
broken=sentence.split()
print("The sentence has",len(broken),"words")
"""
#2
"""
def doesitHave(alp, word):
    if all(i in word for i in alp):
        return True
    else:
        return False
alp=input("Enter the alphanumeric set: ")
word=input("Enter a word: ")
print(doesitHave(alp,word))
"""
#3
"""
def noVowels():
    vowels = "aeiou"
    word = input("Enter the Word: ").lower()

    for c in word:

        if c in vowels:
            word = word.replace(c, "")

    return word
print(noVowels())
"""
#4
'''
def noDuplicates():
    word=input("Enter a word: ")
    newword=""
    for c in word:
        if c not in newword:
            newword+=c
    return newword
print(noDuplicates())
'''
#5
"""
def isWordHere():
    sentence=input("Enter a sentence: ")
    word=input("Enter a word: ")
    if any(word in sentence for i in sentence.split()):
        return True
print(isWordHere())
"""
#6
"""
def middleWord():
    word=input("Enter a word: ")
    if len(word)>=6 and len(word)%2==0:
        print(word[(len(word)//2)-2]+word[(len(word)//2)-1]+word[len(word)//2]+word[len(word)//2+1])
    elif len(word)>=5:

        print(word[len(word)//2-1]+word[len(word)//2]+word[len(word)//2+1])
middleWord()
"""
#7
"""
def sumNum():
    sentence=input("Enter a sentence: ")
    numlist=[]
    for i in sentence:
        if i.isdigit():
            numlist.append(int(i))
    print(sum(numlist))
sumNum()

"""

#8
"""
charList=[]
def freqChar():

    sentence=input("Enter a sentence: ")
    for c in sentence:
        freq=sentence.count(c)
        print(c,"is in sentence",freq,"times")

freqChar()
"""
#9
"""
def stringCheck():
    if all(i in string2 for i in string1):
        return True
    else:
        return False
string1=input("string1 : ").lower()
string2=input("string2 : ").lower()
print(stringCheck())
"""
#10
"""
def msgmerger(msg,name):
    dict={ name:('"Hello, '+name+':'+msg+'"')

    }
    return dict
print(msgmerger("Congrats! Your application is successful","John"))
"""



