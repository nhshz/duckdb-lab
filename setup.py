from setuptools import find_packages, setup

setup(
    name="pandas-demo",
    version="1.0.0",
    packages=find_packages(where="src"),
    package_dir={"": "src"},
    install_requires=["boto3>=1.16"],
    entry_points={
        "console_scripts": [
            "dataset-download=pandasdemo.download:main",
        ]
    },
)
