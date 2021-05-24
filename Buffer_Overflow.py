print("Password should be of 8 characters")
print("First letter should be in CAPS\nPassword Should be Alphanumeric\nLast character should be in LOWERCASE or UPPERCASE")
password =input("Enter Password=")
a=ord(password[0])
b=ord(password[(len(password)-1)])

if(len(password)==8 and password.isalnum() and (a>=65 and a<=90 and b>=97 and b<=122 or b>=65 and b<=90)):

   print("Valid Password")
else:

   print("Not a Valid Password")
