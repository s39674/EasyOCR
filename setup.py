"""
End-to-End Multi-Lingual Optical Character Recognition (OCR) Solution
"""
import re
from setuptools import setup
from pkg_resources import get_distribution, DistributionNotFound
from io import open
import sys

with open('requirements.txt', encoding="utf-8-sig") as f:
    requirements = f.readlines()


def getDescription():
    with open('README.md', encoding="utf-8-sig") as f:
        README = f.read()
    return README

# From: https://github.com/aleju/imgaug/blob/master/setup.py ; modified
def check_alternative_installation(install_require, alternative_install_requires):
    """If some version version of alternative requirement installed, return alternative,
    else return main.
    """
    # install_require: opencv-python-headless<=4.5.4.60 alternative_install_requires: ["opencv-python<=4.5.4.60",  "opencv-contrib-python-headless"]
    for alternative_install_require in alternative_install_requires:
        try:
            # [0] == name ; [1] == version;
            alternative_pkg = re.split(r"[!<>=]", alternative_install_require)
            a = get_distribution(alternative_pkg)
            print(a)
            return str(alternative_install_require)
        except DistributionNotFound:
            continue

    return str(install_require)


def get_install_requirements(main_requires, alternative_requires):
    """Iterates over all install requires
    If an install require has an alternative option, check if this option is installed
    If that is the case, replace the install require by the alternative to not install dual package"""
    install_requires = []
    for main_require in main_requires:
        #print(f"main_require: {main_require}  | alternative_requires: {alternative_requires}")
        if main_require in alternative_requires:
            print("True!")
            main_require = check_alternative_installation(main_require, alternative_requires.get(main_require))
        install_requires.append(main_require)

    return install_requires

INSTALL_REQUIRES = [req.strip() for req in requirements]

# should also check "opencv-contrib-python"
# TODO: IT DOSENT ACTUALLY CHECK IF YOU HAVE THE CORRECT VERSION!
ALT_INSTALL_REQUIRES = {
    "opencv-python-headless<=4.5.4.60": ["opencv-python<=4.5.4.60",  "opencv-contrib-python-headless"],
}

INSTALL_REQUIRES = get_install_requirements(INSTALL_REQUIRES, ALT_INSTALL_REQUIRES)
print(INSTALL_REQUIRES)

sys.exit(0)
setup(
    name='easyocr',
    packages=['easyocr'],
    include_package_data=True,
    version='1.5.0',
    install_requires=INSTALL_REQUIRES,
    entry_points={"console_scripts": ["easyocr= easyocr.cli:main"]},
    license='Apache License 2.0',
    description='End-to-End Multi-Lingual Optical Character Recognition (OCR) Solution',
    long_description=getDescription(),
    long_description_content_type="text/markdown",
    author='Rakpong Kittinaradorn',
    author_email='r.kittinaradorn@gmail.com',
    url='https://github.com/jaidedai/easyocr',
    download_url='https://github.com/jaidedai/easyocr.git',
    keywords=['ocr optical character recognition deep learning neural network'],
    classifiers=[
        'Development Status :: 5 - Production/Stable'
    ],
)
