def file_read_write_with_error_handling():
    # Ask the user for the filename
    filename = input("Enter the name of the file to read: ")

    try:
        # Attempt to open and read the file
        with open(filename, 'r') as file:
            content = file.read()
        
        # Print original content for debugging
        print(f"Original Content:\n{content}")

        # Modify the content (e.g., convert to lowercase)
        modified_content = content.lower()

        # Print modified content for debugging
        print(f"\nModified Content:\n{modified_content}")

        # Extract just the filename and add 'modified_' prefix
        import os
        base_name = os.path.basename(filename)  # Get the file name without path
        new_filename = "modified_" + base_name

        # Add .txt extension to the new file name if it's not already there
        if not new_filename.endswith(".txt"):
            new_filename += ".txt"

        # Ensure the file is saved in the same directory
        new_filename_path = os.path.join(os.path.dirname(filename), new_filename)

        # Saving modified content to the new file
        print(f"\nSaving modified content to: {new_filename_path}")
        
        with open(new_filename_path, 'w') as new_file:
            new_file.write(modified_content)

        print(f"\nModified content has been written to '{new_filename_path}'.")

    except FileNotFoundError:
        print(f"Error: The file '{filename}' was not found. Please check the file name and try again.")
    except PermissionError:
        print(f"Error: You don't have permission to read the file '{filename}'.")
    except IOError:
        print(f"Error: There was an issue reading or writing the file '{filename}'.")
    except Exception as e:
        print(f"Unexpected error: {e}")

# Run the function
file_read_write_with_error_handling()


