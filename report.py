def sort_on(items):
    return items[1]

def print_report(path, num_words, char_dict):
    print('============ BOOKBOT ============')
    print(f'Analyzing book found at {path}...')
    print('----------- Word Count ----------')
    print(f'Found {num_words} total words')
    print('--------- Character Count -------')
    sorted_chars = sorted(char_dict.items(), key=sort_on, reverse=True)

    for key, value in sorted_chars:
        print(f'{key}: {value}')
    print('============= END ===============')