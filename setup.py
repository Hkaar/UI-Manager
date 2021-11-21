from setuptools import setup

setup(
    name="ui-manager",
    version="0.2",

    author="Hkaar",
    author_email="HkaarDev@gmail.com",

    license="MIT License (MIT)",

    description="A UI Manager for PyQt & PySide",
    long_description=open("README.md").read(),

    packages=["ui_manager"],
    include_package_data=True,

    package_data={
        ".": ["*txt"],
        "ui_manager": ["resources/themes/*.qss"],
    },

    python_requires=">=3.4",
    platforms="Windows, OS X, Linux"
)