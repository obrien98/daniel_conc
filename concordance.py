
def most_frequent_word(concordance):
	# prints the word that occurs most frequently
	num_references = 0
	for k, v in concordance.items():
		if len(v) > num_references:
			most_frequent_word = k
			num_references = len(v)
	print(f"The most frequent word is '{most_frequent_word}' with {num_references} references")


def longest_word(concordance):
	#prints the word with the longest length
	longest_word = ''
	for key in concordance:
		if len(key) > len(longest_word):
			longest_word = key
	print(f"The longest word is '{longest_word}' with {len(longest_word)} letters")




def num_words_in_concordance(concordance):
	# print number of words in concordance
	print(f'There are {len(concordance.keys())} in the concordance')

def display_concordance(concordance):
	# output entire concordance
	print(concordance)

def concordance_keys(concordance):
	# print only the keys
	for key in concordance.keys():
		print(key, end = ' ')
	print()

def all_instances_of_word(concordance):
	word = input('Enter word to lookup: ')
	word = word.lower()
	if word in concordance:
		print(f'The citations for {word} is {concordance[word]}')
	else:
		print(f'{word} not in concordance')

def words_starting_with_letter(concordance, letter):
	# all words starting with letter
	letter = letter.lower()
	words = []
	for word in concordance:
		if word[0] == letter:
			words.append(word)
	if words:
		print(f"Words starting with '{letter}' are ", end = '')
		for word in words:
			print(word, end = ' ')
		print() # newline
	else:
		print(f"There are no words starting with '{letter}'")

def menu():
	print("""
	Enter one of the following command letters
		L prints the longest word
		M prints the most frequent word
		C prints the complete concordance
		N prints the number of words in the concordance
		K prints only the words, i.e. keys
		W prompts for a word and prints all list of <line#, word#>
		a and other lower case letters, prints all words start with that letter
		D print the directions
		Q exit and stop accepting commands
	""")





def main():
    concordance = {}
    line = ''
    line_num = 1
    word_num = 1
    excluded_words = ['are', 'and', 'but', 'from', 'that', 'the', 'this']
    file_name = input('Enter file name: ')
    with open(file_name, 'r') as file:
    	for original_line in file:
    		# create new line of text
    		line = ''
    		word_num = 1 # num words in this line
    		for char in original_line:
    			if char == '.' or char == ',' or char == ',' or char == ':' or char == '-' or char == ';' or char == '!' or char == '"' or char == "'":
    				# replace designated characters with spaces
    				char = ' '
    			line += char # add to line var
    		for word in line.split():
    			word = word.lower()
    			if word in excluded_words or len(word) <=2:
    				word_num += 1 # increment word count
    				continue
    			else:
    				if word in concordance:
    					concordance[word].append( (line_num, word_num) )
    				else:
    					concordance[word] = [(line_num, word_num)]
    				word_num += 1 # increment word count
    		line_num += 1 # increment line count


    concordance = dict(sorted(concordance.items())) # given by professor
    menu()
    user_input = ''
    while user_input != 'Q':
        user_input = input('Enter command letter: ')
        if user_input == 'D': # print menu
        	menu()
        elif user_input == 'L':  # longest word
        	longest_word(concordance)
        elif user_input == 'M': # most frequent word
        	most_frequent_word(concordance)
        elif user_input == 'C': # whole concordance
        	display_concordance(concordance)
        elif user_input == 'N': # num words
        	num_words_in_concordance(concordance)
        elif user_input == 'K': # only the keys
        	concordance_keys(concordance)
        elif user_input == 'W': # instances of specific word
        	all_instances_of_word(concordance)
        elif len(user_input) == 1 and user_input.islower(): # words that start with specific letter
        	words_starting_with_letter(concordance, user_input)
        elif (len(user_input) > 1):
        	print(f"{user_input} is not a single command letter")
        elif (user_input == 'Q'):
            print('concordance.py terminating')
        else:
        	print(f'{user_input} is an invalid command')

main()

