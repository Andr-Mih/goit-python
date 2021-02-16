from setuptools import setup, find_namespace_packages

setup(
    name = 'sort_folder',
    version = '1.0',
    author = 'Andrii Mikhalkin',
    description = 'Scrits for sort file in folder',
    entry_points = {'console_scripts': ['sort=sort_folder.sort:main']},
    license = 'MIT',
    packages = find_namespace_packages(),
) 
