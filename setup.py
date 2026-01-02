from setuptools import find_packages,setup
from typing import List

DASH_E_DOT = "-e."
def get_requirements(file_path:str)->list[str]:

   requirements=[]
   with open(file_path) as file_obj:
        requirements = file_obj.readlines()
        [req.replace('/n',"") for req in requirements]

        if DASH_E_DOT in requirements:
            requirements.remove(DASH_E_DOT)
       
   return requirements


setup(
    name="student performance analysis + prediction",
    version = "0.0.1",
    author= "shivang devina",
    author_email="shivangdevinaiitkgp@gmail.com",
    packages=find_packages(),
    install_requires= get_requirements("requirements.txt"),
)