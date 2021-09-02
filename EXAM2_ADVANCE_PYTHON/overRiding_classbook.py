class Book:
    def printv(self,book_name,author):
        self.book_name=book_name
        self.author=author
        print(self.book_name,self.author)
class Novel(Book):
    def printv(self,pages,chapters):
        self.pages=pages
        self.chapters=chapters
        print("numbers of pages",self.pages)
        print("number of chapters",self.chapters)

nl=Novel()
nl.printv(134, 30)
