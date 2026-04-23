from rich.table import Table
from rich.console import Console


def display_subnet_info(subnet_data):
    if "error" in subnet_data:
        print(subnet_data["error"])
        return

    if "warning" in subnet_data and subnet_data["warning"] is not None:
        print(subnet_data["warning"])

    table = Table(title="Subnet Information")
    table.add_column("Property")
    table.add_column("Value")
    table.add_row("Network Address", subnet_data["network_address"])
    table.add_row("Broadcast Address", subnet_data["broadcast_address"])
    table.add_row("Subnet Mask", subnet_data["netmask"])
    table.add_row("Wildcard", subnet_data["wildcard"])
    table.add_row("Prefix Length", str(subnet_data["prefixlen"]))
    table.add_row("First Usable", subnet_data["first_usable"])
    table.add_row("Last Usable", subnet_data["last_usable"])
    table.add_row("Total Hosts", str(subnet_data["total_hosts"]))
    table.add_row("Usable Hosts", str(subnet_data["usable_hosts"]))
    table.add_row("IP Class", subnet_data["ip_class"])
    table.add_row("Private", str(subnet_data["is_private"]))

    console = Console()
    console.print(table)
