from setuptools import setup, find_packages

setup(
    name="mecabpr",
    packages=find_packages(),
    version="0.0.1",
    description="",
    author="yag_ays",
    author_email="yanagi.ayase@gmail.com",
    url="https://github.com/yagays/mecabpr",
    install_requires=['mecab-python3'],
    keywords=["MeCab", "japanese", "part-of-speech"],
    classifiers=[
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "Natural Language :: Japanese",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Topic :: Software Development :: Libraries :: Python Modules"
    ]
)
