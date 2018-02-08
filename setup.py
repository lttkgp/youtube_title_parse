"""
Setup script for youtube_title_parse
"""
from setuptools import setup, find_packages

setup(
    name='youtube_title_parse',
    description='Parse the title of a YouTube video to try and get artist & song name',
    version='1.0.0b1',
    url='https://github.com/lttkgp/youtube-title-parse',
    author='Naresh R',
    author_email='ghostwriternr@gmail.com',
    license='GNU General Public License v3 (GPLv3)',
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: GNU General Public License v3 (GPLv3)',
        'Natural Language :: English',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
    ],
    keywords=['youtube', 'title', 'metadata', 'parse', 'music'],
    packages=find_packages(exclude=['contrib', 'docs', 'tests*']),
    install_requires=[],
    entry_points={
        'console_scripts': [
            'youtube_title_parse=youtube_title_parse.parse:main'
        ],
    }
)
