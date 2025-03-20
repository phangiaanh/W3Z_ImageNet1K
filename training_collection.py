PATH_DATASET = "/run/media/watermelon/fe6895ab-3146-48c7-ba28-d1d7add169ce/Datasets/ILSVRC2012_img_train"
PATH_TARGET = "/run/media/watermelon/fe6895ab-3146-48c7-ba28-d1d7add169ce/Datasets/Reduction"

TAXANOMY_DIR = ["Felidae", "Canidae", "Equidae","Bovidae", "Hippopotamidae"]

import os
import tarfile

from taxanomy_map import IMAGENET_TAXONOMIC_MAPPING

if __name__ == "__main__":

    for file in TAXANOMY_DIR:
        if os.path.exists(os.path.join(PATH_TARGET, file)):
            os.rmdir(os.path.join(PATH_TARGET, file))

    for file in TAXANOMY_DIR:
        os.mkdir(os.path.join(PATH_TARGET, file))

    for tar_file in os.listdir(PATH_DATASET):
        print(IMAGENET_TAXONOMIC_MAPPING[tar_file[:-4]])
        with tarfile.open(os.path.join(PATH_DATASET, tar_file), "r") as tar:
            tar.extractall(path=os.path.join(PATH_TARGET, IMAGENET_TAXONOMIC_MAPPING[tar_file[:-4]]))
    

    