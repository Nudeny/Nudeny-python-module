from setuptools import setup, find_packages
import codecs
import os

here = os.path.abspath(os.path.dirname(__file__))

with codecs.open(os.path.join(here, "README.md"), encoding="utf-8") as fh:
    long_description = "\n" + fh.read()

VERSION = '0.0.1'
DESCRIPTION = 'Image nudity classification and detection package.'
LONG_DESCRIPTION = 'A package that allows to developers to classify or detect nudity in an Image.'

# Setting up
setup(
    name="nudeny",
    version=VERSION,
    author="Nudeny",
    author_email="<thesis.nudeny69@gmail.com>",
    description=DESCRIPTION,
    long_description_content_type="text/markdown",
    long_description=LONG_DESCRIPTION,
    packages=find_packages(),
    install_requires=['certifi', 'charset-normalizer', 'idna', 'Pillow', 'requests', 'urllib3'],
    keywords=['python', 'nudity', 'classification', 'detection', 'machine learning'],
    classifiers=[
        "Development Status :: 1 - Planning",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ]
)