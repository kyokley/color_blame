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

COMMIT_REGEX = re.compile(r'^\s*[0-9a-fA-F^]+\s')
AUTHOR_REGEX = re.compile(r'.*?\([^\)]*\)')

commit_dict = dict()

def stdin_lines():
    return sys.stdin.readlines()

def main():
    rows = []
    num_authors = 0

    for line in stdin_lines():
        line = line.decode('utf-8')
        match = COMMIT_REGEX.match(line)
        commit = match.group().strip() if match else 'None'

        match = AUTHOR_REGEX.search(line)
        author = match.group().strip() if match else 'None'

        match = AUTHOR_REGEX.match(line)
        code = line[match.end():].rstrip() if match else 'None'

        if commit not in commit_dict:
            commit_dict[commit] = COLOR_TAGS[num_authors % len(COLOR_TAGS)]
            num_authors += 1

        tag = commit_dict[commit]

        wrapped_author = u'{%s}%s{/%s}' % (tag, author, tag)
        wrapped_code = u'{%s}%s{/%s}' % (tag, code, tag)

        rows.append([Color(wrapped_author),
                     Color(wrapped_code),
                     ])

    table = BorderlessTable(rows)
    table.inner_heading_row_border = False
    print(table.unicode_table('utf-8'))

if __name__ == '__main__':
    main()
