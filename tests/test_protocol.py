import pytest
from ccmc.protocol import StorageCommand, serialize_get, parse_storage_response, parse_get_response

def test_storage_command_serialize():
    cmd = StorageCommand("set", "foo", 0, 0, 3, b"bar")
    expected = b"set foo 0 0 3\r\nbar\r\n"
    assert cmd.serialize() == expected

def test_serialize_get():
    msg = serialize_get(["foo", "bar"])
    assert msg == b"get foo bar\r\n"

def test_parse_storage_response():
    assert parse_storage_response("STORED\r\n") == "STORED"
    assert parse_storage_response("NOT_STORED\r\n") == "NOT_STORED"

def test_parse_get_response():
    raw = b"VALUE foo 0 3\r\nbar\r\nEND\r\n"
    result = parse_get_response(raw)
    assert "foo" in result
    flags, value = result["foo"]
    assert flags == 0
    assert value == b"bar"