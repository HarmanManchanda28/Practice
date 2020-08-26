def Compound_Interest (principal, rate, time):
    amount = principal * pow( ( (1 + rate * (0.01))) , time)
    CI = amount - principal
    return CI

##Power function x^y = pow (x,y)


print (Compound_Interest(100, 5, 2))



