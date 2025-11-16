def isSpecial(s):
    special_characters = "@# $%^&*()-+?_=,<>/"
    if any(c in special_characters for c in s):
        return True
    else:
        return False
print(isSpecial("%"))


