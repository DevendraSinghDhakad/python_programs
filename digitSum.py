#sum of digit 



def getSum(n):
 
  sum=0
  for digit in str(n):
    sum += int(digit)

  return sum
n = int(input("enter num:"))
print("sum of given num digit is",getSum(n))
    
