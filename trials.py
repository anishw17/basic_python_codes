def palindrome(s):
    s = s.lower()
    return s == s[::-1]
t= int(input('ENTER THE NUMBER OF TEST CASES :'))
if t >=2 and t <=25 :
    for d in range(t):
        str = input('ENTER THE STRING :')
        if len(str) >=2 and len(str)<=100 :
            if palindrome(str):
                print('IT IS A PALINDROME!')
            else:
                print('IT IS NOT A PALINDROME!')
        else:
            print('STRING LENGHT SHOULD BE GREATER OR EQUAL TO 2 AND LOWER OR EQUAL TO 100!')
else:
    print('NUMBER OF TEST CASES SHOULD BE GREATER OR EQUAL TO 2 AND SMALLER OR EQUAL TO 25!')


