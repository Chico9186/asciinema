import sys
try:
    from StringIO import StringIO
except ImportError:
    from io import StringIO


stdout = None


def assert_printed(expected):
    success = expected in stdout.getvalue()
    assert success, 'expected text "%s" not printed' % expected


def assert_not_printed(expected):
    success = expected not in stdout.getvalue()
    assert success, 'not expected text "%s" printed' % expected


class Test(object):

    def setUp(self):
        global stdout
        self.real_stdout = sys.stdout
        sys.stdout = stdout = StringIO()

    def tearDown(self):
        sys.stdout = self.real_stdout


class FakeClock(object):

    def __init__(self, values):
        self.values = values
        self.n = 0

    def time(self):
        value = self.values[self.n]
        self.n += 1

        return value
