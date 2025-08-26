
from setuptools import setup, find_packages
from typing import List

def get_requirements(file_path: str) -> list[str]:
    with open(file_path) as file_obj:
        requirements = file_obj.readlines()
        requirements = [req.replace("\n", "") for req in requirements]
        
        if '-e .' in requirements:
            requirements.remove('-e .')
    return requirements

setup(
    name='your_package_name',
    version='0.0.1',
    author = 'Hamza',
    author_email = 'hamzashakil497@gmail.com',
    packages=find_packages(),
    install_requires=get_requirements('requirements.txt')
) 