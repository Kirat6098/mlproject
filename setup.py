from setuptools import find_packages,setup
from typing import List




def get_requirements(file_path:str)->List[str]:
    '''
    This function will return the list of requirements
    '''
    requirements=[]
    with open('requirements.txt') as file_obj:
        requirements=file_obj.readlines()
        '''
        when we read the list we get \n also so to remove that we perfom an operation to replace
        that with a blank space.
        '''
        [req.replace("\n","") for req in requirements]

        if "-e ." in requirements :
            requirements.remove("-e .")


setup(
    name='MLProject',
    version='0.0.1',
    author='Mankirat.S',
    author_email='mankirat24singh@gmail.com',
    packages=find_packages(),
    install_requires=get_requirements('requirements.txt')
)