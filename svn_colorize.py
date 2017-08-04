import sys
import re
from colorclass import Color
from random import SystemRandom

COLOR_TAGS = [
        'autored',
        'autoyellow',
        'autocyan',
        'automagenta',
        'autoblue',
        'autogreen',
        ]
SystemRandom().shuffle(COLOR_TAGS)

COMMIT_REGEX = re.compile(r'\s*\d+')
commit_dict = dict()

def main():
    num_authors = 0

    for line in sys.stdin.readlines():
        match = COMMIT_REGEX.match(line)
        commit = match.group().strip()

        if commit not in commit_dict:
            commit_dict[commit] = COLOR_TAGS[num_authors % len(COLOR_TAGS)]
            num_authors += 1

        tag = commit_dict[commit]
        print(Color('{%s}%s{/%s}' % (tag, line.strip(), tag)))


if __name__ == '__main__':
    main()
