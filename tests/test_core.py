import pytest
from subnet_calc.core import get_subnet_info


def test_valid_network():
    result = get_subnet_info("192.168.0.0/26")
    assert result["network_address"] == "192.168.0.0"
    assert result["netmask"] == "255.255.255.192"
    assert result["usable_hosts"] == 62


def test_host_address():
    result = get_subnet_info("192.168.0.5/26")
    assert result["warning"] != None


def test_invalid_input():
    result = get_subnet_info("hello")
    assert "error" in result
