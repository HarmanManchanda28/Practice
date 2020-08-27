def lengthOfNum(x):
    l = 1
    while (int(x/10) != 0):
        l = l + 1
        x = int(x/10)
    return l

def armsum (x , l):
    sum = 0
    while (int(x) != 0):
       rem = x%10
       sum = sum + pow (rem, l) 
       x = int(x/10)
    return sum
    

        
IP = input("Enter the number")
SumIP = armsum (int(IP), lengthOfNum(int(IP)))
print (SumIP)
if SumIP == int(IP):
     print ("It is an Armstrong number")
else:
     print ("Not an Armstrong number")

#loops

## while

# while (expr), expr has a boolean result, eg: x> 5, x!=0, x==0
# keeps running till expr is true.
# expression to figure out how many times to run the loop
# x = 5 
# while(x > 2):
#   print("Reeza")
#   x = x - 1 

## for
# set of values for which to run the loop.
## for x in range(0,5):  <- set to iterate. range(0,5)=> [0,1,2,3,4]
## y = [1,2,3],   for i in y: