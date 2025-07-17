import re
import matplotlib.pyplot as plt
import sys


def parse_and_plot(filename):
    """
    Parse the given file for lines starting with 'pages size:',
    extract demo_size and promo_size, sum them, and plot the result.
    """
    # This list will hold the sum of demo_size + promo_size for each valid line
    sums = []

    # Compile a regex pattern for efficiency (optional)
    pattern = re.compile(r"demo_size:\s*(\d+).*promo_size:\s*(\d+)")

    with open(filename, "r", encoding="utf-8") as f:
        for line in f:
            # Check if the line starts with 'pages size:'
            if line.startswith("pages size:"):
                match = pattern.search(line)
                if match:
                    demo_size = int(match.group(1))
                    promo_size = int(match.group(2))
                    sums.append(demo_size + promo_size)

    print(sums)
    # Plot the values
    plt.figure(figsize=(10, 6))
    plt.plot(sums, marker='o')
    # plt.title("Sum of demo_size and promo_size Over Lines")
    plt.xlabel("Program Executes")
    plt.ylabel("# Migrated Pages")
    plt.grid(True)
    plt.savefig("out.png")


if __name__ == "__main__":
    # Replace 'path_to_your_file.txt' with the actual path to your log/input file
    file_name = sys.argv[1]
    parse_and_plot(file_name)
