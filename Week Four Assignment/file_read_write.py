def modify_content(content):
    # Modify the content as needed (example: convert to uppercase)
    return content.upper()  # You can change this logic to something else

try:
    # Ask the user to enter the filename
    input_filename = input("Enter the filename to read from: ")

    # Open and read the content of the file
    with open(input_filename, 'r') as file:
        content = file.read()

    # Modify the content
    modified_content = modify_content(content)

    # Define the output filename
    output_filename = "modified_" + input_filename

    # Write the modified content to a new file
    with open(output_filename, 'w') as file:
        file.write(modified_content)

    print(f"Modified content successfully written to '{output_filename}'.")

except FileNotFoundError:
    print("Error: The file you entered does not exist.")
except IOError:
    print("Error: The file could not be read or written.")
except Exception as e:
    print(f"An unexpected error occurred: {e}")

