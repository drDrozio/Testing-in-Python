from phonebook import Phonebook 
import pytest

@pytest.fixture
def phonebook():
	phonebook = Phonebook()
	yield phonebook
	phonebook.clear()

	
def test_lookup_by_name(phonebook):
	phonebook.add("Alice","1234567890")
	assert "1234567890" == phonebook.lookup("Alice")

def test_all_names(phonebook):
	phonebook.add("Alice","1234567890")
	assert "Alice" in phonebook.names()

def test_missing_name_raises_error(phonebook):
	# phonebook.add("Alice","1234567890") # For fail case => Correct Code
	with pytest.raises(KeyError):
		phonebook.lookup("Alice")
