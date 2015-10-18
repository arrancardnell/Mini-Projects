__author__ = 'Arran'

import csv


class Parse:

    def __init__(self):
        self.MY_FILE = "C:\\Users\\Arran\\Documents\\GitHub\\My-Projects\\DataVisualisation\\sample_sfpd_incident_all.csv"

    def parse(self, raw_file, delimiter):
        """Parses a raw CSV file to a JSON-like object."""

        # Open CSV file
        opened_file = open(raw_file, newline='\n')

        # Read CSV file
        csv_data = csv.reader(opened_file, delimiter=delimiter)

        # Setup an empty list
        parsed_data = []

        # Skip over the first line of the file for the headers
        fields = next(csv_data)

        # Iterate over each row of the csv file, zip together field -> value
        for row in csv_data:
            parsed_data.append(dict(zip(fields, row)))

        # Close the CSV file
        opened_file.close()

        return parsed_data

    def main(self):

        # Call our parse function and give it the needed parameters
        new_data = self.parse(self.MY_FILE, ",")

        return new_data