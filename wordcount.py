def count_words_in_file(file_path):
    try:
        with open(file_path, 'r') as file:
            content = file.read()
            # Split the content into words
            words = content.split()
            # Count the words
            word_count = len(words)
            return word_count
    except FileNotFoundError:
        print(f"The file '{file_path}' does not exist.")
        return None

# File name
file_name = "sample.txt"

# Count the words in the file
word_count = count_words_in_file(file_name)

if word_count is not None:
    print(f"The file '{file_name}' contains {word_count} words.")
