num_dict = {'a':184,
'b':167,
'c':244,
'd':134,
'e':98,
'f':107,
'g':99,
'h':117,
'i':94,
'j':31,
'k':39,
'l':98,
'm':157,
'n':85,
'o':72,
'p':213,
'q':14,
'r':113,
's':278,
't':136,
'u':60,
'v':43,
'w':69,
'x':5,
'y':11,
'z':11}
urls = []
url = "http://www.dictionary.com/list/"
for key, value in num_dict.items():
	for i in range(1, value + 1):
		urls.append(url + key + "/" + str(i))
print urls