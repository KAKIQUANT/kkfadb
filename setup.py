from setuptools import setup, find_packages

setup(
    name="kkfadb",
    version="0.1.0",
    packages=find_packages(),
    install_requires=[
        "pandas>=1.5.0",
        "numpy>=1.20.0",
        "matplotlib>=3.5.0",
        "seaborn>=0.11.0",
        "scipy>=1.7.0",
        "statsmodels>=0.13.0",
    ],
    author="KakiQuant",
    author_email="support@kakiquant.com",
    description="Factor analysis and management library for KakiQuant",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/kakiquant/kkfadb",
) 