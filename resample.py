import os
import random
import shutil
from pathlib import Path

def resample_directory(input_dir, percentage=0.1):
    """Randomly sample percentage of files from Canidae directory."""
    canidae_dir = os.path.join(input_dir, 'Canidae')
    
    if not os.path.exists(canidae_dir):
        print(f"Error: Canidae directory not found in {input_dir}")
        return
    
    # Get all files in Canidae directory
    files = os.listdir(canidae_dir)
    num_files = len(files)
    num_to_keep = int(num_files * percentage)
    
    # Randomly select files to keep
    files_to_keep = random.sample(files, num_to_keep)
    
    # Remove files not in the sample
    for file in files:
        if file not in files_to_keep:
            file_path = os.path.join(canidae_dir, file)
            os.remove(file_path)
    
    print(f"Resampled Canidae: Kept {num_to_keep} out of {num_files} files")

if __name__ == "__main__":
    input_dir = input("Enter the path to the parent directory: ")
    resample_directory(input_dir)
    