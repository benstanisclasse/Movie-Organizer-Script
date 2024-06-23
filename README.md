Sure! Below is a detailed explanation suitable for a GitHub README file:

---

# Movie Organizer Script

This Python script organizes movie files into a structure suitable for use with media server software like Plex. It moves movie files from a source directory to a destination directory, placing each movie into its own folder named after the movie title and year of release.

## Features

- **Automated Organization**: Moves each movie file into its own folder named in the format `MovieName (Year)`.
- **File Filtering**: Only processes movie files directly within the source directory, ignoring any files already organized in folders.
- **Change Tracking**: Reports the number of files moved after execution.

## Requirements

- Python 3.x
- Permissions to read from the source directory and write to the destination directory.

## Usage

1. **Clone the Repository**: Clone this repository to your local machine.

    ```sh
    git clone https://github.com/yourusername/movie-organizer.git
    cd movie-organizer
    ```

2. **Edit the Script**: Modify the `source_dir` and `destination_dir` variables in the script to match the paths to your movie files. Use UNC paths if accessing network locations.

    ```python
    # Directory containing your movie files
    source_dir = r'\\192.168.1.84\docker\jellyfin\Movies'
    # Directory to move and organize your movies
    destination_dir = r'\\192.168.1.84\docker\jellyfin\Movies'
    ```

3. **Run the Script**: Execute the script using Python.

    ```sh
    python organize_movies.py
    ```

## Script Explanation

### Importing Libraries

```python
import os
import shutil
import re
```

These libraries are used for interacting with the file system (`os`, `shutil`) and for matching file names using regular expressions (`re`).

### Defining Directories

```python
source_dir = r'\\192.168.1.84\docker\jellyfin\Movies'
destination_dir = r'\\192.168.1.84\docker\jellyfin\Movies'
```

Specify the source directory containing the movie files and the destination directory where organized movies will be stored. 

### Regular Expression Pattern

```python
movie_pattern = re.compile(r'^(.*) \((\d{4})\)\.(\w+)$')
```

Defines a regular expression to match movie file names in the format `MovieName (Year).ext`.

### Organize Movies Function

```python
def organize_movies(source_dir, destination_dir):
    changes_made = 0

    # Create destination directory if it doesn't exist
    if not os.path.exists(destination_dir):
        os.makedirs(destination_dir)

    for filename in os.listdir(source_dir):
        source_file_path = os.path.join(source_dir, filename)
        if os.path.isfile(source_file_path):  # Only process files, not directories
            match = movie_pattern.match(filename)
            if match:
                movie_name = match.group(1)
                movie_year = match.group(2)
                file_extension = match.group(3)
                
                # Create a new folder for the movie
                movie_folder = os.path.join(destination_dir, f'{movie_name} ({movie_year})')
                if not os.path.exists(movie_folder):
                    os.makedirs(movie_folder)
                
                # Move the movie file to the new folder
                destination_file = os.path.join(movie_folder, filename)
                shutil.move(source_file_path, destination_file)
                changes_made += 1

    return changes_made
```

- **Creating Destination Directory**: Checks if the destination directory exists, creating it if necessary.
- **Processing Files**: Iterates through files in the source directory, matching each file name against the regular expression pattern.
- **Creating Movie Folders**: Creates a new folder for each movie based on its name and year.
- **Moving Files**: Moves each matched movie file to its respective folder.
- **Tracking Changes**: Keeps a count of the number of files moved.

### Running the Function

```python
# Organize the movies and get the number of changes made
changes = organize_movies(source_dir, destination_dir)

print(f"Movies have been organized successfully. {changes} changes were made.")
```

- **Executing the Function**: Calls the `organize_movies` function with the specified directories.
- **Printing Results**: Outputs the number of changes made after organizing the movies.

## Contributing

Feel free to contribute by submitting pull requests or opening issues for any bugs or feature requests.

## License

This project is licensed under the MIT License. See the `LICENSE` file for details.

---

This README file provides a clear explanation of the script's functionality, setup, and usage instructions for potential users.
