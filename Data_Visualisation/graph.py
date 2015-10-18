__author__ = 'Arran'

import matplotlib.pyplot as plt
from collections import Counter
from parse import Parse

def visualise_days():
    """Visualise data by day of the week."""
    Parser = Parse()
    data_file = Parser.main()
    # Returns a dict where it sums the total values for each key.
    # In this case, the keys are the DaysOfWeek, and the values are
    # a count of incidents.
    counter = Counter(item["DayOfWeek"] for item in data_file)

    # Separate out the counter to order it correctly when plotting.
    data_list = [counter["Monday"],
                 counter["Tuesday"],
                 counter["Wednesday"],
                 counter["Thursday"],
                 counter["Friday"],
                 counter["Saturday"],
                 counter["Sunday"]
                 ]

    day_tuple = tuple(["Mon", "Tues", "Wed", "Thurs", "Fri", "Sat", "Sun"])

    # Assign the data to a plot
    plt.plot(data_list)

    # Assign labels to the plot
    plt.xticks(range(len(day_tuple)), day_tuple)

    # Save the plot!
    plt.savefig("Days.png")

    # Close figure
    plt.clf()

def main():
    visualise_days()

if __name__ == "__main__":
    main()