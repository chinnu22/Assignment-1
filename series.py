'''program to find the sum of the series'''

num=int(input("Enter a number:"))
sum=0
if num>0:
   for i in range(1,num+1):
      fact=1
      for j in range(1,i+1):
         fact*=j
      sum+=1/fact
print(f"the result is {sum}")
  