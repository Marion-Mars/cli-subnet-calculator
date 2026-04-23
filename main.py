import click
from subnet_calc.core import get_subnet_info
from subnet_calc.formatter import display_subnet_info


@click.command()
@click.argument("network")
@click.option("--split", default=None)
def cli(network, split):
    result = get_subnet_info(network)
    display_subnet_info(result)
