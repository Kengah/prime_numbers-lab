def primeNumbers(num):
 list_of_prime_numbers = []

 for i in range(2, num):
   prime = True

   for x in range(2, i): # 2,3
     if i % x == 0: 
       prime = False

   if prime == True:
     list_of_prime_numbers.append(i)

 return list_of_prime_numbers

print (primeNumbers(8))