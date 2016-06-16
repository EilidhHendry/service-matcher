import unittest
import match

class TestMatch(unittest.TestCase):

    test_cases = [
    ('I need a plumber', ('plumber', None)),
    ('eliktrition', ('electrician', None)),
    ('', (None, None)),
    ('carpet cleaning', ('cleaner', 'carpet cleaning')),
    ('PlUmBeR', ('plumber', None))
    ]

    def test_fuzzy(self):
        for input_query, service in self.test_cases:
            self.assertEquals(match.fuzzy_match(input_query), service)

if __name__ == '__main__':
    unittest.main()
