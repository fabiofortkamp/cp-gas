"""Command-line interface."""
import click


@click.command()
@click.version_option()
def main() -> None:
    """Correlations for Specific Heat of Gases."""


if __name__ == "__main__":
    main(prog_name="cp-gas")  # pragma: no cover
