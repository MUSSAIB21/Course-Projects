f = open("myfile.txt", "w")
f.write("Now this file has more content")
f.close()
#open and read the file after the appending:
f = open("myfile.txt", "r")
print(f.read())
print(type(f))
yesking = open("myfile2.txt", "r")
for i in yesking:
#yesking is an iterable made up of strings, every element in it is a string
    y=i.split("||")
    print(y[0]+y[1],type(i))



