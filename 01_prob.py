# '''Given an integer,n , perform the following conditional actions:
# If n is odd, print Weird
# # If n is even and in the inclusive range of 2 to 5, print Not Weird
# # If n is even and in the inclusive range of 6 to 20, print Weird
# # If n is even and greater than 20 , print Not Weird '''


n = int(input("enter the number ")) # here user will enter the number
if n%2 != 0 or n in range(6,20): # in this line were we have applied some range and put n%2 !=0  it will provide the output as "wierd"
    print("wierd")
elif n%2 == 0 or n in range(2,5) and n%2 ==0 or n>20: # in this line we have entered some range and the output will be as "not wierd"
    print("not wierd")  
       

