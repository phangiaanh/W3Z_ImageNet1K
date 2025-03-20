import os
import shutil
from pathlib import Path
from taxanomy_map import IMAGENET_TAXONOMIC_MAPPING

def read_imagenet_labels(label_file_path):
    """Read ImageNet labels file and extract JPEG filenames with their values."""
    jpeg_files = {}
    try:
        with open(label_file_path, 'r') as f:
            for line in f:
                # Split line by whitespace and get the JPEG filename and value
                parts = line.strip().split()
                if len(parts) >= 2:  # Ensure line has both filename and value
                    jpeg_name = parts[0]  # First part is the JPEG filename
                    jpeg_value = parts[1]  # Second part is the value
                    jpeg_files[jpeg_name] = jpeg_value
    except FileNotFoundError:
        print(f"Error: Cannot find label file at {label_file_path}")
        exit(1)
    return jpeg_files

def filter_and_copy_images(input_dir, output_dir, target_jpegs):
    """Copy JPEG files to taxonomy-based subdirectories."""
    # Counter for copied files
    copied_count = 0
    
    # Iterate through all files in input directory
    for filename in os.listdir(input_dir):
        if filename in target_jpegs:
            # Get the class ID and find its taxonomy
            class_id = target_jpegs[filename]
            taxonomy = IMAGENET_TAXONOMIC_MAPPING.get(class_id, "unknown")
            
            # Create taxonomy-specific subdirectory
            taxonomy_dir = os.path.join(output_dir, taxonomy)
            Path(taxonomy_dir).mkdir(parents=True, exist_ok=True)
            
            # Copy the file to the appropriate taxonomy directory
            src_path = os.path.join(input_dir, filename)
            dst_path = os.path.join(taxonomy_dir, filename)
            shutil.copy2(src_path, dst_path)
            copied_count += 1
            print(f"Copied: {filename} -> {taxonomy}/{filename}")
    
    return copied_count

def main():
    # Get input from user
    input_dir = input("Enter the path to the input directory containing images: ")
    output_dir = input("Enter the path to the output directory: ")
    label_file = input("Enter the path to ImageNet_Label.txt: ")
    
    # Validate input directory
    if not os.path.isdir(input_dir):
        print(f"Error: Input directory '{input_dir}' does not exist!")
        return
    
    # Read JPEG filenames from labels file
    target_jpegs = read_imagenet_labels(label_file)
    
    # Filter and copy images
    copied_count = filter_and_copy_images(input_dir, output_dir, target_jpegs)
    
    print(f"\nProcess completed!")
    print(f"Total images copied: {copied_count}")
    print(f"Output directory: {output_dir}")

if __name__ == "__main__":
    main()
