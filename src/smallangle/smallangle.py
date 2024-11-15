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
    help="Gives the user the control to decide the amount of steps.",
    show_default=True,
)

def sin(number):
    x = np.linspace(0, 2 * pi, number)
    df = pd.DataFrame({"x": x, "sin (x)": np.sin(x)})
    print(df)

@cmd_group.command()
@click.option(
    "--number",
    "-n",
    default=10,
    help="Gives the user the control to decide the amount of steps.",
    show_default=True,
)
def tan(number):
    x = np.linspace(0, 2 * pi, number)
    df = pd.DataFrame({"x": x, "tan (x)": np.tan(x)})
    print(df)


if __name__ == "__main__":
    cmd_group()