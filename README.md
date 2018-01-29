# Color Blame
Script to colorize svn/git blame output

## Purpose
The purpose of this script is to add some highlighting to the output of the blame function. All lines from the same commit receive the same color. Because the number of colors available is limited, it is not possible to assign a unique color to each commit. However, I believe that even a couple of colors can be useful in displaying what blocks of code were changed together.

## Usage
```bash
$ git blame init.vim | color_git_blame | less
```
