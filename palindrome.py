from ast import Num
from tkinter import N


n = int(input("enter num:"))
temp = n
rev = 0

while(n>0):
    digit = n%10
    rev = rev*10 + digit
    n = n//10

if(temp == rev):
    print("the given is palindrom")

else:
    print("the given number is not a palidrome")