from setuptools import find_packages, setup
from typing import List




def get_requirements(file_path: str) -> List[str]:
    '''
    This function will return the list of requirements
    '''
    requirements = []
    
    with open(file_path) as file_obi:
        requirements = file_obi.readline()
        requirements = [req.replace('\n', "") for req in requirements]


           
        
    return requirements




setup(
name='MLPROHECT',
version='0.01',
author='vrushali',
author_email='vrushalip037@gmail.com',
packages=find_packages(),
install_requires=get_requirements('requirements.txt'))