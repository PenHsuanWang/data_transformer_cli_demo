"""
CLI application for the Titanic data processing project.
"""

import click
from src.data_loader import load_data
from src.data_processor import process_data
# import pandas as pd

@click.group()
def cli():
    """Entry point for the CLI."""
    pass

@click.command()
@click.argument('file_path')
def load(file_path):
    """Load the data from the given file path.

    :param file_path: The path to the CSV file containing Titanic data.
    :type file_path: str
    """
    try:
        data = load_data(file_path)
        click.echo(f"Data loaded successfully from {file_path}")
        click.echo(data.head())
    except Exception as e:
        click.echo(f"Error: {e}")

@click.command()
@click.argument('file_path')
@click.argument('output_path')
def process(file_path, output_path):
    """Process the data from the given file path and save to output path.

    :param file_path: The path to the CSV file containing Titanic data.
    :type file_path: str
    :param output_path: The path where the processed data will be saved.
    :type output_path: str
    """
    try:
        data = load_data(file_path)
        processed_data = process_data(data)
        processed_data.to_csv(output_path, index=False)
        click.echo(f"Data processed successfully and saved to {output_path}")
    except Exception as e:
        click.echo(f"Error: {e}")


cli.add_command(load)
cli.add_command(process)

if __name__ == '__main__':
    cli()
