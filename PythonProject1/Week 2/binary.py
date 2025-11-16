x = 0b10 # this is binary number 10, what’s this in base 10?
         #A)in base 10 this is 2

y = 0b11 # this is binary number 11, what’s this in base 10?
         #A)in base 10 this is 3
print(x&y) # bitwise AND
           #A)AND operator turns each bit to 1 if both bits are 1 and 0 otherwise. So,
           #x in binary is 10
           #y in binary is 11
           #AND operator will turn it into 10 which is 2 in decimal, hence our result

print(x|y) # bitwise OR
           #A)OR operator turns each bit to 1 if either bit is 1 and 0 otherwise. So,
           #x in binary is 10
           #y in binary is 11
           #OR operator will turn it into 11 which is 3 in decimal, hence our result

print(~x) # bitwise NOT
          # A) the NOT operator inverts all the bits. So,
          # x which is 0010 becomes 1101 which is -3 in decimal.

print(~y) # bitwise NO
          #A) the NOT operator inverts all the bits. So,
          #y which is 0011 becomes 1100 which is -3 in decimal.