import os
#Creating a file named script.txt
file_name = "script.txt"
#reading contents from the script.txt file
try:
    file = open(file_name,'r');
    content = file.read();
    print(content);
except FileNotFoundError:
    print(f"Error: File '{file_name}' not found.")
    exit()
except PermissionError:
    print(f"Error: Permission denied for file '{file_name}'.")
    exit()
except Exception as e:
    print(f"Error: {e}")
    exit()

#counting words
def count_words(text):
    words = text.split()
    return len(words)
#counting lines
def count_lines(text):
    lines = text.split('\n')
    return len(lines)
#couting characters
def count_characters(text):
    return len(text)
# Function to replace words
def replace_words(text, old_word, new_word):
    modified_text = text.replace(old_word, new_word)
    return modified_text
# Function to create a backup of the original file so that if modified information using write function,I would keep this as a backup!
def create_backup(file_name, content):
    backup_file_name = file_name + ".bak"
    try:
        with open(backup_file_name, 'w') as backup_file:
            backup_file.write(content)
        print(f"Backup created: {backup_file_name}")
    except Exception as e:
        print(f"Error creating backup: {e}")
def main():
    
    content = file
    
if content:
        print(f"The script contains {count_words(content)} words, {count_lines(content)} lines, and {count_characters(content)} characters!")
else:
     print("The script is empty!");
#user input for replacing the text content!
old_word = input("Enter the word to replace: ")
new_word = input("Enter the new word: ")
modified_content = replace_words(content, old_word, new_word)
print(modified_content);
    # Write modified content back to file
try:
    with open(file_name, 'w') as file:
        file.write(modified_content)
        print("Modified content written back to the file successfully.")
except Exception as e:
        print(f"Error: {e}")
# Create a backup of the original file
create_backup(file_name, content);
# Calling main function
if __name__ == "__main__":
    main()
