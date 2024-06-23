import os
import shutil
import re

# Directory containing your movie files
source_dir = r'\\192.168.1.84\docker\jellyfin\Movies'
# Directory to move and organize your movies
destination_dir = r'\\192.168.1.84\docker\jellyfin\Movies'

# Regular expression to match movie files (assuming format MovieName (Year).ext)
movie_pattern = re.compile(r'^(.*) \((\d{4})\)\.(\w+)$')

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

# Organize the movies and get the number of changes made
changes = organize_movies(source_dir, destination_dir)

print(f"Movies have been organized successfully. {changes} changes were made.")
