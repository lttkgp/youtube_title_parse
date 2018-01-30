"""
Setup script for youtube-title-parse
"""
from setuptools import setup, find_packages

setup(name='youtube-title-parse',
      description='Parse the title of a YouTube video to try and get artist & song name',
      version='1.0.0a1',
      url='https://github.com/lttkgp/youtube-title-parse',
      author='Naresh R',
      author_email='ghostwriternr@gmail.com',
      license='GNU General Public License version 3',
      classifiers=[
          'Development Status :: 3 - Alpha',
          'Intended Audience :: Developers',
          'License :: OSI Approved :: GNU General Public License version 3',
          'Programming Language :: Python :: 3'
      ],
      keywords='youtube title metadata parse music',
      packages=find_packages(exclude=['contrib', 'docs', 'tests*']),
      install_requires=[],
      entry_points={
          'console_scripts': [
              'youtube-title-parse=youtube-title-parse.parse:main',
          ],
      })
