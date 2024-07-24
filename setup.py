from setuptools import setup, find_packages

setup(
    name='comsol_clone',
    version='0.1',
    author='Dominic James LaCavera Jr./PythonGPT',
    author_email='Djlacavera21@gmail.com',
    description='A free software version of COMSOL MultiPhysics Simulator',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/djlacavera21/comsol_clone',
    packages=find_packages(where='src'),
    package_dir={'': 'src'},
    include_package_data=True,
    install_requires=[
        'numpy',
        'scipy',
        'matplotlib',
        'PyQt5',
    ],
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
    entry_points={
        'console_scripts': [
            'comsol_clone = gui.main_window:main',
        ],
    },
)

