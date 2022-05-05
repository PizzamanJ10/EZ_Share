
def do_power(first_num,second_num):
    #Help me Yehuda!!!
    number = first_num
    for i in range(second_num-1):
        first_num *= number
    return first_num 
    


#this is a program that gets 2 numbers and returns one in the power of the other.
print("This is a program that gets 2 numbers and returns one in the power of the other.")

#get numbers
first_num = int(input("Please input the first number:"))
second_num = int(input("Please input the second number:"))

print(do_power(first_num, second_num))

