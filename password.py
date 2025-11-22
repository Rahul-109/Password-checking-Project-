import re

#this function is to check the strength of password
def password_checking (pw):
    x = ["123456789", "abcdefghi", "qwertyuio", "000000000"]
    if pw.lower() in x:
        return "very weak password : It is a common password"


    if not any(a.isupper() for a in pw):
        return "weak password : Add upper case letter"
    if not any( a.isdigit() for a in pw):
        return "very weak password : Add a digit "
    if len(pw) < 9:
        return " very weak password : it should contain more than 8 letters  "
    if not any(a.islower() for a in pw):
        return "weak password : Add lower case letter"
    if not re.search(r'[ @!#$%^&]', pw):
        return "medium password : It should contain a special character"

    return "you have a strong and secure password!!!"
#this is to check the strength of the password by using above conditions and if it clears all the given conditons the  its safe and final return will display the output


def user_input ():
    #the main function is to take input from the user and check strength of the password
    print (" Welcome to the password checker !! ")
    while True:
        pw = input ("enter your password (or type 'quit' to exit): ")
        if pw.lower() == "quit":
            print (" Thankyou for using password checker !! ")
            break

        final= password_checking(pw)
        print (final)

#To run this password checker
if __name__=="__main__":
    user_input()
