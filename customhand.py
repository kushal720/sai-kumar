class Error(Exception):
    pass
class AmountException (Error):
    print("WELCOME TO ATM ")
class customgeneric (Error):
    pass
a= int(input("Enter the Number : "))
try:
    if a>=500 and a<2000:
        print("The withdraw Amount is vaild , Debited from your Account")
    else:
        raise AmountException
except AmountException:
    print("The Amount Enterned is invaild. only 500 and 2000 Notes")
finally:
    print("THANKING YOU , NEVER VIST YOU AGAIN")
