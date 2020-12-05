from setuptools import setup, find_packages


def readme():
    with open("README.md") as f:
        return f.read()


setup(
    name="rich-view",
    version="0.1.0.dev1",
    description="Nicely viewing files using the rich library",
    long_description=readme(),
    classifiers=[
        "Development Status :: 2 - Pre-Alpha",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
    ],
    url="http://github.com/mbollmann/rich-view",
    author="Marcel Bollmann",
    author_email="marcel@bollmann.me",
    license="MIT",
    packages=find_packages(),
    entry_points={
        "console_scripts": [
            "rv = richview.bin.rv:main",
        ]
    },
    python_requires=">=3.6",
    install_requires=["docopt", "rich"],
    include_package_data=True,
    zip_safe=True,
)
