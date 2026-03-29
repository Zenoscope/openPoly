"""
This is the performance test code.
Add in the additional code to test both search algorithms and with the required test data
"""

import csv
import time

from storage import PurchaseOrdersBT, PurchaseOrdersLL


def perform_search(data, number):
    start_time = time.perf_counter()
    record = data.search_by_number(number)
    end_time = time.perf_counter()
    elapsed = (end_time - start_time) * 1000
    if record is None:
        print(f"Purchase order {number} missing: {elapsed:0.3f} milliseconds")
    else:
        print(f"Purchase order {number} found: {elapsed:0.3f} milliseconds")


if __name__ == "__main__":
    # Load the data
    data = PurchaseOrdersLL()  # Change to the relevant data structure
    with open("unsorted_orders.csv") as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=",")
        for row in csv_reader:
            data.add(row[0], row[1])

    # Test the performance of the algorithm with the test values
    perform_search(data, 14308662)
