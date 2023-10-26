import time

print('okay so this is just the basic project of pyhthon')
name = (input('enter your name please :'.upper()).capitalize())
#print(name)
time.sleep(1)
print('Hello ' + name + ' this project is about how to set password for anythimg!')
print()
print("now for eg! let's say this is your bank balance!")

rstpassword = input('reset the password here :')
print()
time.sleep(2)
print()
print()
print('okay now your bank balance!')
print()
#time.sleep(3)
password = input('Enter the password to check your bank balance :')
time.sleep(2)
if password == rstpassword :
    print('correct password, this is your bank balance :Rs. XXXX')
else:
    print('Wrong password,please try again!')
time.sleep(3)
print()
print("yeah that's it :)")

print("thanks for watching " + name + ' have a great day ahead! :)')
print()
print('by anish w.'.upper())