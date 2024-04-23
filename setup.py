from setuptools import find_packages, setup
from typing import List

hd='-e .'
def get_requirements(file_path:str)->List[str]:
    '''
    this function will return the list of requirement
    '''
    requirements=[]
    with open(file_path) as file_obj:
        requirements=file_obj.readlines()
        requirements=[req.replace("\n","") for req in requirements]
        
        if hd in requirements:
            requirements.remove(hd)
    return requirements
setup(name="mlproject",
version="0001",
author="kajal",
author_email = "goodwish22@gmail.com",
packages=find_packages(),
install_requires=get_requirements('requirements.txt')
)