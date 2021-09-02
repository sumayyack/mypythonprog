class Book:
    def set(self,library_name,book_name,author,pages):
        self.library_name=library_name
        self.book_name=book_name
        self.author=author
        self.pages=pages
    def print(self):
        print(self.library_name)
        print(self.book_name)
        print(self.author)
        print(self.pages)

bk=Book()
bk.set("abc","Alchemist","paulo coehlo",134)
bk.print()