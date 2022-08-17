"""
Py-EgyBest-Api
~~~~~~~~~
:Copyright: (c) 2022 By Amine Soukara <https://github.com/AmineSoukara>.
:License: MIT, See LICENSE For More Details.
:Description: Asynchronous Python Wrapper For EgyBest-API.
"""

from setuptools import find_packages, setup

AUTHOR = "AmineSoukara"
EMAIL = "AmineSoukara@gmail.com"
URL = "https://github.com/AmineSoukara/Py-EgyBest-Api"


# Get the long description
with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

VERSION = '1.7'

setup(
    name="Py-EgyBest-Api",
    version=VERSION,
    description="Asynchronous Python Wrapper For EgyBest-API.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    author=AUTHOR,
    author_email=EMAIL,
    url=URL,
    license="MIT",
    packages=find_packages(),
    keywords="EgyBest Api Scrapper Python",
    project_urls={
        "Source": "https://github.com/AmineSoukara/Py-EgyBest-Api",
        "Documentation": "https://github.com/AmineSoukara/Py-EgyBest-Api#readme",
        "Tracker": "https://github.com/AmineSoukara/Py-EgyBest-Api/issues",
    },
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Intended Audience :: Developers",
        "Topic :: Software Development :: Build Tools",
        "Natural Language :: English",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Topic :: Internet",
    ],
    python_requires=">=3.8",
    install_requires=["aiohttp", "aiofiles", "dotmap", "requests"],
)
