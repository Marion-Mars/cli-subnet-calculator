import click


@click.command()
@click.argument("network")
@click.option("--split", default=None)
def cli(network, split):
    print(f"Calculating subnet info for: {network}")
