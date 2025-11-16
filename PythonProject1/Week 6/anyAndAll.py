specialNumbers="AEIOU"
majorana=input("Enter the majorana: ")
print(any(c in specialNumbers for c in majorana))
print(all(c in specialNumbers for c in majorana))