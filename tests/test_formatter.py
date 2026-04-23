import pytest
from subnet_calc.formatter import display_subnet_info


def test_error_message(capsys):
    display_subnet_info(
        {
            "error": "Please make sure you enter your ip with the slash mask e.g. 192.168.0.0/23"
        }
    )
    captured = capsys.readouterr()
    assert (
        "Please make sure you enter your ip with the slash mask e.g. 192.168.0.0/23"
        in captured.out
    )


def test_warning_message(capsys):
    display_subnet_info(
        {
            "network_address": "192.168.0.0",
            "broadcast_address": "192.168.0.63",
            "netmask": "255.255.255.192",
            "wildcard": "0.0.0.63",
            "prefixlen": 26,
            "total_hosts": 64,
            "usable_hosts": 62,
            "first_usable": "192.168.0.1",
            "last_usable": "192.168.0.62",
            "ip_class": "C",
            "is_private": True,
            "warning": "Entered IP is a host, converted to network base",
        }
    )
    captured = capsys.readouterr()
    assert "Entered IP is a host, converted to network base" in captured.out


def test_valid_data(capsys):
    display_subnet_info(
        {
            "network_address": "192.168.0.0",
            "broadcast_address": "192.168.0.63",
            "netmask": "255.255.255.192",
            "wildcard": "0.0.0.63",
            "prefixlen": 26,
            "total_hosts": 64,
            "usable_hosts": 62,
            "first_usable": "192.168.0.1",
            "last_usable": "192.168.0.62",
            "ip_class": "C",
            "is_private": True,
            "warning": "Entered IP is a host, converted to network base",
        }
    )
    captured = capsys.readouterr()
    assert "192.168.0.0" in captured.out
