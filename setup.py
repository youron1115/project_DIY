from setuptools import find_packages,setup
from typing import List
import os

HYPEN_E_DOT='-e .'
def get_requirements(file_path:str)->List[str]:
    '''
    this function will return the list of requirements
    '''
    requirements=[]
    with open(file_path) as file_obj:
        requirements=file_obj.readlines()
        requirements=[req.replace("\n","") for req in requirements]

        if HYPEN_E_DOT in requirements:
            requirements.remove(HYPEN_E_DOT)
    
    return requirements

install_requires_path=str(os.path.abspath(__file__)).split("\\")[:-1]#這樣就去掉檔案名稱剩路徑
install_requires_path="\\".join(install_requires_path)+"\\"+"requirements.txt"

setup(
#name='firstproject',
#version='0.0.1',
#author='the author',
#author_email='',
packages=find_packages(),
install_requires=get_requirements(install_requires_path)

)