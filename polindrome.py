# function which return reverse of a string
w = input("Write a word: ").lower() 

def isPalindrome(w):
    polindrome=0
    if w == w[::-1]:
            polindrome=polindrome+1
    else:
            polindrome=polindrome+0
    return polindrome
# Driver code


print(w[::-1])

print(isPalindrome(w))
