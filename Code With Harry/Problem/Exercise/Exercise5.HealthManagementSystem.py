import datetime


def getdate():
    return datetime.datetime.now()


print('There are 3 Client in Our System : Yash, Vicky, Aaditya')
print("'1' for Yash, \n'2' for Vicky, \n'3' for Aaditya")
client_id = int(input("Enter Client Id : "))
if client_id == 1:
    print('1:input data, 2:GetData')
    key = int(input())
    if key == 1:
        f = open("Yash.txt", "a")
        print("What did u Eat ?\n")
        yash_food = input()
        f.write(yash_food)
        print("What did u Exercise ?\n")
        yash_gym = input()
        f.write(yash_gym)
        f.close()
    elif key == 2:
        f = open("Yash.txt", "rt")
        print(f.read())
        f.close()
elif client_id == 2:
    print('1:input data, 2:GetData')
    key = int(input())
    if key == 1:
        f = open("Vicky.txt", "a")
        print("What did u Eat ?\n")
        vicky_food = input()
        f.write(vicky_food)
        print("What did u Exercise ?\n")
        vicky_gym = input()
        f.write(vicky_gym)
        f.close()
    elif key == 2:
        f = open("Vicky.txt", "rt")
        print(f.read())
        f.close()

elif client_id == 3:
    print('1:input data, 2:GetData')
    key = int(input())
    if key == 1:
        f = open("Aaditya.txt", "a")
        print("What did u Eat ?\n")
        aaditya_food = input()
        f.write(aaditya_food)
        print("What did u Exercise ?\n")
        aaditya_gym = input()
        f.write(aaditya_gym)
        f.close()
    elif key == 2:
        f = open("Aaditya.txt", "rt")
        print(f.read())
        f.close()
else:
    print("Invalid Id")
