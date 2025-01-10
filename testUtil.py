import unittest
from unittest.mock import patch
from src.util import *

class TestUtilities(unittest.TestCase):

    @patch('sys.argv', ['script.py', 'arg1', 'arg2'])
    def test_arguments(self):
        self.assertRaises(TooManyArgumentsError, getArgs)

    def test_empty_file(self):
        self.assertRaises(MissingSection, parseInput, 'test/input_5.txt')

    def test_section_names(self):
        self.assertRaises(MissnamedSection, parseInput, 'test/input_6_1.txt')
        self.assertRaises(MissnamedSection, parseInput, 'test/input_6_2.txt')
        self.assertRaises(MissnamedSection, parseInput, 'test/input_6_3.txt')
    
    def test_needed_sections_exist(self):
        self.assertRaises(ChargerWitoutStation, parseInput, 'test/input_7_1.txt')
        self.assertRaises(ValueError, parseInput, 'test/input_7_2.txt')
        self.assertRaises(MissingSection, parseInput, 'test/input_7_3.txt')
    
    def test_improper_inputs(self):
        self.assertRaises(InvalidFormat, parseInput, 'test/input_8_1.txt')
        self.assertRaises(InvalidFormat, parseInput, 'test/input_8_2.txt')
        self.assertRaises(InvalidFormat, parseInput, 'test/input_8_3.txt')
        self.assertRaises(InvalidFormat, parseInput, 'test/input_8_4.txt')
        self.assertRaises(InvalidFormat, parseInput, 'test/input_8_5.txt')
        self.assertRaises(InvalidFormat, parseInput, 'test/input_8_6.txt')
        self.assertRaises(InvalidFormat, parseInput, 'test/input_8_7.txt')
        self.assertRaises(InvalidFormat, parseInput, 'test/input_8_8.txt')
        self.assertRaises(ValueError, parseInput, 'test/input_8_9.txt')
        self.assertRaises(ValueError, parseInput, 'test/input_8_10.txt')
        self.assertRaises(ValueError, parseInput, 'test/input_8_11.txt')

    def test_stationId_duplicates(self):
        self.assertRaises(DuplicatedStationID, parseInput, 'test/input_9.txt')

    def test_empty_station(self):
        self.assertRaises(EmptyStation, parseInput, 'test/input_10.txt')
    
    def test_duplicate_charger_across_stations(self):
        self.assertRaises(DuplicatedChargerID, parseInput, 'test/input_11.txt')

    def test_valid_report_window(self):
        self.assertRaises(InvalidFormat, parseInput, 'test/input_12.txt')

    def test_charger_without_station(self):
        self.assertRaises(ChargerWitoutStation, parseInput, 'test/input_13.txt')
    
    def test_compute_uptime(self):
        input = [(1001, 0.0, 50000.0, True), 
                 (1001, 50000.0, 100000.0, True), 
                 (1002, 50000.0, 100000.0, True)]
        self.assertEqual(computeUptime(input), (100000,100000))

        input = [(2, 1000.0, 10500.0, True), 
                 (1, 10000.0, 11500.0, False), 
                 (5, 14000.0, 22000.0, False), 
                 (2, 16000.0, 23500.0, False), 
                 (2, 16500.0, 23000.0, False), 
                 (1, 18000.0, 23000.0, True), 
                 (1, 19000.0, 21500.0, True), 
                 (2, 22000.0, 31000.0, True), 
                 (5, 33000.0, 40000.0, True), 
                 (5, 63000.0, 71000.0, False), 
                 (1, 66500.0, 70000.0, True), 
                 (5, 82000.0, 84000.0, True), 
                 (5, 89000.0, 90500.0, True), 
                 (2, 89500.0, 98000.0, False), 
                 (1, 96000.0, 98000.0, True)]
        self.assertEqual(computeUptime(input), (38500,97000))

        input = [(6, 11500.0, 15000.0, True), 
                 (6, 42000.0, 48000.0, False), 
                 (6, 56000.0, 59000.0, False), 
                 (6, 64000.0, 73000.0, True), 
                 (6, 86500.0, 88000.0, True)]
        self.assertEqual(computeUptime(input), (14000,76500))


if __name__ == '__main__':
    unittest.main()