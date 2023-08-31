import unittest
from mapper.mapper import Mapper

class TestMapper(unittest.TestCase):

    def setUp(self):
        # Create an instance of Mapper
        self.mapper = Mapper()
        self.mock_class = type('MockClass', (), {'method': lambda: 'mock'})

    def test_get_key_variable_existing_key(self):
        # Test the _getKeyVariable method with an existing key
        self.mapper.mapper_dict = {'key': self.mock_class}

        result = self.mapper._getKeyVariable('key')

        self.assertEqual(result, self.mock_class)

    def test_get_key_variable_non_existing_key(self):
        # Test the _getKeyVariable method with a non-existing key
        with self.assertRaises(ModuleNotFoundError):
            self.mapper._getKeyVariable('non_existing_key')

if __name__ == '__main__':
    unittest.main()
