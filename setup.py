from setuptools import setup, find_packages
from typing import List

HYPEN_E_DOT = '-e .'


def get_requirements(filename: str) -> List[str]:
    # This function reads the requirements.txt file and returns a list of requirements
    requirements = []
    with open(filename) as f:
        requirements = f.read().splitlines()
        requirements = [req.replace('\n', '') for req in requirements]

        if HYPEN_E_DOT in requirements:
            requirements.remove(HYPEN_E_DOT)

    return requirements


setup(
    name='mlproject',
    version='0.0.1',
    author='Hardik',
    author_email='hardikgangajaliya05@gmail.com',
    packages=find_packages(),
    install_requires=get_requirements('requirements.txt'),
)
