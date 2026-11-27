"""CLI script for the three_r_package package. This will be called on the command line"""


import click

from three_r_package.three_r_package import describe_numbers


@click.command()
@click.option(
    "--numbers",
    required=True,
    help="Comma-separated numbers, e.g. 10,20,30,40,50",
)
def three_r_package_cli(numbers):
    """Calculate descriptive statistics."""
    try:
        values = [float(x.strip()) for x in numbers.split(",")]
        results = describe_numbers(values)
    except ValueError as exc:
        raise click.BadParameter(
            str(exc), param_hint="--numbers"
        ) from exc

    click.echo("Descriptive Statistics")
    click.echo("-" * 30)

    for name, value in results.items():
        if name == "Count":
            click.echo(f"{name:<20}: {value}")
        else:
            click.echo(f"{name:<20}: {value:.2f}")
