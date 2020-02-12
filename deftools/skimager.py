"""
Skimager \\ Skim through images and organize on the fly
"""

# Std lib
import os
from shutil import move

# Third-party
import cv2
import numpy as np


def skimager(src_dir: str, dst_dir: str, exts: list = [".png", ".jpg", "jpeg"]):
    """
    Skims through images in a directory, taking action on them as needed.
    
    Parameters
    ----------
    src_dir : str, path, or path-like
        Source directory of images to skim through.
    dst_dir : str, path, or path-like
        Destination for good images that are not of the correct class.
    """
    # Create destination directory if needed
    os.makedirs(dst_dir, exist_ok=True)

    # Move into src directory
    os.chdir(src_dir)

    for file in os.listdir(src_dir):

        # Remove invalid file types
        file_ext = os.path.splitext(file)[-1].lower()
        if file_ext not in exts:
            print(f"{file} is '{file_ext}'. Removing...")
            os.remove(file)
        else:
            # Load image
            img = cv2.imread(file, cv2.IMREAD_UNCHANGED)

            # Show image
            cv2.imshow("preview", img)

            # Wait for and take action based on keystroke
            # "0" means wait indefinitely
            k = cv2.waitKey(0) & 0xFF
            if k == 27:  # ESC key exits entire program
                cv2.destroyAllWindows()
                break
            elif k == ord("s"):  # Image is good; do nothing
                cv2.destroyAllWindows()
            elif k == ord("m"):  # Image is good; wrong class
                move(file, dst_dir)
                cv2.destroyAllWindows()
            elif k == ord("x"):
                os.remove(file)
                cv2.destroyAllWindows()


if __name__ == "__main__":
    # Set up necessary paths
    root = "/Users/Tobias/workshop/buildbox/neurecycle/trashpanda-ds/exploration/1_image_downloading/Bing/downloads"
    clusdir = "engine_degreaser"
    dst_name = "misclasses"

    src = os.path.join(root, clusdir)
    dst = os.path.join(root, dst_name)

    skimager(src_dir=src, dst_dir=dst)
