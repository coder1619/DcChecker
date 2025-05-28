from time import sleep
from helpers.web import Web
from helpers.string import String

class DcChecker:
    def menu(self):
        print("Dc Checker V1")
        print("[1] Check Random Usernames")
        print("[2] Check Usernames from file")
        print("[3] Exit")
        x = input("> ")

        if x == "1":
            count = int(input("Input How Many You Want To Check\n> "))
            uname_type = input("Input Username Type ('random', 'letters', 'numbers')\n> ")
            length = input("Input Username Length\n> ")
            for _ in range(count):
                sleep(2.5)
                Web().check_user(
                    token=String().get_token(),
                    username=String().gen_username(type=uname_type, length=length)
                )
            print("\n\nDone Checking Usernames")
        elif x == "2":
            usernames = String().get_user_list()
            for username in usernames:
                sleep(2.5)
                Web().check_user(token=String().get_token(), username=username)
            print("\n\nDone Checking Usernames From File")
        elif x == "3":
            exit()

    def main(self):
        self.menu()

if __name__ == "__main__":
    DcChecker().main()