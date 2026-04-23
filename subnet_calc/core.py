import ipaddress


def get_subnet_info(network):
    try:
        ip_network = ipaddress.IPv4Network(network, strict=False)

    except ValueError:
        return {
            "error": "Please make sure you enter your ip with the slash mask e.g. 192.168.0.0/23"
        }

    ipadd = network.split("/")[0]
    network_address = str(ip_network.network_address)
    if ipadd != str(ip_network.network_address):
        warning = "Entered IP is a host, converted to network base"
    else:
        warning = None

    first_octet = int(str(ip_network.network_address).split(".")[0])
    if first_octet <= 126:
        ip_class = "A"
    elif first_octet <= 191:
        ip_class = "B"
    else:
        ip_class = "C"

    hosts = list(ip_network.hosts())
    return {
        "network_address": str(ip_network.network_address),
        "broadcast_address": str(ip_network.broadcast_address),
        "netmask": str(ip_network.netmask),
        "wildcard": str(ip_network.hostmask),
        "prefixlen": ip_network.prefixlen,
        "total_hosts": 2 ** (32 - ip_network.prefixlen),
        "usable_hosts": len(hosts),
        "first_usable": str(hosts[0]),
        "last_usable": str(hosts[-1]),
        "ip_class": ip_class,
        "is_private": (ipaddress.IPv4Address(ip_network.network_address).is_private),
        "warning": warning,
    }
