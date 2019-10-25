def isPalindrome(string):
    reversedstring = ""
	for i in reversed(range(len(string))):
		reversedstring += string[i]
	return string == reversedstring
    
def isPalindrome(string):
    leftidx = 0
    rightidx = len(string) - 1
    while leftidx < rightidx:
        if string[leftidx]!= string[rightidx]:
            return False
        leftidx +=1
        rightidx -=1
    return True
    
def isPalindrome(string,i=0):
    j = len(string) -1 -i
    return True if i>=j else string[i]==string[j] and isPalindrome(string,i+1)

isPalindrome("abcdefghihgfedcba")
