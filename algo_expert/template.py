import os
import sys


def main():
    if len(sys.argv) < 5:
        print(
            "Usage: python template.py directory_name file_name function_name arg_1 arg_2 .... arg_n"
        )
        sys.exit(1)

    # Extract arguments
    directory_name, file_name, function_name = sys.argv[1:4]
    args = sys.argv[4:]

    # Create directory if it doesn't exist
    dir_path = directory_name
    os.makedirs(dir_path, exist_ok=True)

    # Ensure the file name has a .py extension
    if not file_name.endswith(".py"):
        file_name += ".py"

    # File path
    file_path = os.path.join(dir_path, file_name)

    # Create and write to the file
    with open(file_path, "w") as file:
        # Write 6 function stubs to the file
        for i in range(
            3
        ):  # It seems there was a mistake in the comment, it should say 3 function stubs, not 6.
            # Creating the function signature
            function_signature = f"def {function_name}({', '.join(args)}):\n"
            function_body = "    pass\n\n\n"

            # Writing the stub to the file
            file.write("# Approach:\n")
            file.write("# Time: O()\n")
            file.write("# Space: O()\n")
            file.write("# n\n")
            file.write(function_signature)
            file.write(function_body)

    print(f"File '{file_name}' created successfully in '{directory_name}'.")


if __name__ == "__main__":
    main()
