"""search query term in the dictionary
	testing left corner case 1.caps lock check  2.same word multiple times in list
	working file
	increase scope  can create index """
D={}
D1={}
L=[]
fp=open("index_file.txt","r")

def filenames_list():

	global L
	for filenames in fp:
		L.append(filenames)
	#print(L)

def group_words():
	

	for filename in L:
		D={}
		s=filename.replace("\n","")
		fp=open(s,"r")
		for line in fp:
			#print(filename)
			for w in line.split():
				if w[0] in D:
					if w not in D[w[0]]:
						D[w[0]].append(w)
				else:
					D[w[0]] = [w]

		D1[filename]=D
	#print(D1)

def search_query():

	global user_search
	user_search=input("Enter the word to be searched    ")
	return user_search

def search_word():

	for filename in L:
		if user_search[0] in D1[filename]:
			if user_search in D1[filename][user_search[0]]:
				print(filename)
		

filenames_list()
group_words()
search_query()
search_word()
	

	




