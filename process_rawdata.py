"""
A python program to parse raw_data.txt for lab4
"""
# Open file"raw_data.txt" for reading
infile = open("raw_data.txt")

# Read the first five lines of infile - Unwanted data
for i in range(1,6):
	infile.readline()
	
# Read the rest of the lines, save as lines
lines = infile.readlines()
#print(lines)
# Close infile
infile.close()

# Strip ugly spaces from the data
for i in range(0, len(lines)):
	lines[i] = lines[i].strip()

#print(lines)
authors=[]
emails=[]
authors_d={}

# Set current line num to 0
line_num=0
# While the current line number is less than the total number of lines, run this loop
while line_num<len(lines):
	# Store ID of book from current line number
	book_id = lines[line_num]
	# Update line number by 1
	line_num +=1
	# Store title of book from curret line number
	book_title = lines[line_num]
	# Update line number by 1
	line_num +=1
	#print(book_id + ' ' + book_title)
	
	# Set loop condition to True
	reading_authors=True
	# A while loop to read all authors
	while(reading_authors==True):
		# Store author name from current line number
		author_name = lines[line_num]
		# Update line number by 1
		line_num +=1
		# If there is no comma in author name
		if author_name.count(",")==0:
			# Falsify loop condition
			reading_authors=False
			#print("author is " + author_name)
		# Else (there are more authors)
		else:
			# Strip comma from name
			author_name=author_name.strip(",")
			#print("author is " + author_name)
		# If author_name is not in authors list
		if author_name not in authors:
			# Append name to authors list
			authors.append(author_name)
	# Set loop condition to True
	reading_emails=True
	# A while loop to read all emails
	while(reading_emails==True):
		# Store email from current line number
		email = lines[line_num]
		# Update line numebr by 1
		line_num +=1
		# If there is no comma in email
		if email.count(",")==0:
			# Falsify loop condition
			reading_emails=False
			#print("email is " + email)
		# Else (there are more emails)
		else:
			# Strip comma from email
			email=email.strip(",")
			#print("email is " + email)
		# If email is not in email list
		if email not in emails:
			# Append email to list
			emails.append(email)
			# Create a new key which is the email
			# The value of this key is a dictionary
			# It contains a key called books
			# Which stores all the book_id written by this author
			authors_d[email]={'books':[book_id]}
		else:
			# Next time the same email is encountered
			# append the new book_id to existing list of books
			authors_d[email]['books'].append(book_id)
	# Store isbn from current line
	isbn = lines[line_num]
	#print("isbn is " + isbn)
	# Update line number by 1
	line_num+=1
	print("Insert into books(id,title,isbn) values("+ str(book_id) + ", '" + book_title + "', " + str(isbn) + ");")
# END OF WHILE

#print(authors)
#print(emails)



# Set author_id to 1
author_id=1
# Process authors and emails list together
for i in range(0,len(authors)):
	#print(author_id,authors[i], emails[i])
	print("Insert into authors(id,author_name,e_mail) values("+str(author_id)+", '"+authors[i]+"', '" + emails[i] + "');")
	# Inside authors_d, access the emails[i] key
	# Add a new key called id and set author_id as its value
	authors_d[emails[i]]['id'] =author_id
	author_id+=1


#print(authors_d)


# Process the dictionary to help generate insert statements for bridge table
for email in authors_d.keys():
	# Store auhtor_id from id key
	author_id = authors_d[email]['id']
	# Get the list of book_ids from books key
	books = authors_d[email]['books']
	# Process the books list
	for book in books:
		print("Insert into book_authors(author_id,book_id) values("+ str(author_id) + ", "+ book + ");")
