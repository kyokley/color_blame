import mock
import unittest
from colorize.git_colorize import main

class TestMain(unittest.TestCase):
    def setUp(self):
        self.stdin_lines_patcher = mock.patch('colorize.git_colorize.stdin_lines')
        self.mock_stdin_lines = self.stdin_lines_patcher.start()

    def tearDown(self):
        self.stdin_lines_patcher.stop()

    def test_ascii(self):
        self.mock_stdin_lines.return_value = ['e7ab9458 (John Doe        2017-05-13 16:24:56 -0700    1) #!/usr/bin/env python',
                ]
        main()

    def test_unicode(self):
        self.mock_stdin_lines.return_value = [u'e7ab9458 (\u0134\xf0\u0127\xf1 \xd0\xf0\xeb        2017-05-13 16:24:56 -0700    1) #!/usr/bin/env python',
                ]
        main()

    def test_byte_str(self):
        self.mock_stdin_lines.return_value = [u'e7ab9458 (\u0134\xf0\u0127\xf1 \xd0\xf0\xeb        2017-05-13 16:24:56 -0700    1) #!/usr/bin/env python'.encode('utf-8'),
                ]
        main()
