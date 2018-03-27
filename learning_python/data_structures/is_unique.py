##is unique
## tests to show that a string only contains uniqe data structors

##frist crack at it
def unique1(testString):
    dic = {}
    for letter in testString:
        if letter in dic:
            return False
        else:
            dic[letter] = letter
    return True

##secound crack at it
def unique2(testString):
    for i in range(len(testString)):
        for j in range(len(testString)):
            if ((j != i) and (testString[i] == testString[j])):
                return False
    return True

