nterms = int(input("How many terms? "))
# The first term n1 will be zero and for the next term i.e n2 it will be 0+1 which is equal to 1 
n1 = 0
n2 = 1
#Intialy the count will be zero
count = 0
# checking if the number of terms are valid or not 
if nterms <= 0:
   print("Please enter a positive integer")
# if there is only one term, return n1
elif nterms == 1:
   print("Fibonacci sequence upto",nterms,":")
   print(n1)
# generating fibonacci sequence
else:
   print("Fibonacci sequence:")
   while count < nterms:
       print(n1)
       nth = n1 + n2
       # updating the values
       n1 = n2
       n2 = nth
       count += 1
