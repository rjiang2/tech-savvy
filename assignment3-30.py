def any_lowercase1(s):
    for c in s:
        if c.islower():
            return True
        else:
            return False
# If the first letter is lowercased, then return true. If the first letter is uppercased, then return false. It will not go to the second letter.

def any_lowercase2(s):
    for c in s:
        if 'c'.islower():
            return 'True'
        else:
            return 'False'
# No matter what is entered, it will always return true, because it goes through the string 'c', not what is entered. And c is lowercased.

def any_lowercase3(s):
    for c in s:
        flag = c.islower()
    return flag
# Return the value of the last letter in string 's'. If it is lowercased, return true. If uppercased, return false.


def any_lowercase4(s):
    flag = False
    for c in s:
        flag = flag or c.islower()
    return flag
#If there is any lowercased letter in string 's', return true. If all uppercased, return false.

def any_lowercase5(s):
    for c in s:
        if not c.islower():
            return False
    return True
#If there is any uppercased letter in the string 's', return False. If all lowercased, return True.

def convert(str):
    print (chr(ord(str) + 2))

raw = 'g fmnc wms bgblr rpylqjyrc gr zw fylb. rfyrq ufyr amknsrcpq ypc dmp. bmgle gr gl zw fylb gq glcddgagclr ylb rfyrq ufw rfgq rcvr gq qm jmle. sqgle qrpgle.kyicrpylq() gq pcamkkclbcb. lmu ynnjw ml rfc spj.'

for i in raw:
    convert(i)