import setuptools


def read_file(file_name):
    with open(file_name, "r") as fh:
        return fh.read()


setuptools.setup(
    name="sample_django_package",
    version="0.0.1",
    description="A Django app to spit out sample JSON response",
    long_description=read_file("README.md"),
    long_description_content_type="text/markdown",
    url="https://www.example.com",
    author="Noopur Phalak",
    author_email="noopurphalak007@gmail.com",
    license="MIT License",
    classifiers=[
        "Environment :: Web Environment",
        "Framework :: Django::3.2",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3.9",
        "Topic :: Internet :: WWW/HTTP",
        "Topic :: Internet :: WWW/HTTP :: Dynamic Content",
    ],
    packages=setuptools.find_packages(),
    python_requires=">=3.9",
    install_requires=read_file("requirements.txt"),
)
