import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="NekoMimi",
    version="1.0.8",
    author="NekoMimi",
    author_email="nekomimi@tilde.team",
    description="A module to assist coding in python with useful shortcuts and tools",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/NekoMimiOfficial/NekoMimi",
    project_urls={
        "Bug Tracker": "https://github.com/NekoMimiOfficial/NekoMimi/issues",
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    package_dir={"./": "NekoMimi/"},
    install_requires = ['pyfiglet', 'requests', 'BeautifulSoup4', 'termcolor'],
    packages=setuptools.find_packages(),
    python_requires=">=3.6",
)
