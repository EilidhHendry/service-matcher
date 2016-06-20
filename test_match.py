import unittest
import match

class TestMatch(unittest.TestCase):

    service_test_cases = [
    ('I need a plumber', ('plumber', None)),
    ('eliktrition', ('electrician', None)),
    ('', (None, None)),
    ('carpet cleaning', ('cleaner', 'carpet cleaning')),
    ('PlUmBeR', ('plumber', None))
    ]

    def test_fuzzy(self):
        for input_query, service in self.service_test_cases:
            self.assertEquals(match.fuzzy_match(input_query), service)

    process_test_cases = [
    ("TeS.tI,nG", ["testing"]),
    ("ThIs IS a . test  sent()ence", ["test", "sentence"]),
    ("Install a washing machine", ["install", "washing", "machine"]),
    ("", []),
    ]

    def test_pre_process(self):
        for input_query, result in self.process_test_cases:
            self.assertEquals(match.pre_process(input_query), result)


if __name__ == '__main__':
    unittest.main()
