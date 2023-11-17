from setuptools import setup, find_packages

setup(
    name="Color Blame",
    version="0.4",
    description="Colorize VCS blame command output",
    long_description="Colorize blame output for git and svn",
    url="https://github.com/kyokley/color_blame",
    author="Kevin Yokley",
    author_email="kyokley2@gmail.com",
    license="MIT",
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: End Users/Desktop",
        "Programming Language :: Python :: 3",
    ],
    packages=find_packages(),
    install_requires=[
        "terminaltables",
        "colorclass",
    ],
    tests_require=[
        "mock",
    ],
    entry_points={
        "console_scripts": [
            "color_svn_blame = colorize.svn_colorize:main",
            "color_git_blame = colorize.git_colorize:main",
        ],
    },
)
