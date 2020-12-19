import requests  # For making http requests
import re  # For regular expressions
from bs4 import BeautifulSoup  # For pulling data out of HTML files
movie_list = {"Superman": 250, "Avengers": 300, "Hulk": 200, "Ironman": 400}
adm_psw = "password"  # please use this password for admin


class Movie:  # Class movie for movie related functions
    def __init__(self, name=0, price=0):
        self.name = name
        self.price = price

    def movie_add(self):
        self.name = input("Enter the movie you want to add: ")
        while True:
            try:
                self.price = int(input("Enter the ticket price: "))
                break
            except:
                print("Invalid input")
        if self.name not in movie_list.keys():
            movie_list[self.name] = self.price
            print("Movie added successfully\n")
        else:
            print("\nMovie already exists")

    def movie_view(self):
        print("Movies running now")
        cnt = 1
        for i in movie_list.keys():
            print(cnt, "\tMovie Name:", i, "\tPrice", movie_list[i])
            cnt = cnt+1

    def movie_search(self):
        if self.name in movie_list.keys():
            print(self.name, "is currently running\n")
            return 1
        else:
            print("\nMovie not available\n")


class Customer(Movie):  # Class customer inherits from class movie
    adm_val = 0

    def __init__(self, c_name=0):
        self.c_name = c_name
        self.ic = self.Rating()

    @classmethod  # This is a class method
    def adm_set(cls):
        cls.adm_val = 1

    @classmethod  # This is a class method
    def adm_unset(cls):
        cls.adm_val = 0

    def book_movie(self):
        cnt = 1
        for i in movie_list.keys():
            print(cnt, "\tMovie Name:", i, "\tPrice", movie_list[i])
            cnt = cnt+1
        movie = input("Choose the movie by entering the movie name: ")
        while True:
            try:
                total_ticket = int(input("Enter the total number of seats: "))
                break
            except:
                print("Invalid input")
        while True:
            if(re.match(r'[2-9]', str(total_ticket))):  # Regular expression
                break
            else:
                print("Invalid number of seats")
                while True:
                    try:
                        total_ticket = int(input("Re-enter: "))
                        break
                    except:
                        print("Invalid input")
        if movie in movie_list.keys():
            price = movie_list[movie]
            cost = (price.__mul__(total_ticket))  # using magic method mul
            if(Customer.adm_val == 1):
                print("Congrats!!!You received admin discount")
                self.c_name = input("Enter your name")
                cost = cost.__sub__(100)  # using magic method sub
            print("Movie booked succesfully")
            print("Amount to be paid: ", cost, "\n")
            dat = open("info.txt", "a")
            dat.write("Customer name: "+self.c_name+"\t")
            dat.write("Movie booked: "+movie+"\t")
            dat.write("Tickets booked: "+str(total_ticket)+"\t")
            dat.write("Total cost: "+str(cost)+"\n")
            dat.close()
        else:
            print("\nMovie not available")

    class Rating:  # Class rating is inside class customer
        def get_rating(self):
            print("To see the imdb rating")
            print("Enter 1 for Superman")
            print("Enter 2 for Avengers")
            print("Enter 3 for Hulk")
            print("Enter 4 for Ironman")
            while True:
                try:
                    opt = int(input())
                    break
                except:
                    print("Invalid input")
            if(opt == 1):
                url_imdb = "https://www.imdb.com/title/tt0078346/"
            elif(opt == 2):
                url_imdb = "https://www.imdb.com/title/tt0848228/"
            elif(opt == 3):
                url_imdb = "https://www.imdb.com/title/tt0286716/"
            elif(opt == 4):
                url_imdb = "https://www.imdb.com/title/tt0371746/"
            r = requests.get(url=url_imdb)
            soup = BeautifulSoup(r.text, 'html.parser')
            title = soup.find('title')
            print(title.string)
            ratingValue = soup.find("span", {"itemprop": "ratingValue"})
            print(ratingValue.string)


class Admin(Customer):  # Class admin inherits from Customer

    @staticmethod  # This is a static method
    def log_in():
        passwd = input("Enter the password for admin log-in")
        if(passwd == adm_psw):
            return 1
        else:
            return 0

    def view_orders(self):
        dat = open("info.txt", "r")
        print(dat.read())
        dat.close()


def menu():  # This acts as the home screen
    while True:
        print("\nWelcome to the home screen\n")
        print("Enter 1 to add a movie")
        print("Enter 2 to view all movies")
        print("Enter 3 to search a movie")
        print("Enter 4 to book tickets")
        print("Enter 5 to view bookings")
        print("Enter 6 to view movie ratings\n")
        print("Enter any other number to exit\n")
        while True:
            try:
                choice = int(input())
                break
            except:
                print("Invalid option")
        if(choice == 1):
            adm = Admin()
            if(Admin.log_in()):
                adm = Movie()
                adm.movie_add()
            else:
                print("Wrong admin password")
        elif(choice == 2):
                mov = Movie()
                mov.movie_view()
        elif(choice == 3):
            movie = input("Enter the movie you want to search: ")
            mov = Movie(movie)
            mov.movie_search()
        elif(choice == 4):
            print("Want to book movie as admin or customer")
            opt = int(input(("Enter 1 for admin\nEnter 2 for customer")))
            if(opt == 1):
                adm = Admin()
                if(Admin.log_in()):
                    Customer.adm_set()
                    adm.book_movie()
                    Customer.adm_unset()
            elif(opt == 2):
                person = input("Enter your name: ")
                cus = Customer(person)
                cus.book_movie()
        elif(choice == 5):
            adm = Admin()
            Admin.log_in()
            adm.view_orders()
        elif(choice == 6):
            cus = Customer()
            i = cus.ic
            i.get_rating()
        else:
            break
menu()
