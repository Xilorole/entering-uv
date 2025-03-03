import os
import random
import secrets
import signal
import sys
import time

import click
from loguru import logger


@click.group()
def cli() -> None:
    """Command Line Interface (CLI) entry point for the tool.

    This function serves as the main entry point for the CLI of the tool.
    It is intended to handle user inputs and execute the appropriate
    commands based on those inputs.
    Currently, this function is a placeholder and does not perform any
    operations.
    """


@cli.command()
def hello() -> None:
    """Log a greeting message."""
    logger.info("hi, there")

@cli.command()
def christmas() -> None:
    """Shows a Christmas tree animation and adapts if the terminal size changes."""
    logger.info("Merry Christmas!")

    def clear():
        os.system("cls" if os.name == "nt" else "clear")

    def print_at(row, col, text, color_code=""):
        sys.stdout.write(f"\033[{row};{col}H{color_code}{text}\033[0m")
        sys.stdout.flush()

    def exit_gracefully(signum, frame):
        clear()
        sys.stdout.write("\033[?25h")
        sys.stdout.flush()
        sys.exit(0)

    signal.signal(signal.SIGINT, exit_gracefully)

    def draw_tree_and_trunk():
        nonlocal lin
        clear()
        sys.stdout.write("\033[?25l")
        sys.stdout.flush()

        # Recalculate everything for new size
        current_size = os.get_terminal_size()
        lines_available, cols_available = current_size.lines, current_size.columns
        tree_height = int(lines_available / 2.5)
        trunk_width = 3
        trunk_height = tree_height // 6

        # Draw tree
        new_lin = (lines_available - tree_height) // 2
        center_col = cols_available // 2
        GREEN = "\033[32m"
        RED_BOLD = "\033[31;1m"
        BROWN = "\033[33m"

        for i in range(1, tree_height * 2, 2):
            print_at(new_lin, center_col - i // 2, "*" * i, GREEN)
            new_lin += 1

        # Draw trunk
        trunk_col = center_col - trunk_width // 2
        for i in range(trunk_height):
            print_at(new_lin + i, trunk_col, "mWm", BROWN)
        new_lin += trunk_height

        # Show message
        new_year = time.localtime().tm_year
        print_at(new_lin, center_col - 7, "MERRY CHRISTMAS", RED_BOLD)
        print_at(new_lin + 1, center_col - 11, f"And lots of CODE in {new_year}", RED_BOLD)

        return (new_lin, center_col, lines_available, cols_available, tree_height)

    lin = 0
    (lin, col, prev_lines, prev_cols, tree_height) = draw_tree_and_trunk()

    k = 1
    lines_dict = {}
    columns_dict = {}
    start_line = (prev_lines - tree_height) // 2

    while True:
        current_lines, current_cols = os.get_terminal_size()
        if current_lines != prev_lines or current_cols != prev_cols:
            (lin, col, prev_lines, prev_cols, tree_height) = draw_tree_and_trunk()
            lines_dict.clear()
            columns_dict.clear()
            start_line = (prev_lines - tree_height) // 2

        for i in range(35):
            if k > 1:
                prev_key = (k - 1, i)
                if prev_key in lines_dict:
                    print_at(lines_dict[prev_key], columns_dict[prev_key], "*", "\033[32m")
                    del lines_dict[prev_key]
                    del columns_dict[prev_key]
            li = secrets.randbelow(tree_height - 1) + start_line + 1
            start = col - li + start_line + 1
            co = secrets.randbelow(li - start_line) * 2 + start
            color = secrets.randbelow(7)
            sys.stdout.write(f"\033[1;3{color}m")
            print_at(li, co, "o")
            lines_dict[(k, i)] = li
            columns_dict[(k, i)] = co
            sh = 1
            for l in "CODE":
                color = secrets.randbelow(7)
                sys.stdout.write(f"\033[1;3{color}m")
                print_at(lin + 1, col + sh, l)
                sh += 1
                time.sleep(0.01)
        k = k % 2 + 1
