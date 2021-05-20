def pooja_rani(x,y):
    # hcf=0
    if x>y:
        smaller=y
    else:
        smaller=x
    for i in range(1,smaller+1):
        if x %i==0 and y%i==0:
            hcf=i
    return hcf
num1=int(input("enter first number:"))
num2=int(input("enter second number:"))

print("the hcf of",num1,"and",num2,"is",pooja_rani(num1,num2))

# oja_rani(num1,num2)po









