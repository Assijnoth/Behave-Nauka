from setuptools import setup, find_packages

setup(
    name="PWA Behave/Selenium Automatic Tests",
    description="...the spice must flow...",
    long_description=open("readme.txt").read().strip(),
    long_description_content_type="text/markdown",
    license="",
    version="0.9 Atreides",
    packages=find_packages(),
    scripts=[],
    url="",
    author="Azzinoth",
    author_email="michaln@ecom.house",
    python_requires=">=3.8, <4",
    install_requires=[
        "selenium>=3.141.0",
        "behave>=1.2.6",
        "behave-webdriver>=0.3.1,"
        "urllib3==1.26.15",
        "requests>=2.30.0",

    ],
    classifiers=[],
    extras_require={"dev": ["black"], "test": ["pytest"], "docs": ["sphinx"]},
    package_data={},
)
