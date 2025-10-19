#1
# def file_read():
#     file=open('python.txt','r')
#     for each in file:
#      print(each)
# file_read()
#2



# file=open('python.txt','r')
# print("using read() mode character wise:")
# s1=file.read(19)
# print(s1)

# f1=open("jj",)
# f1.write("something")

# def main():
#     # Open file for output (ensure the file path is valid)
#     outfile = open(r'C:\Users\FATTANI COMPUTERS\OneDrive\Documents\labortories-python-all\python.txt', 'w')

#     # Write data to the file
#     outfile.write("Bill Clinton\n")
#     outfile.write("George Bush\n")
#     outfile.write("Barack Obama")

#     print("Data has been written to the file.")

#     # Close the output file
#     outfile.close()

# # Call the main function
# main()


# def main():
# # Open file for output
#     outfile=open('C:\Users\FATTANI COMPUTERS\OneDrive\Documents\labortories-python-all\python1.txt','x')
# # Write data to the file
#     outfile.write("var, account_balance, client_name")
#     outfile.write("var = 1\n account_balance = 1000.0\nclient_name = 'John Doe'") 
#     print(outfile)
#     # Close the output file
#     outfile.close()  
# main()

# def main():
#     try:
#         # Open file for output using 'x' mode (create file, fail if exists)
#         outfile = open(r'C:\Users\FATTANI COMPUTERS\OneDrive\Documents\labortories-python-all\python1.txt', 'x')

#         # Write data to the file
#         outfile.write("var, account_balance, client_name\n")
#         outfile.write("var = 1\naccount_balance = 1000.0\nclient_name = 'John Doe'")

#         print("Data has been written to the file.")

#         # Close the output file
#         outfile.close()
#     except FileExistsError:
#         print("Error: The file already exists. Choose a different name or location.")

# # Call the main function
# main()


# def file_read(file_path):
#     """
#     Reads the entire content of a text file and prints it.
#     :param file_path: The path to the file to be read
#     """
#     try:
#         with open(file_path, 'r') as file:
#             content = file.read()
#             print("File Content:")
#             print(content)
#     except FileNotFoundError:
#         print("Error: The file was not found.")
#     except Exception as e:
#         print(f"An error occurred: {e}")


# file_path = r'C:\Users\FATTANI COMPUTERS\OneDrive\Documents\labortories-python-all\python1.txt'  # 
# file_read(file_path)

# 2. Write a program that reads the content and replace any word in a string with different word.
# Example: 
# Replace ‘dog’ with ‘cat’in  a sentence


# def replace_word_in_file(file_path, target_word, replacement_word):
#     """
#     Reads a file, replaces a word with another word, and prints the modified content.
#     :param file_path: Path to the input file
#     :param target_word: The word to replace
#     :param replacement_word: The word to replace it with
#     """
#     try:
#         # Read the file content
#         with open(file_path, 'r') as file:
#             content = file.read()

#         # Replace the target word
#         modified_content = content.replace(target_word, replacement_word)

#         # Print the modified content
#         print("Modified Content:")
#         print(modified_content)

#         # Optionally save changes back to the file
#         with open(file_path, 'w') as file:
#             file.write(modified_content)
#             print(f"The file has been updated with the new content.")
#     except FileNotFoundError:
#         print("Error: File not found.")
#     except Exception as e:
#         print(f"An error occurred: {e}")

# # Example usage
# file_path = r'C:\path\to\your\file.txt'  # Replace with your file path
# replace_word_in_file(file_path, 'dog', 'cat')



# def replace_word_in_file(file_path, target_word, replacement_word):
#     try:
#         with open(file_path, 'r') as file:
#             content = file.read()

#         modified_content = content.replace(target_word, replacement_word)

#         print("Modified Content:")
#         print(modified_content)

#         with open(file_path, 'w') as file:
#             file.write(modified_content)
#             print(f"The file has been updated with the new content.")
#     except FileNotFoundError:
#         print("Error: File not found.")
#     except Exception as e:
#         print(f"An error occurred: {e}")

# file_path = r'C:\Users\FATTANI COMPUTERS\OneDrive\Documents\labortories-python-all\python.txt' 
# replace_word_in_file(file_path, 'cat', 'dog')


def write_name_to_file():
    try:
        # Prompt the user for their name
        name = input("Enter your name: ")
        
        # Write the name to guest.txt
        with open("guest.txt", "w") as file:
            file.write(name)
        
        print(f"Your name has been written to 'guest.txt'.")
    except Exception as e:
        print(f"An error occurred: {e}")

write_name_to_file()
