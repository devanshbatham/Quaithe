#!/usr/bin/env python3


import argparse
import concurrent.futures
import subprocess
import sys
import logging
from alive_progress import alive_bar
from datetime import datetime


def process_command(command, silent):
    """
    Execute a given command in a subprocess.

    Args:
        command (str): The command to execute.
        silent (bool): Whether to suppress command output.

    Raises:
        subprocess.CalledProcessError: If the command returns a non-zero exit code.
    """
    try:
        if silent:
            subprocess.run(
                command, shell=True, check=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL
            )
        else:
            subprocess.run(command, shell=True, check=True)
    except subprocess.CalledProcessError as e:
        logging.error(f'Error running command {command}: {e}')


if __name__ == "__main__":
    # Set up logging
    logging.basicConfig(level=logging.INFO, format="[%(asctime)s] %(message)s", datefmt="%Y-%m-%d %H:%M:%S")
    logger = logging.getLogger(__name__)

    # Parse command-line arguments
    parser = argparse.ArgumentParser(description="Run commands in parallel")
    parser.add_argument(
        "-w",
        type=int,
        default=7,
        help="Number of worker processes to use (default: 7)",
    )
    parser.add_argument(
        "-silent",
        action="store_true",
        help="Silent mode: suppress command output",
    )
    args = parser.parse_args()

    # Read commands from standard input
    commands = sys.stdin.read().splitlines()
    num_commands = len(commands)

    # Begin execution
    logger.info("Let the show begin!")

    try:
        with concurrent.futures.ThreadPoolExecutor(max_workers=args.workers) as executor:
            # Submit commands to executor and track futures
            futures = [
                executor.submit(process_command, command, args.silent)
                for command in commands
            ]
            # Display progress bar while commands are executing
            with alive_bar(num_commands) as progress_bar:
                for future in concurrent.futures.as_completed(futures):
                    # Check for exceptions in futures
                    if future.exception() is not None:
                        logger.error(f"Error processing command: {future.exception()}")
                    progress_bar()
    except Exception as e:
        logger.error(f"An error occurred: {e}")
        sys.exit(1)

    # Execution complete
    logger.info("That's a wrap!")
