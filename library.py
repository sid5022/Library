import pandas as pd

class Book:
	def __init__(self,name,author,publisher,number):
		self.name = name
		self.author = author
		self.publisher = publisher
		self.number = number

	def detail(self):
		det = pd.DataFrame([self.name,self.author,self.publisher],
				index = ["Book","Author","Publishers"],columns = [" "])
		print(det,"\n")

class library:
	books = ["Fundamentals of Microelectronics",
		"Digital IC Design in VHDL", "IC Fabrication","OOPs in Python", 
		"Master in OOPs", "Digital VLSI Design for CMOS",
		"Microelectronics for Firmware", "CMOS VLSI Design",
		"Analog CMOS Circuits", "Basics of CMOS","OOPs in Real Life",
		"VHDL Fundamentals", "VLSI and VHDL"]
	
	authors = ["Behzad Rezavi", "Peter Frost", "Sergio Franco",
		"O'Relly", "Alexander Ameni", "B.Rezavi, M.Lorentzo",
		"Solomon", "Marsch", "Karl Hoser", "Marsch, Hoser",
		"Marco Mapelli", "Peter Farelli", "Boston"]
	
	publishers = ["Willey", "Pearson", "Springer", "Pearson",
		"Pearson", "Willey", "Elesevier", "Oxford", "Springer",
		"Willey", "Elesevier", "Oxford", "Pearson"]

	numbers = [3,3,4,3,6,3,2,2,4,4,2,3,4]
	lib = []
	for i in range(len(books)):
		lib.append(Book(books[i],authors[i],publishers[i],numbers[i]))
	
	def __init__(self,name):
		self.name = name
		self.my_books = []

	@classmethod
	def add_book(cls):
		print("Add book: ")
		new = input("Name of the book: ")
		if new not in cls.books:
			ath = input("Name of Author: ")
			pub = input("Publisher: ")
			num = int(input("How many: "))
			cls.books.append(new)
			cls.authors.append(ath)
			cls.publishers.append(pub)
			cls.numbers.append(num)
			cls.lib.append(Book(new,ath,pub,num))
		else:
			num = int(input("How many: "))
			n = cls.books.index(new)
			cls.numbers[n] += num
			for i in cls.lib:
				if cls.lib.index(i) == n:
					i.number += num

	@classmethod
	def booklist(cls):
		print("Booklist: \n")
		for j in library.lib:
			print(j.name,"\t",j.number)
		print("\n")

	@classmethod
	def search(cls):
		ab = input("'b' for Book and 'a' for Author: ")
		res = []
		if ab == 'b':
			inp = input("Name of the book: ")
			for i in cls.books:
				if inp in i:
					res.append(cls.books.index(i))
		else:
			inp = input("Name of the author: ")
			for i in cls.authors:
				if inp in i:
					res.append(cls.authors.index(i))
		if len(res) != 0:
			found = []
			avl = []
			for i in res:
				if cls.numbers[i] <= 1:
					avl.append("No")
				else:
					avl.append("Yes")
			for j in range(len(res)):
				found.append([cls.books[res[j]], cls.authors[res[j]],
					cls.publishers[res[j]], avl[j], cls.numbers[res[j]]])
			df = pd.DataFrame(found, index = [" "]*len(res),
					columns = ["Book","Author","Publisher","Availability","Left"])
			print(df,"\n")
		else:
			print("Not found!!")
		return res
	
	def lend(self):
		print("Hello "+self.name)
		print("Book Issue: ")
		if len(self.my_books) > 3:
			print("Maximum limit reached!")
		else:
			s = library.search()
			if len(s) > 0:
				n = int(input("Enter number: "))
				if library.books[s[n-1]] in self.my_books:
					print("Already issued..")
				else:
					if library.numbers[s[n-1]] > 1:
						self.my_books.append(library.books[s[n-1]])
						library.numbers[s[n-1]] -= 1
						library.lib[s[n-1]] = Book(library.books[s[n-1]],
							library.authors[s[n-1]],library.publishers[s[n-1]],
							library.numbers[s[n-1]])
						print("Book issued..")
					else:
						print("Not for lend!")
		print("My Books: ")
		for i in range(len(self.my_books)):
			print(str(i+1)+". "+self.my_books[i])
		print("\n")

	def ret(self):
		print("Hello "+self.name)
		print("Book Return: ")
		print("My Books: ")
		for i in range(len(self.my_books)):
			print(str(i+1)+". "+self.my_books[i])
		r = int(input("Enter number: "))
		k = library.books.index(self.my_books[r-1])
		library.numbers[k] += 1
		library.lib[k] = Book(library.books[k],library.authors[k],
					library.publishers[k],library.numbers[k])
		self.my_books.remove(self.my_books[r-1])
		print("My Books: ")
		for j in self.my_books:
			print(j)
		print("\n")

u1 = library("USER-1")
u2 = library("USER-2")
u3 = library("USER-3")
u1.lend()
u2.lend()
u2.lend()
u1.lend()
u3.lend()
u2.ret()
u1.ret()
library.booklist()
