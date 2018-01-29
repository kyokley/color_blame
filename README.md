# Color Blame
Script to colorize svn/git blame output

![Screenshot](/../screenshots/blame.jpg?raw=true)

## Purpose
The purpose of this script is to add some highlighting to the output of the blame function. All lines from the same commit receive the same color. Because the number of colors available is limited, it is not possible to assign a unique color to each commit. However, I believe that even a couple of colors can be useful in displaying what blocks of code were changed together.

## Installation
The easiest way to install this script is to invoke it through docker. Add the following to your .bashrc.

```bash
alias color_svn_blame="docker run --rm \
                                  -i \
                                  kyokley/color_blame \
                                  color_svn_blame"
alias color_git_blame="docker run --rm \
                                  -i \
                                  kyokley/color_blame \
                                  color_git_blame"
```

## Usage
For svn:
```bash
$ svn blame FILENAME | color_svn_blame | less
```

For git:
```bash
$ git blame FILENAME | color_git_blame | less
```
