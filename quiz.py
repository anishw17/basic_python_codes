import time

print("let's play a quiz")
print('type the options only!'.upper())
print()
print('Q.1)Which of the following belongs to Donald Trump :\n(A): JW Marriot NYC\n(B): Grand Hyatt NYC\n(C): Ritz Carlton Chicago\n(D): Ritz Carlton NYC')
print()
ans = input('enter your answer :').upper()
if ans == 'B' :
    print('correct')
elif ans == 'A':
    print('wrong its option B')
elif ans == 'C':
    print('wrong its option B')
elif ans == 'D' :
    print('wrong its option B')
else:
    print('ans not supported')
print()
time.sleep(2)
#print()
print('Q.2) Which is the richest Royal Family in the world? :')
print('(A): British Royal Family')
print('(B): Spanish Royal Family')
print("(C): Saudi's Royal Family")
print("(D): UAE's Royal Family")
print()
ans1 = input('enter your answer :').upper()
if ans1 == 'C' :
    print('correct')
    ans1 = True

elif ans1 == 'A':
    print('wrong its option C')
elif ans1 == 'B':
    print('wrong its option C')
elif ans1 == 'D' :
    print('wrong its option C')
else:
    print('ans not supported')
print()
time.sleep(2)
print('Q3.) Which country is going to host G20 Summit in 2023?')
print('(A): India')
print("(B): USA")
print('(C): France')
print('(D): Taiwan')
print()
ans2 = input('enter your answer :').upper()
if ans2 == 'A' :
    print('correct')
elif ans2 == 'B':
    print('wrong its option A')
elif ans2 == 'C':
    print('wrong its option A')
elif ans2 == 'D' :
    print('wrong its option A')
else:
    print('ans not supported')
