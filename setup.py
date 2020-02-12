"""
:: deftools \\ setup ::
"""

import os
from setuptools import setup, find_packages

# The directory containing this file
HERE = os.path.abspath(os.path.dirname(__file__))

# The text of the README file
with open(os.path.join(HERE, "README.md")) as fid:
    README = fid.read()

# List of required dependencies
REQUIRED = ["Click"]

# This call to setup() does all the work
setup(
    name="deftools",
    version="0.0.2",
    description="A set of simple tools to increase data deftness.",
    long_description=README,
    long_description_content_type="text/markdown",
    url="https://github.com/tobias-fyi/deftools",
    author="Tobias Reaper",
    author_email="tobyreaper@gmail.com",
    license="MIT",
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",
    packages=find_packages(),
    include_package_data=True,
    py_modules=["sojorn"],
    install_requires=REQUIRED,
    entry_points="""
        [console_scripts]
        sojorn=deftools.sojorn:cli
    """,
)
