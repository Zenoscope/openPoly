"""
This is the performance test code.
add in the additional code to test both storage algorithms and with the required test data
"""

import csv
import time

from AS1_storage import PurchaseOrdersLL


def measure_performance(data):
    data = PurchaseOrdersLL()  # Change to PurchaserOrderBT when needed
    start_time = time.perf_counter()
    count = 0
    for row in csv_reader:
        data.add(row[0], row[1])
        count += 1
    end_time = time.perf_counter()
    print(f"Added {count} records in {end_time - start_time:0.3f} seconds")


if __name__ == "__main__":
    with open("AS1_unsorted_orders.csv") as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=",")

        # Test the performance of the algorithm
        measure_performance(csv_reader)
