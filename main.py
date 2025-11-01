import sys
from stats import count_words, char_count
from report import print_report

# with open('/books/frankenstein.txt') as file:
#     content = file.read()

def get_book_text(path):
    with open(path, encoding='utf-8') as file:
        return file.read()

def main():
	if len(sys.argv) < 2:
		print("Usage: python3 main.py <path_to_book>")
		sys.exit(1)
	else:
		path_to_book = sys.argv[1]	
		content = get_book_text(path_to_book)
		num_words = count_words(content)    
		char_dict = char_count(content)
		print_report(path_to_book,num_words,char_dict)

main()