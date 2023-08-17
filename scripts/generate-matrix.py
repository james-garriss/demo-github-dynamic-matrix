"""Script to generate a matrix of random numbers."""
import os
import random


def get_random_int(lowest=0, highest=20):
    """Get a random integer in the provided range

    Args:
        lowest (int, optional): The lower bound. Defaults to 0.
        highest (int, optional): The upper bound. Defaults to 20.

    Returns:
        int: A random integer.
    """
    return random.randint(lowest, highest)


output_list = []
for i in range(5, get_random_int(15, 30)):
    output_list.append(get_random_int(lowest=1))

print("Dynamic matrix: " + str(output_list))

# Catch so this only runs in GitHub Actions
if "GITHUB_OUTPUT" in os.environ:
    # Write to GITHUB_OUTPUT
    with open(os.environ["GITHUB_OUTPUT"], "a") as fh:
        print(f"dynamic_list={str(output_list)}", file=fh)
