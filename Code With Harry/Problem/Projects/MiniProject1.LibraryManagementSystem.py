# Question : https://www.youtube.com/watch?v=LH6wWxXLKQ0&list=PLu0W_9lII9agICnT8t4iYVSZ3eykIAOME&index=72

from typing import List, Mapping


class Library:
    def __init__(self, Library_Name, List_of_Books):
        self.Library_Name = Library_Name
        self.List_of_Books = List_of_Books
        self.LendDictionary = {}
    
    def DisplayBook(self):
        print("Available Books are as Follows : \n")
        for book in self.List_of_Books:
            print(book)

    def LendBook(self, user, book):
        if book not in self.LendDictionary.keys():
            self.LendDictionary.update({book:user})
            print("Lender-Book Database has been updated. You can take Book now")
        else:
            print(f"Book is already being used by {self.LendDictionary[book]}")

    def AddBook(self, book):
        List_of_Books.append(book)
        print("Book has been added to the book list")

    def ReturnBook(self, book):
        self.LendDictionary.pop(book)


if __name__ == "__main__":
    Library_Name = input("Library Name : ")
    List_of_Books = ['The Intellient Investor', 'Python Crash Course', 'Rich Dad Poor Dad', 'The Psychology of Money']
    Nikhil = Library(Library_Name, List_of_Books)
    
    while(True):
        print(f"Welcome to the {Library_Name} Library !\n")
        print("1 for Display Books")
        print("2 for Lend Book")
        print("3 for Add Book")
        print("4 for Return Book")
        choice = int(input())
        
        if choice == 1:
            Nikhil.DisplayBook()
        elif choice == 2:
            book = input("Name of Book you want to lend : ")
            user = input("Your Name : ")
            Nikhil.LendBook(user, book)
        elif choice == 3:
            book = input("Name of the book you want to add : ")
            Nikhil.AddBook(book)
        elif choice == 4:
            book = input("Name of the book you want to Return : ")
            Nikhil.ReturnBook(book)
        else:
            print("Invalid Input")

        
        print("Press 'Q' to quit and 'C' to Continue")
        choice_2 = ""
        while(choice_2!="Q" and choice_2!="C"):
            choice_2 = input()
            if choice_2 == "Q":
                exit()
            elif choice_2 == "C":
                continue