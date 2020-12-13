movie_list = {"Superman": 250, "Avengers": 300, "Hulk": 200}
a = 1


def movie_add():
    movie = input("Enter movie name")
    while True:
        try:
            price = int(input("Enter price of the ticket"))
            break
        except:
            print("Invalid input")
    movie_list[movie] = price
    print("Movie added successfully")


def movie_view():
    print("Movies running now")
    cnt = 1
    for i in movie_list.keys():
        print(cnt, "Movie Name-", i, "\tTicket Price-", movie_list[i])
        cnt = cnt+1
        print("\n")


def movie_search():
    movie = input("Enter movie name\t")
    if movie in movie_list.keys():
        print(movie, "\navailable\n")
        return 1
    else:
        print("\nMovie not available\n")


def movie_book():
    movie = input("Enter movie name\t")
    if movie in movie_list.keys():
        total_ticket = int(input("Enter the number of tickets to be booked\t"))
        price = movie_list[movie]
        cost = (price*total_ticket)
        print("Movie booked succesfully")
        print("Amount to be paid: ", cost, "\n")
    else:
        print("\nMovie not available")


def menu():
    while True:
        print("Welcome to the home screen")
        print("Enter 1 to view movies")
        print("Enter 2 to search a mpvie")
        print("Enter 3 to add a movie")
        print("Enter 4 to book a movie")
        while True:
            try:
                choice = int(input("Enter the choice"))
                break
            except:
                print("Invalid input")
        if(choice == 1):
            movie_view()
        elif(choice == 2):
            movie_search()
        elif(choice == 3):
            movie_add()
        else:
            movie_book()
menu()
