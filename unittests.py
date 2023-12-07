import socket
import unittest
from unittest.mock import patch, MagicMock
from PyScanner import validate_arguments, get_target_ip, port_scan


class TestPortScanner(unittest.TestCase):

    @patch('sys.argv', ['PyScanner.py', '192.168.1.1'])
    def test_validate_arguments_valid(self):
        self.assertEqual(validate_arguments(), '192.168.1.1')

    @patch('sys.argv', ['PyScanner.py'])
    def test_validate_arguments_invalid(self):
        with self.assertRaises(SystemExit):
            validate_arguments()

    @patch('socket.gethostbyname', return_value='192.168.1.1')
    def test_get_target_ip_valid(self, mock_gethostbyname):
        self.assertEqual(get_target_ip('localhost'), '192.168.1.1')

    @patch('socket.gethostbyname', side_effect=socket.error)
    def test_get_target_ip_invalid(self, mock_gethostbyname):
        with self.assertRaises(SystemExit):
            get_target_ip('invalid_host')

    @patch('socket.socket')
    def test_port_scan_open_port(self, mock_socket):
        mock_socket_instance = mock_socket.return_value
        mock_socket_instance.connect_ex.return_value = 0
        self.assertIsNone(port_scan('192.168.1.1', 80))  # Assuming port 80 is open

    @patch('socket.socket')
    def test_port_scan_closed_port(self, mock_socket):
        mock_socket_instance = mock_socket.return_value
        mock_socket_instance.connect_ex.return_value = 1
        self.assertIsNone(port_scan('192.168.1.1', 81))  # Assuming port 81 is closed


if __name__ == '__main__':
    unittest.main()
