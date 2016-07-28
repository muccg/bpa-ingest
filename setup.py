from setuptools import setup, find_packages

install_requires = [
    'requests>=2.2',
    'ckanapi',
    'git+https://github.com/muccg/ckanapi.git@streaming-uploads',
    'unipath==1.1',
    'xlrd==0.9.4',
    'xlwt==1.0.0',
    'beautifulsoup4==4.4.1',
    'python-dateutil==2.5.3',
    'requests==2.10.0',
]

setup(
    author="CCG, Murdoch University",
    author_email="info@ccg.murdoch.edu.au",
    description="Ingest script for BPA data to CKAN",
    license="GPL3",
    keywords="",
    url="https://github.com/muccg/bpa-ingest",
    name="bpaingest",
    version="1.0.0",
    packages=find_packages(exclude=["*.tests", "*.tests.*", "tests.*", "tests"]),
    install_requires=install_requires,
    entry_points={
        'console_scripts': [
            'bpa-ingest=bpaingest.cli:main',
        ],
    }
)
