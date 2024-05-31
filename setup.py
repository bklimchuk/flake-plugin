from setuptools import setup


setup(
    name="braces_checker",
    license="MIT",
    version="1.1.8",
    package_dir={"": "braces_checker/"},
    packages=["braces_checker"],
    entry_points={
        "flake8.extension": [
            "XF51 = braces_checker.braces_checker:BracesChecker"
        ],
    },
    classifiers=[
        "Framework :: Flake8",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.11",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "Topic :: Software Development :: Quality Assurance",
    ],
)
