'''program to print first n prime numbers'''

def is_prime(num):
   for i in range(2,num//2+1):
      if num%i==0:
         return False
   return True


N=int(input("Enter the value of N:"))
i=2
count=0
while True:
   if is_prime(i):
      print(i,end=" ")
      count+=1
   i+=1
   if count==N:
      break