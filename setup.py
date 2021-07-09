from setuptools import setup

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="NekoMimi",
    version="1.0.4",
    author="NekoMimi",
    author_email="mrcreaperwhantsadingdongtobedo@gmail.com",
    description="A handy collection of tools",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/NekoKitsune/NekoMimi",
    project_urls={
        "Bug Tracker": "https://github.com/NekoKitsune/NekoMimi/issues",
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    packages=['NekoMimi'],
    scripts=['src/NekoMimi.py','src/__init__.py'],
    python_requires=">=3.6",
)