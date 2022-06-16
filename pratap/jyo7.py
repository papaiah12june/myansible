n1=int(input("Enter the first number:"))
n2=int(input("Enter the second number:"))
n3=int(input("Enter the third number:"))
if n1<n2 and n1<n3:
  print("The smallest number:",n1)
elif n2<n3:
  print("The smallest number:",n2)
else:
  print("The smallest number:",n3)