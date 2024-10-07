# file_handling_assignment.py

def create_file():
    try:
        # File Creation and Writing
        with open("my_file.txt", "w") as file:
            file.write("Hello, this is line 1.\n")
            file.write("This is line 2 with a number: 42.\n")
            file.write("Final line before appending.\n")
        print("File created and initial content written successfully.")
    except Exception as e:
        print(f"An error occurred while creating or writing the file: {e}")
    finally:
        print("Finished file creation process.")


def read_file():
    try:
        # File Reading and Displaying
        with open("my_file.txt", "r") as file:
            content = file.read()
            print("Reading file content:")
            print(content)
    except FileNotFoundError:
        print("Error: The file does not exist.")
    except Exception as e:
        print(f"An error occurred while reading the file: {e}")
    finally:
        print("Finished reading process.")


def append_file():
    try:
        # File Appending
        with open("my_file.txt", "a") as file:
            file.write("Appending line 1.\n")
            file.write("Appending line 2 with another number: 99.\n")
            file.write("Final appended line.\n")
        print("Content appended to the file successfully.")
    except Exception as e:
        print(f"An error occurred while appending to the file: {e}")
    finally:
        print("Finished appending process.")


if __name__ == "__main__":
    # Step 1: Create and write to the file
    create_file()
    
    # Step 2: Read and display file content
    read_file()
    
    # Step 3: Append additional content to the file
    append_file()

    # Step 4: Read and display the updated file content
    read_file()
