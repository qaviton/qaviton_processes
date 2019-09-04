package_name = "qaviton_processes"


if __name__ == "__main__":
    from sys import version_info as v
    from qaviton_processes import __author__, __version__, __author_email__, __description__, __url__, __license__
    from setuptools import setup, find_packages
    with open("requirements.txt") as f: requirements = f.read().splitlines()
    with open("README.md", encoding="utf8") as f: long_description = f.read()
    setup(
        name=package_name,
        version=__version__,
        author=__author__,
        author_email=__author_email__,
        description=__description__,
        long_description=long_description,
        long_description_content_type="text/markdown",
        url=__url__,
        packages=[pkg for pkg in find_packages() if pkg.startswith(package_name)],
        license=__license__,
        classifiers=[
            f"Programming Language :: Python :: {v[0]}.{v[1]}",
        ],
        install_requires=requirements
    )
