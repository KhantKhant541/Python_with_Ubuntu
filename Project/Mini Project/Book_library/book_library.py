
book_info = []

with open("book_info.txt", "rt")as f:
    file = f.readlines()
    f.seek(0)
    for item in file:
        book_info.append(item.split(" : "))


def available_book():
    books = []
    print("Available book : ")
    for book in book_info:
        print(book[0])
        books.append(book[0])
    return books


def read():
    available_book()
    choice_book = input("Which book do you want to read? : ")
    if choice_book in available_book():
        with open(f"{choice_book}.txt", "rt")as read_f:
            print(read_f.read())
    else:
        print("Invalid book Name!")
        yes_or_no = input("Do you want to read other book? [Yes/no]")
        if yes_or_no == "yes":
            available_book()
            choice_book = input("Which book do you want to read? : ")
            if choice_book in available_book():
                with open(f"{choice_book}.txt", "rt") as read_f:
                    print(read_f.read())
        else:
            print("Have a nice day!")
            exit()


def borrow():
    borrow_book = []
    books = []
    for book in available_book():
        books.append(book)
    choice_book = input("Which one do you want to borrow? : ")
    if choice_book in books:
        name = input("Please enter your name : ")
        borrow_book.append(choice_book)
        for i in book_info:
            if i[0] == choice_book:
                book_info.remove(i)
                print(book_info)

        # with open("book_info.txt", "wt")as update_f:
        #     for i in book_info:
        #          update_f.writelines((" : ".join(i[1]))


if __name__ == '__main__':
    choice = input("What do you want to do? [Borrow, Read, Return] : ")

    if choice.lower() == "read":
        read()

    elif choice.lower() == "borrow":
        borrow()

    else:
        pass
# temp = []
#
# for item in book_info:
#     temp.append(item[1].strip("\n"))
# for i in range(len(book_info)-1):
#     book_info.pop([i][1])
# print(book_info)
# print(temp)
