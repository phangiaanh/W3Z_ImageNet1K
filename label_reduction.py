from taxanomy_map import IMAGENET_TAXONOMIC_MAPPING


import os

if __name__ == "__main__":
    if os.path.isfile("ImageNet_Label.txt"):
        os.remove("ImageNet_Label.txt")

    with open("ImageNet_Label.txt", "w") as write_file:
        with open("ImageNet_val_label.txt", "r") as file:
            for line in file:
                parts = line.strip().split()
                if parts[1] in IMAGENET_TAXONOMIC_MAPPING:
                    write_file.write(line)
