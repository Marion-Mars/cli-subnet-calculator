from rich.tree import Tree
from rich.console import Console
import ipaddress


def display_subnet_tree(network, prefixlen):
    ip_network = ipaddress.IPv4Network(network, strict=False)
    tree = Tree(f"{ip_network.network_address}/{ip_network.prefixlen}")

    for subnet in ip_network.subnets(new_prefix=prefixlen):
        tree.add(f"{str(subnet)} Usable hosts:{len(list(subnet.hosts()))}")

    console = Console()
    console.print(tree)
