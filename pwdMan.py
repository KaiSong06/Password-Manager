import os

def getInput():
        user = input("User: ")
        password = input("Password: ")
        return user, password

def validatePassword(password):
        with open("users.txt", "r") as file:
                data = file.read().split("\n")
                for i in range(len(data)):
                        data[i] = data[i].split(",")
                for i in data:
                        if i[1].strip() == password:
                                return True
        return False

def addUser(user, password):
        #Check if user exists
        with open("users.txt", "r") as file:
                data = file.read().split("\n")
                for i in range(len(data)):
                        data[i] = data[i].split(",")

                for i in data:
                        if i[0] == user:
                                return False
        print(data)      
        #Add user and password
        with open("users.txt", "a") as file:
                file.write("\n")
                file.write(f"{user}, {password}")

        #Create a file for user
        f = open(user+".txt", "x")
        f.close
        return True

def addPassword(user, webName, webUser, password):
        try:
                with open(user+".txt", "a") as file:
                        file.write(f"{webName}, {webUser}, {password}")
                return True
        except FileNotFoundError:
                return False

def checkPassword(user, webName):
        try:
                with open(user+".txt", "r") as file:
                        data = file.read().split("\n")
                        for i in range(len(data)):
                                data[i] = data[i].split(",")
                        for name in range(len(data)):
                                if data[i][0] == webName:
                                        return data[i][1], data[i][2]
        except FileNotFoundError:
                return False
        
def checkOrAdd(options, user):
        print("a")
        if options == "add":
                webName = str(input("Website name: "))
                webUser = str(input("Username or email: "))
                webPassword = str(input("Password: "))
                addPassword(user, webName, webUser, webPassword)
                print("Added")

        elif options == "check":
                webName = str(input("Website name: "))
                info = checkPassword(user, webName)
                if info == False:
                        print("Invalid website name")
                else:
                        print(f"Username: {info[0]}")
                        print(f"Password: {info[1]}")
def main():
        #Get user
        username, password = getInput()
        userAdded = addUser(username, password)

        #Check for user
        if userAdded == True:
                print("User added")


        elif userAdded == False:
                validate = validatePassword(password)
                if validate == False:
                        print("Invalid Password")
                        exit()
                print(f"Welcome {username}")
                options = input("Check password or add password? (check/add): ")

                #Add new password
                options = checkOrAdd(options, username)





main()


