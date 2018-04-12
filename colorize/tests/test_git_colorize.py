import mock
import unittest
from colorize.git_colorize import main

class TestMain(unittest.TestCase):
    def setUp(self):
        self.COLOR_TAGS_patcher = mock.patch('colorize.git_colorize.COLOR_TAGS', ['mock_color'])
        self.COLOR_TAGS_patcher.start()

        self.Color_patcher = mock.patch('colorize.git_colorize.Color')
        self.mock_Color = self.Color_patcher.start()
        self.mock_Color.side_effect = ['colored_author',
                                       'colored_code']

        self.BorderlessTable_patcher = mock.patch('colorize.git_colorize.BorderlessTable')
        self.mock_BorderlessTable = self.BorderlessTable_patcher.start()

        self.stdin_lines_patcher = mock.patch('colorize.git_colorize.stdin_lines')
        self.mock_stdin_lines = self.stdin_lines_patcher.start()

    def tearDown(self):
        self.COLOR_TAGS_patcher.stop()
        self.Color_patcher.stop()
        self.BorderlessTable_patcher.stop()
        self.stdin_lines_patcher.stop()

    def test_ascii(self):
        self.mock_stdin_lines.return_value = ['e7ab9458 (John Doe        2017-05-13 16:24:56 -0700    1) #!/usr/bin/env python',
                ]
        main()

        self.mock_Color.assert_any_call(u'{mock_color}e7ab9458 (John Doe        2017-05-13 16:24:56 -0700    1){/mock_color}')
        self.mock_Color.assert_any_call(u'{mock_color} #!/usr/bin/env python{/mock_color}')

        self.mock_BorderlessTable.assert_called_once_with([['colored_author',
                                                            'colored_code']])

    def test_unicode(self):
        self.mock_stdin_lines.return_value = [u'e7ab9458 (\u0134\xf0\u0127\xf1 \xd0\xf0\xeb        2017-05-13 16:24:56 -0700    1) #!/usr/bin/env python',
                ]
        main()

        self.mock_Color.assert_any_call(u'{mock_color}e7ab9458 (\u0134\xf0\u0127\xf1 \xd0\xf0\xeb        2017-05-13 16:24:56 -0700    1){/mock_color}')
        self.mock_Color.assert_any_call(u'{mock_color} #!/usr/bin/env python{/mock_color}')

        self.mock_BorderlessTable.assert_called_once_with([['colored_author',
                                                            'colored_code']])

    def test_byte_str(self):
        self.mock_stdin_lines.return_value = [u'e7ab9458 (\u0134\xf0\u0127\xf1 \xd0\xf0\xeb        2017-05-13 16:24:56 -0700    1) #!/usr/bin/env python'.encode('utf-8'),
                ]
        main()

        self.mock_Color.assert_any_call(u'{mock_color}e7ab9458 (\u0134\xf0\u0127\xf1 \xd0\xf0\xeb        2017-05-13 16:24:56 -0700    1){/mock_color}')
        self.mock_Color.assert_any_call(u'{mock_color} #!/usr/bin/env python{/mock_color}')

        self.mock_BorderlessTable.assert_called_once_with([['colored_author',
                                                            'colored_code']])

# TODO: Add tests for git blame output that contains filenames
