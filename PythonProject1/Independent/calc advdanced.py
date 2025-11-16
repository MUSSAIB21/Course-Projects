def splitter(exp):
    explist=[]
    oplist=[]
    operators=['+','-','*','/']
    for i in exp:
        explist.append(i)
    i=0
    while i<len(explist)-1:
        i+=1
        if explist[i] == '+':
            print(i, 'th iteration')
            print(explist)
            print(explist[i - 1], explist[i + 1])
            tmprslt = float(explist[i - 1]) + float(explist[i + 1])
            explist.remove(explist[i + 1])
            explist.insert(i + 1, tmprslt)
            explist.remove(explist[i - 1])
            explist.remove(explist[i - 1])
            print(explist)
            i = i - 1
            if explist[i] == '+':
                print(i, 'th iteration')
                print(explist)
                print(explist[i - 1], explist[i + 1])
                stmprslt = float(explist[i - 1]) - float(explist[i + 1])
                explist.remove(explist[i + 1])
                explist.insert(i + 1, stmprslt)
                explist.remove(explist[i - 1])
                explist.remove(explist[i - 1])
                print(explist)
                i = i - 1

    print(explist)
splitter(input('enter expression'))

def myadd():

    expression=input('enter expression')
    expression=expression.split('+')


    print(expression)
    for i in range(1,len(expression)-1,2):
        if expression[i]=='+':
            print(float(expression[i-1])+float(expression[i+1]))
        elif expression[i]=='-':
            print(float(expression[i - 1]) - float(expression[i + 1]))
        elif expression[i] == '*':
            print(float(expression[i - 1]) * float(expression[i + 1]))
        elif expression[i] == '/':
            print(float(expression[i - 1]) / float(expression[i + 1]))



