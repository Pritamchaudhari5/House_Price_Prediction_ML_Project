from setuptools import setup,find_packages
from typing import List


#Declaring variables for setup function
PROJECT_NAME="housing-predictor"
VERSION="0.0.2"
AUTHOR="Pritam Chaudhari"
DESCRIPTION="This is the first machine learning project"
REQUIREMENTS_FILE_NAME="requirements.txt"

def get_requirements_list()->List[str]:
    """
    Description: This function is going to return list of requirement
    mention is reqirements.txt file

    return this fuction is going to return a list which contain name
    of libraries mentioned in requirements.txt file
    """
    with open(REQUIREMENTS_FILE_NAME) as requirement_file:
        return requirement_file.readlines().remove("-e .")
 
setup(
name=PROJECT_NAME,
version=VERSION,
author=AUTHOR,
description=DESCRIPTION,
packages=find_packages(),
inatall_requires=get_requirements_list()

)
