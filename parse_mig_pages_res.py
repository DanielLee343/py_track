import matplotlib.pyplot as plt


def parse_and_plot(filename):
    """
    Reads a file where each line contains several numeric values separated by ", ".
    Each line corresponds to one line in the chart.
    """
    data = []

    with open(filename, "r") as f:
        for line in f:
            line = line.strip()
            if not line:
                # Skip empty lines if any
                continue
            # Split by comma, remove extra spaces, and convert each to float
            values = [float(x.strip()) for x in line.split(",")]
            data.append(values)

    # print(data)
    # scale up the data by 10
    data = [[x * 10 for x in row] for row in data]
    # print(data)
    # exit(0)

    # We'll a
    # ssume there are exactly 4 lines in total
    # If your file has fewer or more lines, adjust accordingly
    if len(data) != 4:
        print("Warning: Expected 4 lines in the file, but found:", len(data))

    # Define 4 distinct colors for the 4 lines
    colors = ['red', 'blue', 'green', 'orange']

    plt.figure(figsize=(8, 4))
    labels = ["Summed Hotness", "Median Hotness",
              "Interval Mode Hotness", "Average Hotness"]

    # Plot each line with a different color
    for i, line_data in enumerate(data):
        plt.plot(line_data,
                 color=colors[i % len(colors)],
                 marker='o',
                 label=labels[i])

    plt.yticks(fontsize=13)
    plt.xlabel("Program Execution", fontsize=13)
    plt.ylabel("# Migrated Pages", fontsize=13)
    plt.xticks([])
    plt.legend(fontsize=13, loc='upper center')
    plt.grid(False)

    # Display the plot
    plt.savefig("representation.png")


if __name__ == "__main__":
    # Change 'my_data.txt' to the path of your own input file
    parse_and_plot("mig_pages_res.txt")
