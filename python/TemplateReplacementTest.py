__author__ = 'ssinghal'

import unittest
import TemplateReplacement


class TemplateReplacementTest(unittest.TestCase):
    def test_perform_template_replacement(self):
        file_location = "/u001/src/github/sandeepsinghal/code-samples/python/files/sample_template.txt"
        variable_map = dict()
        variable_map['GOOGLE_INDIA_URL'] = "http://google.co.in"
        variable_map['GOOGLE_US_URL'] = "http://google.com"

        replaced_data = TemplateReplacement.perform_template_replacement(file_location, variable_map)
        print replaced_data
        #self.assertEqual(True, "http://google.co.in" in replaced_data)

if __name__ == '__main__':
    unittest.main()
