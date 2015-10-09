# Piggetty.py 
# Cynthia Carter
# IWU Fall 2015 CS 125
# A program that converts the text to pig latin

# Define a function called piggy(string) that returns a string
def piggy(word):
	n = 0
	vowels = "aeiouAEIOU"
	endword = ""
	for letter in word:
		# Check if letter is a vowel
		if letter in vowels:
			# True?  We are done
			if n == 0:
				pig = word + "yay"
			break
		else:
			endword += word[n]
			pig = word[n+1:] + endword + "ay"
		n += 1
	
	return pig

# Open the file *getty.txt* for reading.  
gettyfile = open ("getty.txt","r")

# Open a new file *piggy.txt* for writing.  
Pmy_file = open ("piggy.txt","w")

# Read the getty.txt file into a string. 
gettystr = gettyfile.read()

# Strip out bad characters (, - .).  
gettystr = gettystr.replace ('.', '')
gettystr = gettystr.replace (',', '')
gettystr = gettystr.replace ('-','')

# Split the string into a list of words.  
gettylist = gettystr.split()

# Create a new empty string.  
newstr = ""

# Loop through the list of words, pigifying each one.  
for word in gettylist:
	newword = piggy(word)
	newstr = newstr + newword + " "
	
outfile = open("piggy.txt","w")
print (newstr, gettylist, file=outfile)
outfile.close()
gettyfile.close()

# Write the new string to piggy.txt. 

# close the files.