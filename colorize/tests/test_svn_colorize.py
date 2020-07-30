import pytest
from colorize.svn_colorize import main


class TestMain:
    @pytest.fixture(autouse=True)
    def setUp(self, mocker):
        mocker.patch('colorize.svn_colorize.COLOR_TAGS', ['mock_color'])

        self.mock_Color = mocker.patch('colorize.svn_colorize.Color')
        self.mock_Color.side_effect = ['colored_commit',
                                       'colored_author',
                                       'colored_code']

        self.mock_BorderlessTable = mocker.patch('colorize.svn_colorize.BorderlessTable')

        self.mock_stdin_lines = mocker.patch('colorize.svn_colorize.stdin_lines')

    def test_ascii(self):
        self.mock_stdin_lines.return_value = [' 51232    jdoe  #!/usr/bin/env python']
        main()

        self.mock_Color.assert_any_call('{mock_color}51232{/mock_color}')
        self.mock_Color.assert_any_call('{mock_color}jdoe{/mock_color}')
        self.mock_Color.assert_any_call('{mock_color}  #!/usr/bin/env python{/mock_color}')

        self.mock_BorderlessTable.assert_called_once_with([['colored_commit',
                                                            'colored_author',
                                                            'colored_code']])

    def test_unicode(self):
        self.mock_stdin_lines.return_value = [' 51232    \u0135\u1d81\xf0\xeb  #!/usr/bin/env python']
        main()

        self.mock_Color.assert_any_call('{mock_color}51232{/mock_color}')
        self.mock_Color.assert_any_call('{mock_color}\u0135\u1d81\xf0\xeb{/mock_color}')
        self.mock_Color.assert_any_call('{mock_color}  #!/usr/bin/env python{/mock_color}')

        self.mock_BorderlessTable.assert_called_once_with([['colored_commit',
                                                            'colored_author',
                                                            'colored_code']])

    def test_byte_str(self):
        self.mock_stdin_lines.return_value = [' 51232    \u0135\u1d81\xf0\xeb  #!/usr/bin/env python'.encode('utf-8')]
        main()

        self.mock_Color.assert_any_call('{mock_color}51232{/mock_color}')
        self.mock_Color.assert_any_call('{mock_color}\u0135\u1d81\xf0\xeb{/mock_color}')
        self.mock_Color.assert_any_call('{mock_color}  #!/usr/bin/env python{/mock_color}')

        self.mock_BorderlessTable.assert_called_once_with([['colored_commit',
                                                            'colored_author',
                                                            'colored_code']])
