from ast import Num
from math import remainder


num= int(input("enter num:"))

reverse_num = 0
while(num!=0):
  remainder = num%10
  reverse_num = (reverse_num*10) + remainder
  num = num//10

print(f"the  Reverse number of given number is",reverse_num)

