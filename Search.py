import datetime
import os


def list_files_by_extension(folder_path):
    print(f"Searching in: {folder_path}")
    files = {}
    for root, _, filenames in os.walk(folder_path):
        print(f"Root: {root}")
        for filename in filenames:
            print(f"\t{filename}")
            file_path = os.path.join(root, filename)
            extension = os.path.splitext(filename)[1]
            if extension not in files:
                files[extension] = []
            files[extension].append(file_path)
    return files


def print_files_by_extension(files):
    print("Files by extension:")
    for extension, file_paths in sorted(files.items()):
        print(f"Extension: {extension}")
        for file_path in sorted(file_paths):
            parent_folder = os.path.dirname(file_path)
            print(f"\t{parent_folder}: {file_path}")
    return ""


def save_output_to_file(output, filename):
    if output is None:
        output = ""
    with open(filename, "w") as f:
        f.write(output)


if __name__ == "__main__":
    folder_path = os.path.dirname(__file__)

    files = list_files_by_extension(folder_path)

    # Check if the `files` dictionary is empty.
    if not files:
        print("No files found in the directory.")
        exit()

    # Print the output of the `print_files_by_extension()` function to the console.
    output = print_files_by_extension(files)
    print(output)

    # Save the output to a file.
    now = datetime.datetime.now()
    date_time = now.strftime("%Y-%m-%d_%H-%M-%S")
    filename = f"Search-File[{date_time}].txt"
    save_output_to_file(output, filename)
