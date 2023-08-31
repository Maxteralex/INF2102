import unittest
from abc import abstractmethod
from connection.connection import Connection

class TestConnection(unittest.TestCase):

    def setUp(self):
        class MockConnection(Connection):
            @abstractmethod
            def configure(self, conn_settings: dict, chunk_size: int = None) -> None:
                pass

            @abstractmethod
            def connect(self) -> None:
                pass

            @abstractmethod
            def disconnect(self) -> None:
                pass

        self.mock_connection = MockConnection()

    def test_abstract_methods(self):
        with self.assertRaisesRegex(TypeError, "Can't instantiate abstract class"):
            Connection()
        with self.assertRaises(NotImplementedError):
            self.mock_connection.configure({}, chunk_size=10)
        with self.assertRaises(NotImplementedError):
            self.mock_connection.connect()
        with self.assertRaises(NotImplementedError):
            self.mock_connection.disconnect()

if __name__ == '__main__':
    unittest.main()
