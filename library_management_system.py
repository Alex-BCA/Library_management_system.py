books=[]
issued_books=[]
while True:
    print("***Library management system***")
    print("1.Add book")
    print("2.View book")
    print("3.Search book")
    print("4.Issue book")
    print("5.Return book")
    print("6.Delete book")
    print("7.Count book")
    print("8.Exit")

    choice=input("Enter your choice:")
    if choice=="1":
        print("Add book")
        book=input("Enter book name:")
        books.append(book)
    elif chooice=="2":
        print("View book:")
        for i in range(len(books)):
            print(i+1,".",books[i])
    elif choice=="3":
        print("Search book:")
        book=input("Enter searching book name:")
        if book in books:
            print("Book found!")
        else:
            print("Do not found!")
    elif choice=="4":
        print("Issue book:")
        book=input("Enter issued book name:")
        if book in books:
            books.remove(book)
            issued_books.append(book)
            print("Book issued successfully!")
        else:
            print("Book not  found!")
    elif choice=="5":
        print("Return book:")
        book=input("Enter return book:")
        if book in issued_books:
            issued_books.remove(book)
            books.append(book)
            print("Book returned successfilly!")
        else:
            print("Book not found in issued books!")
    elif choice=="6":
        print("Delete book:")
        book=input("Enter deleting book name:")
        if book in books:
            books.remove(book)
            print("Book removed successfully!")
        else:
            print("Book not found!")
    elif choice=="7":
        print("Count:")
        print("Total books =",len(books)+len(issued_books))
    elif choice=="8":
        print("Thank you!")
        break
    else:
        print("In-valid syntax")
