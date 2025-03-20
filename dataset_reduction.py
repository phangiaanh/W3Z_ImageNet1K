from taxanomy_map import IMAGENET_TAXONOMIC_MAPPING

PATH_DATASET = "/run/media/watermelon/fe6895ab-3146-48c7-ba28-d1d7add169ce/Datasets/ILSVRC2012_img_train"


import os

if __name__ == "__main__":

    for tar_file in os.listdir(PATH_DATASET):
        if  tar_file[:-4] not in IMAGENET_TAXONOMIC_MAPPING:
            os.remove(os.path.join(PATH_DATASET, tar_file))