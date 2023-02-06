def anagram(string1, string2):
	anagram = False
	string1 = string1.replace(" ", "")
	string2 = string2.replace(" ", "")
	print(string1, string2)
	if sorted(string1) == sorted(string2):
	    anagram = True
	if anagram == True:
	    print("Anagram")
	else:
	    print("Not Anagram")
