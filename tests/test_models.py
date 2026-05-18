import pytest

from source.modules.record import Record


def test_record_adds_valid_phone():
    record = Record("Anna")

    record.add_phone("4165551234")

    assert record.find_phone("4165551234") is not None


def test_record_rejects_invalid_phone():
    record = Record("Anna")

    with pytest.raises(ValueError):
        record.add_phone("123")


def test_record_adds_valid_email():
    record = Record("Anna")

    record.add_email("anna@example.com")

    assert record.email.value == "anna@example.com"


def test_record_rejects_invalid_email():
    record = Record("Anna")

    with pytest.raises(ValueError):
        record.add_email("not-an-email")


def test_record_adds_birthday():
    record = Record("Anna")

    record.manage_birthday("12.05.1990")

    assert record.birthday.value.day == 12
    assert record.birthday.value.month == 5
    assert record.birthday.value.year == 1990


def test_note_tags_are_added():
    record = Record("Anna")
    record.add_note("Call every Sunday")

    record.edit_note(["#family", "#important"])

    assert "#family" in record.note.value
    assert "#important" in record.note.value