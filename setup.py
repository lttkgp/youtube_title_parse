"""
Setup script for youtube_title_parse
"""
import pathlib
from setuptools import setup, find_packages

# The directory containing this file
HERE = pathlib.Path(__file__).parent

# The text of the README file
README = (HERE / "README.md").read_text()

tests_require = ["six"]

setup(
    name="youtube_title_parse",
    version="1.0.0",
    description="Parse the title of a YouTube video to try and get artist & song name",
    long_description=README,
    long_description_content_type="text/markdown",
    url="https://github.com/lttkgp/youtube-title-parse",
    author="lttkgp",
    author_email="ghostwriternr@gmail.com",
    license="MIT",
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Natural Language :: English",
        "Programming Language :: Python :: 2.7",
        "Programming Language :: Python :: 3",
    ],
    keywords=["youtube", "title", "metadata", "parse", "music"],
    packages=find_packages(exclude=["contrib", "docs", "test*"]),
    install_requires=[],
    tests_require=tests_require,
    entry_points={
        "console_scripts": ["youtube_title_parse=youtube_title_parse.parse:main"],
    },
)
