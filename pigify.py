# 
# File Header
#
# Define vowels

vowels = "aeiouAEIOU"

# Ask for word

n = 0


word = input("Please enter a word: ")

# Loop through word, one letter at a time

for letter in word:
# Check if letter is a vowel
	if letter in vowels:
		# True?  We are done
		if n == 0:
			pig = word + "yay"
	else:
		pig = word[n:] + endword + "ay"
		# False? Consonant
		endword += word[n]
		n += 1
		

print(word)
