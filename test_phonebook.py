import unittest
from phonebook import Phonebook


class PhonebookTest(unittest.TestCase):

	# This will run before each test case
	def setUp(self) -> None:
		self.phonebook = Phonebook()

	# This will run after each test case - for eg. to release resources
	def tearDown(self) -> None:
		pass

	def test_lookup_by_name(self):
		self.phonebook.add("Nav","9878239087")
		number = self.phonebook.lookup("Nav")
		self.assertEqual("9878239087",number)

	def test_mising_name(self):
		with self.assertRaises(KeyError):
			self.phonebook.lookup("Missing")

	def test_empty_phonebook_is_consistent(self):
		self.assertTrue(self.phonebook.is_consistent())

	def test_is_consistent_with_different_entries(self):
		self.phonebook.add("Bob","12900")
		self.phonebook.add("Ali","012900")
		self.assertTrue(self.phonebook.is_consistent())

	def test_is_consistent_with_duplicate_entries(self):
		self.phonebook.add("Reema","98998")
		self.phonebook.add("Sushma","98998")
		self.assertFalse(self.phonebook.is_consistent())

	def test_is_consistent_with_duplicate_prefixes(self):
		self.phonebook.add("Sita","98998")
		self.phonebook.add("Geeta","9899")
		self.assertFalse(self.phonebook.is_consistent())

	# Skipping a testcase
	@unittest.skip("WIP")
	def test_empty_phonebook_lol_is_consistent(self):
		self.assertTrue(self.phonebook.is_consistent())