def lowerCase(string):
    lower = True
    for str in string:
        if ord(str) >=97:
            print("It contains a lowercase")
            break
            

        else:
            print("it contains an uppercase")
            return
    answer = input("Do uo wish to convert to uppercase ")
    if answer == "y":
        for str in string:
            print("{:c}".format(ord(str) -32), end="")
       



lowerCase("goke")
