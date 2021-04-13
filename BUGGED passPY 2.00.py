import codecs
import os
import os.path
import string
import random 

#Startup Phase
print("Welcome to PassPY, the python based, opensource password...")
start = input("Press ENTER to start")

login = 0
while login < 3:
    print("Welcome!\n *UNDER CONSTRUCTION* 1:  New users - register your account\n 2:  Existing users - log in\n 3:  Exit - close the application.")
    login = int(input("Enter a number:\n"))
#registration
    if login == 1:
        print("New user registration is curently under construction")
        #print("user name rules:\n1: ")
        NewUser = input("Enter Username:  ")
        nametest = NewUser + ".txt"
        try:
            usersearch = open(nametest)  #search for user's password file
            usersearch.close()
            print("User name not available")
            #print("user name rules:\n1: ")
            NewUser = input("Try another Username:  ")
            nametest = NewUser + ".txt"
        except FileNotFoundError:
            print("User name is available")
            
        create = open(nametest,"a")  #create user's password file
        password = input("Enter password:  ")
        cypher = codecs.encode(password, 'ROT13')
        create.write(cypher)
        create.close()
        print("Done!  New account created!\nWelcome.")
   

    elif login == 2:
        
        #Login Process
        user_name = input("Enter Username: ")
        nametest = user_name + ".txt"
        try:
            usersearch = open(nametest,"r")  #search for user's password file
            lst = list(usersearch.readlines())
            confirm = lst[0]
            print("Hello " + user_name)
            password = input("Enter Password: ")
            compare = codecs.encode(password, 'ROT13')

            #the issue is between here
            if compare == confirm:
                print("Access Granted")
            else:
                print("else triggered.  Access Denied")
                exit(exit())
        except FileNotFoundError:
            print("Access Denied")
            input("please press enter to continue")
            exit(exit())
        #and here
        
        menu = 0
        while menu < 4:
            print("Menu:\n  1:  New password - register new password\n  2:  List - show passwords\n  3:  *UNDER CONSTRUCTION* Register new user - create another user account\n  4:  create a random password\n 5:  Exit")
            menu = int(input("Enter a number:\n"))
            if menu == 1:
                filea = open(nametest,"a")
                inputask = input("Input new password: ")
                cypher = codecs.encode(inputask, 'ROT13')
                filea.write("\n" + cypher)
                filea.close()
                print("Done!")
            elif menu == 2:
                filer = open(nametest,"r") #"a+" isn't reading the file
                contents = filer.read()
                plaintext = codecs.encode(contents, 'ROT13')
                print("Current Passwords: \n" + plaintext)
                filer.close()
            elif menu == 3:
                print("New user registration is curently under construction.\n Menu:\n  1:  new password - register new password\n  2:  list - show passwords\n  4:  Exit")
                menu = int(input("Enter a number:\n"))
            elif menu == 4:
                menu2 = 0
                print("1: generate a password with all lowercase letters \n 2: generate a password with all uppercase letters \n 3: make a mixed case password \n 4: make a numeric password \n 5: make a password with only punctuation characters")
                menu2 = int(input("Enter a number:\n"))
                if menu2 == 1:
                    filea = open(nametest,"a+")
                    # printing lowercase
                    letters = string.ascii_lowercase
                    create.write( ''.join(random.choice(letters) for  i in range(10)) + 'ROT13' )
                    cypher2 = codecs.encode( ''.join(random.choice(letters) for i in range(10), 'ROT13')
                    filea.write("\n" + cypher2)
                    filea.close()
                elif menu2 == 2:
                    usersearch = open(nametest,"a+")
                    # printing upercase
                    letters = string.ascii_uppercase
                    create.write( ''.join(random.choice(letters) for i in range(10)) + 'ROT13' )
                    cypher2 = codecs.encode( ''.join(random.choice(letters) for i in range(10), 'ROT13')
                    filea.write("\n" + cypher2)
                    filea.close()
                elif menu2 == 3:
                    usersearch = open(nametest,"a+")
                    letters = string.ascii_letters
                    create.write( ''.join(random.choice(letters) for i in range(10)) + 'ROT13')
                elif menu2 == 4:
                    letters = string.digits
                    create.write( ''.join(random.choice(letters) for i in range(10)) + 'ROT13')
                elif menu2 == 5:  
                    letters = string.punctuation
                    create.write( ''.join(random.choice(letters) for i in range(10)) + 'ROT13')
            elif menu == 5:
                filea.close()
                filer.close()
                exit(exit())
    elif login == 3:
        exit()
