from setuptools import setup


setup(
    name="func_checker",
    license="MIT",
    version="1.3.0",
    package_dir={"": "checkers/"},
    packages=["func_checker"],
    entry_points={
        "flake8.extension": [
            "XF51 = func_checker.func_arg_checker:FunctionFormatChecker"
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
    tests_require=[
        'pytest'
    ]
)
