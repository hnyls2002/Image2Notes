import argparse
import os

import easyocr
from tqdm import tqdm
from PIL import Image

from image2notes.config import IMG_EXT


def get_all_images(image_path):
    if not image_path.endswith("/"):
        image_path += "/"

    ret_list = []
    for file_name in os.listdir(image_path):
        if file_name.split(".")[-1] in IMG_EXT:
            try:
                with Image.open(image_path + file_name):
                    ret_list.append(image_path + file_name)
            except:
                pass
    return ret_list


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--image-path", type=str, default="./")
    args = parser.parse_args()

    image_list = get_all_images(args.image_path)
    reader = easyocr.Reader(["ch_sim", "en"])

    results = []
    for img_file in tqdm(image_list):
        res = reader.readtext(img_file)
        results.append(res)
        print(res)

    with open("raw_results.txt", "w") as f:
        f.write(str(results))


main()
