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


def stdin_lines():
    return sys.stdin.readlines()


def main():
    rows = []
    num_authors = 0

    str_lines = (x.decode('utf-8')
                 for x in stdin_lines())

    for line in str_lines:
        match = COMMIT_REGEX.match(line)
        commit = match.group().strip() if match else 'None'

        match = COMMIT_AUTHOR_REGEX.match(line)
        author = match.group().split()[1] if match else 'None'

        if match:
            code = line[match.end():].rstrip()
        else:
            code = ''

        if commit not in commit_dict:
            commit_dict[commit] = COLOR_TAGS[num_authors % len(COLOR_TAGS)]
            num_authors += 1

        tag = commit_dict[commit]

        wrapped_commit = '{%s}%s{/%s}' % (tag, commit, tag)
        wrapped_author = '{%s}%s{/%s}' % (tag, author, tag)
        wrapped_code = '{%s}%s{/%s}' % (tag, code, tag)

        rows.append([Color(wrapped_commit),
                     Color(wrapped_author),
                     Color(wrapped_code),
                     ])

    table = BorderlessTable(rows)
    table.inner_heading_row_border = False
    print(table.unicode_table('utf-8'))


if __name__ == '__main__':
    main()
