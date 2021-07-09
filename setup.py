import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="NekoMimi",                     
    version="1.0.0",                        
    author="NekoMimi",                     
    description="NekoMimi's special utilities",
    long_description=long_description,      
    long_description_content_type="text/markdown",
    packages=setuptools.find_packages(),    
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],                                      
    python_requires='>=3.6',               
    py_modules=["NekoMimi"],             
    package_dir={'':'src'},     
    install_requires=['pyfiglet']                     
)