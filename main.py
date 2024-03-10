class Library:
    def __init__(self):
        self.noofbooks = 0
        self.books = []
        self.borrowerdic = {}

    def check(self):
        if len(self.books) == self.noofbooks:
            print("All good, you can save them ^^")
            return True
        else:
            print('Problem occurred as the number of books does not match the length of the array')
            return False

    def remove_book(self, bookname):
        if bookname in self.books:
            self.books.remove(bookname)
            self.noofbooks -= 1
            return f"Removed {bookname} from the library."
        else:
            return f"{bookname} is not in the library."

    def add_books(self):
        while True:
            try:
                z = int(input('Enter the number of books to add: '))
                break
            except ValueError:
                print("Please enter a valid integer.")

        for _ in range(z):
            bookname = input('Enter book name: ')
            self.noofbooks += 1
            self.books.append(bookname)
        return f'Updated Books in library: {self.books}. Contains {self.noofbooks} books.'

    def search_book(self, bookname):
        if bookname in self.books:
            return f'{bookname} is in the library ^^'
        else:
            return f'{bookname} is not in the library -_-'

    def borrower(self, noofbooksborrowed):
        for i in range(noofbooksborrowed):
            bookname = input('Enter the book name: ')
            name = input(f'{bookname} is issued by: ')
            temp = {'name': name, 'bookname': bookname}
            self.borrowerdic[len(self.borrowerdic)] = temp

    def show_borrowers(self):
        if self.borrowerdic:
            for i in self.borrowerdic:
                print(i, 'borrowed', self.borrowerdic[i]['bookname'], 'issued by', self.borrowerdic[i]['name'])
        else:
            print("No borrowers in the record.")


def main():
    print('Welcome to the New Library ^^')
    a = Library()
    print(f'Currently, there are {a.noofbooks} books in the library.')
    
    while True:
        n = input('What do you want to do now (add books/remove books/check list/search/show borrowers list/ borrower/exit): ')
        if 'add' in n:
            print(a.add_books())
        elif 'remove' in n:
            book = input('Enter the book you want to remove from the shelf: ')
            print(a.remove_book(book))
        elif 'search' in n:
            book = input('Enter the book you want to search: ')
            print(a.search_book(book))
        elif 'show borrowers' in n:
            a.show_borrowers()
        elif 'borrower' in n:
            noofbooksborrowed = int(input("Enter the number of books borrowed: "))
            a.borrower(noofbooksborrowed)
            print('Added borrowers.')
        elif 'exit' in n:
            break

if __name__ == '__main__':
    main()
