from setuptools import find_packages, setup

setup(
    name="app",
    version="1.0.0",
    packages=find_packages(),
    install_requires=[
        "django==5.1.4",
        "fastapi[all]==0.115.6",
        "psycopg==3.2.3",
    ],
)
