def process_file():
    """
    Reads a file, processes its content, and writes to a new file with error handling.
    """
    try:
        # Get filename from user
        filename = input("Enter the filename to process (e.g., input.txt): ").strip()
        
        # Read the file
        with open(filename, 'r') as input_file:
            content = input_file.read()
        
        # Process the content 
        processed_content = content.upper()
        word_count = len(processed_content.split())
        
        # Create output filename
        output_filename = f"processed_{filename}"
        
        # Write to new file
        with open(output_filename, 'w') as output_file:
            output_file.write(f"Word count: {word_count}\n\n")
            output_file.write(processed_content)
        
        print(f"\n✅ Success! Processed file saved as '{output_filename}'")
        print(f"📝 Word count: {word_count}")
    
    except FileNotFoundError:
        print(f"\n❌ Error: The file '{filename}' was not found.")
    except PermissionError:
        print(f"\n❌ Error: Permission denied when accessing '{filename}'.")
    except UnicodeDecodeError:
        print(f"\n❌ Error: Could not decode the file '{filename}'. Is it a text file?")
    except Exception as e:
        print(f"\n❌ An unexpected error occurred: {str(e)}")
    finally:
        print("\nOperation completed.")


if __name__ == "__main__":
    print("📂 File Processing Program 📂")
    print("---------------------------")
    process_file()