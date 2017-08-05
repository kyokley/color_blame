import sys
import re
from colorclass import Color
from random import SystemRandom
from terminaltables import BorderlessTable

COLOR_TAGS = [
        'autored',
        'autoyellow',
        'autocyan',
        'automagenta',
        'autoblue',
        'autogreen',
        ]
SystemRandom().shuffle(COLOR_TAGS)

COMMIT_REGEX = re.compile(r'\s*[0-9a-fA-F]+')
COMMIT_AUTHOR_REGEX = re.compile(r'^\s*\d+\s+\S+')

commit_dict = dict()

def main():
    rows = []
    num_authors = 0

    for line in sys.stdin.readlines():
        match = COMMIT_REGEX.match(line)
        commit = match.group().strip()

        match = COMMIT_AUTHOR_REGEX.match(line)
        author = match.group().split()[1]
        code = line[match.end():].rstrip()

        if commit not in commit_dict:
            commit_dict[commit] = COLOR_TAGS[num_authors % len(COLOR_TAGS)]
            num_authors += 1

        tag = commit_dict[commit]
        rows.append([Color('{%s}%s{/%s}' % (tag, commit, tag)),
                     Color('{%s}%s{/%s}' % (tag, author, tag)),
                     Color('{%s}%s{/%s}' % (tag, code, tag)),
                     ])

    table = BorderlessTable(rows)
    table.inner_heading_row_border = False
    print(table.table)

if __name__ == '__main__':
    main()
