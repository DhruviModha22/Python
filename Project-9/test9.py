import re
import sys

print("Welcome to the Pattern Extractor and Command-Line Utility")

def extract_email(text):
    return re.findall(r'\b[\w\.-]+?@\w+?\.\w+?\b', text)

def find_phone_number(text, pattern=r'\d{3}-\d{3}-\d{4}'):
    return re.findall(pattern, text)

def count_word_occurrences(text, word):
    return len(re.findall(rf'\b{re.escape(word)}\b', text, re.IGNORECASE))

def replace_pattern(text, pattern, replacement):
    return re.sub(pattern, replacement, text)

def read_file(file_path):
    try:
        with open(file_path, 'r') as file:
            return file.read()
    except FileNotFoundError:
        print(f"Error: file '{file_path}' not found.")
        return None

def save_to_file(content):
    filename = input("Enter filename to save result: ")
    try:
        with open(filename, 'w') as file:
            file.write(content)
        print(f"Result saved to {filename}")
    except Exception as e:
        print("Error saving file:", e)

def menu_option():
    text = ""
    result = ""
    while True:
        print("\nChoose an operation:")
        print("1. Extract email addresses from text")
        print("2. Find all phone numbers matching a specific pattern")
        print("3. Count occurrences of a specific word in text")
        print("4. Replace a pattern in the text with another string")
        print("5. Load text from a file")
        print("6. Save result to a new file")
        print("7. Exit")

        option = input("Choose an option (1-7): ")

        if option in ['1', '2', '3', '4']:
            input_mode = input("Enter 'file' to load text from file or press Enter to enter manually: ")
            if input_mode.lower() == 'file':
                path = input("Enter file path: ")
                text = read_file(path)
                if text is None:
                    continue
        else:
            text = input("Enter the text to process:\n")


        if option == '1':
            result = extract_email(text)
            print("Email(s) found:")
            for email in result:
                print(email)

        elif option == '2':
            pattern = input("Enter the phone number pattern (e.g., \\d{3}-\\d{3}-\\d{4}): ")
            result = find_phone_number(text, pattern)
            print("Phone number(s) found:")
            for number in result:
                print(number)

        elif option == '3':
            word = input("Enter the word to count: ")
            result = count_word_occurrences(text, word)
            print(f"The word '{word}' occurs {result} times.")

        elif option == '4':
            pattern = input("Enter the regex pattern to replace: ")
            replacement = input("Enter the replacement string: ")
            result = replace_pattern(text, pattern, replacement)
            print("Modified text:\n", result)

        elif option == '5':
            path = input("Enter file path to load: ")
            text = read_file(path)
            if text:
                print("Text loaded successfully.")

        elif option == '6':
            if result:
                save_to_file(str(result))
            else:
                print("No result to save. Perform an operation first.")

        elif option == '7':
            print("Exiting... Bye bye!")
            break

        else:
            print("Invalid option. Please choose from 1 to 7.")

def main():
    if len(sys.argv) > 2:
        input_path = sys.argv[1]
        operation = sys.argv[2]
        text = read_file(input_path)
        if text is None:
            return

        if operation == "extract_email":
            print("Extracting emails:")
            print("\n".join(extract_email(text)))

        elif operation == "find_phone_number":
            if len(sys.argv) < 4:
                print("Error: Please provide the phone number pattern.")
            else:
                pattern = sys.argv[3]
                print("Phone numbers found:")
                print("\n".join(find_phone_number(text, pattern)))

        elif operation == "count_word":
            if len(sys.argv) < 4:
                print("Error: Please provide the word to count.")
            else:
                word = sys.argv[3]
                print(f"The word '{word}' appears {count_word_occurrences(text, word)} times.")

        elif operation == "replace":
            if len(sys.argv) < 5:
                print("Error: Please provide both pattern and replacement string.")
            else:
                pattern = sys.argv[3]
                replacement = sys.argv[4]
                print("Modified text:\n", replace_pattern(text, pattern, replacement))

        else:
            print("Error: Unknown operation.")

    else:
        menu_option()

if __name__ == "__main__":
    main()
