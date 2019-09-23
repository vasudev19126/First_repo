def sm(s):
	x=s.find("(")
	print(x)
	word1=s[:x].upper()
	y=s.find(")")
	print(y)
	word2=s[x+1:y]
	word2=word2[::-1]
	print(word2)
	size3=str(len(s[y+1:len(s)]))
	return "#"+size3+"\""+word2+"\""+word1+"#"

y=sm("ican(see)you?")
print(y)	
