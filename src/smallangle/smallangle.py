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

@cmd_group.command()
@click.argument("epsilon", type=float)
def approx(epsilon):
    """Finds the largest x where the sin approximation for a given EPSILON does not hold anymore.

    EPSILON is the number (of type float) where | sin(x) - x | must be <= EPSILON.
    """
    x = 0
    while np.abs(np.sin(x) - x) <= epsilon:
        x += 0.001
    print(f"For an accuracy of {epsilon}, the small-angle approximation holds up to x = {round(x, 3)}.")



if __name__ == "__main__":
    cmd_group()