"""Walks through a directory tree and counts the leaves."""

import os
import shutil
from collections import Counter
from pprint import pprint


def walka(root_dir: str, exts: list = None, contains: list = None):
    """
    Walks through a directory tree and counts the leaves.
    TODO: count the different types of leaves.
    
    Parameters
    ----------
    root_dir : str, path, or path-like, optional
        Root directory, by default os.getcwd()
    exts : list, optional
        List of file extensions to count, by default None
    contains : list, optional
        Keywords to use as filter or to count, by default None
    
    Returns
    -------
    [type]
        [description]
    """

    # Instantiate file extension counter
    if exts:
        # Only count extensions in ext list
        ext_counter = Counter(exts)
    else:
        # Count all extensions in tree
        ext_counter = Counter()

    counter = 1
    for root, dirnames, filenames in os.walk(root_dir):
        for file in filenames:
            counter += 1

            ext = os.path.splitext(file)[-1].lower()
            ext_counter[ext] += 1

            print(shutil.disk_usage(file))

    # TODO: Prompt to remove non-valid files

    print("Total files:", counter)
    print("Extensions:")
    pprint(ext_counter.most_common())
    # for extension in ext_counter:
    #     print(f"{extension}: {ext_counter[extension]}")

    return counter


if __name__ == "__main__":
    walka("downloads/")
