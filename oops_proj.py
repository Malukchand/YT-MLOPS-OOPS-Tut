class chatbook:
    def __init__(self):
        self.username  = ""
        self.password  = ""
        self.loggedin = True
        self.menu()


    def menu(self):
        user_input = input("""welcome to chatbook!! how would you like to proceed ?
                           1. press 1 to signup
                           2. press 2 to signin
                           3. press 3 to write a post
                           4. press 4 to message a friend
                           5. press any other key to exit """)
        if user_input == "1":
            self.signup()
        elif user_input == "2":
            self.signin()
        elif user_input == "3":
            pass
        elif user_input == "4":
            pass
        else:
            print("thank you for using chatbook!! goodbye!!")
            exit()
    def signup(self):
        email = input("enter your email here :")
        pwd = input("enter your password here :")
        self.username = email
        self.password = pwd
        print("you have signed up succesfully !!")
        print("\n")
        self.menu

    def signin(self):
        if self.username == '' and self.password == '':
            print("please signup first by pressing 1 in the menu")
        else:
            uname = input("enter your email here :")
            pwd = input("enter your password here :")
            if self.username == uname and self.password == pwd:
                print("you have signed in succesfully !!")
                self.loggedin = True
            else:
                print("please enter correct credentials..")
        print("\n")
        self.menu()


obj = chatbook()