try:
    # File creation and writing
    file = open("my_file.txt", 'w')
    # Writing a mix of strings and numbers
    file.write("Hello World!\n")
    file.write("12345\n")
    file.write("PLP Python class has the best tutor!\n")
    print("File created and written successfully.")
    file.close()

    # Reading and displaying file content
    file = open("my_file.txt", 'r')
    content = file.read()
    print("\n--- File Content After Initial Write ---")
    print(content)
    file.close()

    # Appending additional lines to the file
    file = open("my_file.txt", 'a')
    file.write("Adding more content.\n")
    file.write("67890\n")
    file.write("Let's learn more about Python!\n")
    print("Content appended successfully.")
    file.close()

    # Reading and displaying updated file content
    file = open("my_file.txt", 'r')
    content = file.read()
    print("\n--- File Content After Appending ---")
    print(content)
    file.close()

except FileNotFoundError as fnf_error:
    print(f"Error: File not found. Details: {fnf_error}")
except PermissionError as perm_error:
    print(f"Error: Permission denied. Details: {perm_error}")
except Exception as error:
    print(f"An error occurred: {error}")
finally:
    print("File operation complete.")



