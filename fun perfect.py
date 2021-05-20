#Ek perfect() naam ka function define kijiye jo ki ek parameter 
# lega aur uss parameter ko hume check karana hai ki vo perfect number hain ya nahi.
#  Iske baad uss function ko use karke ek program likhiye jo ki 1 se 1000 tak sabhi perfect numbers ko print kare.
# [ hum ek aise integer number ko perfect number kahenge jo ki uske sabhi factors 
# ( including 1 & excluding itself) ka sum uss number ke barabar hota hai. 
# Example:-



# def perfect(num):
#     i=1
#     sum=0
#     while i<num:
#         if num%i==0:
#             print(i)
#             sum=sum+i
#         i=i+1
#     if sum==num:
#         print("it is perfect",i)
#     else:
#         print("not perfect",i)
# perfect(int(input("enter a number")))