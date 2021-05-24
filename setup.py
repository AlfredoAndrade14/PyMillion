from setuptools import setup, find_packages

with open("README.md", "r") as fh:
    readme = fh.read()

setup(
    name='PyMillion',
    version="1.0.0rc1",
    description='Um jogo do milhão sobre python feito em python',
    long_description=readme,
    long_description_content_type="text/markdown",
    url='https://github.com/AlfredoAndrade14/PyMillion',
    author='Alfredo Vasconcelos de Andrade e André Araújo Alves',
    author_email='alfredov.andrade@gmail.com',
    license='MIT',
    keywords=[
        'jogo',
        'game',
        'Jogo do milhão',
        'retro',
        'quiz'
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    packages=find_packages(),
    install_requires=['pygame>=2.0'],
    entry_points={
        'console_scripts': [
            'pymillion=python3 -m PyMillion'
        ]
    },
    python_requires='>=3.6',
    include_package_data=True,
)