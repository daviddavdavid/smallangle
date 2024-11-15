import numpy as np
from numpy import pi
import pandas as pd
import click

@click.group()
def cmd_group():
    pass

@cmd_group.command()
@click.option(
    "--number",
    "-n",
    default=10,
)

def sin(number):
    """Runs the sin function for NUMBER amount of steps.

    NUMBER is the amount of steps.
    """
    x = np.linspace(0, 2 * pi, number)
    df = pd.DataFrame({"x": x, "sin (x)": np.sin(x)})
    print(df)

@cmd_group.command()
@click.option(
    "--number",
    "-n",
    default=10,
)
def tan(number):
    """Runs the tan command for NUMBER amount of steps.

    NUMBER is the amount of steps.
    """
    x = np.linspace(0, 2 * pi, number)
    df = pd.DataFrame({"x": x, "tan (x)": np.tan(x)})
    print(df)


if __name__ == "__main__":
    cmd_group()