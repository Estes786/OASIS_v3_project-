# GitHub Repository Zipper

This script allows you to create a zip archive of your GitHub repository, automatically excluding the `.github/workflows` directory and `.git` related files.

## Usage

1.  **Place the script:** Save the `zip_repo.sh` script in the root directory of your GitHub repository.

2.  **Make it executable:** Open your terminal or command prompt, navigate to your repository's root directory, and run:
    ```bash
    chmod +x zip_repo.sh
    ```

3.  **Run the script:** Execute the script from the root of your repository:
    ```bash
    ./zip_repo.sh
    ```

    This will create a file named `repo_archive.zip` in the same directory, containing all files and folders from your repository, except for the `.github/workflows` directory and `.git` related files.

## Customization

You can modify the `zip_repo.sh` script to change the output zip file name or the directory to exclude:

-   `OUTPUT_ZIP`: Change `repo_archive.zip` to your desired output file name.
-   `EXCLUDE_DIR`: Change `.github/workflows` to any other directory you wish to exclude.

## Requirements

-   `zip` utility: This script relies on the `zip` command-line utility. Most Linux and macOS systems have it pre-installed. For Windows, you might need to install a tool like Git Bash or Cygwin that includes `zip`.


