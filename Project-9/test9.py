import re
import sys
print("Welcome to the Pattern Extractor and command-line Utility")

def extract_email(text):
    return re.findall(r'\b[\w.-]+?@\w+?\.\w+?\b',text)

def find_phone_number(text):
    return re.findall(r'\b\d{10}\b',text)

def count_word_occurrences(text,word):
    return len(re.findall(rf'\b{re.escape(word)}\b',text, re.IGNORECASE))

def replace_pattern(text,pattern,replacement):
    return re.sub(pattern,replacement,text)

def read_file(file_path):
    try:
        with open("input.txt",'r') as file:
            return file.read()
    except FileNotFoundError:
        print(f"Error file '{file_path}'not found:)")
        return None

def save_to_file(content):
    filename=input("Enter filename to save result: ")
    with open (filename,'w') as file:
        return file.write(content)
    print(f"Result saved to {filename}")

def menu_option():
    choice='y'
    while choice.lower()=='y':
        print("\nChoose an operation: ")
        print("1. Extract email addresses from text")
        print("2. Find all phone numbers matching a specific pattern")
        print("3. Count occurrences of a specific word in text")
        print("4. Replace a pattern in the text with another string")
        print("5. Load text from a file")
        print("6. Save result to a new file")
        print("7. Exit")

        option=input("choose an option(1-7): ")

        source=input("Enter text manually or type 'file' to load from file: ")
        if source.lower()=='file':
            path=input("Enter file path: ")
            text=read_file(path)
            if text is None:
                continue
        else:
            text=source

        if option=='1':
            result=extract_email(text)
            print(f"Email found: {result}")
        elif option=='2':
            result=find_phone_number(text)
            print("Phone number found: ",result)
        elif option=='3':
            word=input("Enter the word to count: ")
            result= count_word_occurrences(text,word)
            print(f"The word '{word}' occurrences {result} times.")
        elif option=='4':
            pattern =input("Enter the regex pattern to replace: ")
            replacement=input("Enter the replacement string:  ")
            result=replace_pattern(text,pattern,replacement)
            print("Modified text:\n",result)
        elif option=='5':
            read_file(input)
        elif option=='6':
            if input("Do you want to save the ouput? (y/n): ").lower()=='y':
                save_to_file(str(result))
        elif option=='7':
            print("Exiting bye byeee.....")
            break

def main():
    if len(sys.argv)>2:
        input_path=sys.argv[1]
        operation=sys.argv[2]
        text=read_file(input_path)
        if text is None:
            return
        
        if operation == "extract_email":
            print(extract_email(text))
        elif operation =="find_phone_number":
            print(find_phone_number(text))
        elif operation =="count_word":
            if len(sys.argv)<4:
                print("Error: please provide the word to count..")
            else:
                word=sys.argv[3]
                print(count_word_occurrences(text,word))
        elif operation=="replace":
            if len(sys.argv)<5:
                print("Error: please provide both pattern and replacement.")
            else:
                pattern=sys.argv[3]
                replacement=sys.argv[4]
                print(replace_pattern(text,pattern,replacement))
        else:
            print("Error: unknown operation.")
    else:
        menu_option()

if __name__=="__main__":
    main()