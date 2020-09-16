import setuptools

setuptools.setup(
    name="psc-parse",
    version="0.1",
    install_requires=['pyknp<=0.4.1', 'scikit-learn'],
    author="satamame",
    author_email="satax@nifty.com",
    description="Train/use tree model to parse play script",
    long_description="Train/use tree model to parse play script",
    long_description_content_type="text/markdown",
    url="https://github.com/satamame/psc_parse",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ]
)
