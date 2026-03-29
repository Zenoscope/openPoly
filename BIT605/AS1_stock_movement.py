"""
###########################################################################################################
Algorithm 1
Stock movement
"""


def print_move(count, item, from_site, to_site):
    print(f"{count}: Moving item #{item} from {from_site} to {to_site}")
    count += 1


def stock_moving_algorithm_1(number_of_items, location_1, location_2, location_3):
    return stock_moving_algorithm_1_inner(
        0, number_of_items, location_1, location_3, location_2
    )


def stock_moving_algorithm_1_inner(
    count, number_of_items, from_location, to_location, temp_location
):

    if number_of_items == 0:
        return count

    count = stock_moving_algorithm_1_inner(
        count, number_of_items - 1, from_location, temp_location, to_location
        )
    count += 1

    print_move(count, number_of_items, from_location, to_location)

    count = stock_moving_algorithm_1_inner(
        count, number_of_items - 1, temp_location, to_location, from_location
    )
    return count
   # O(1) - no loops, though there are things moving

"""
###########################################################################################################
    Algorithm 2
    Stock movement    
"""

def move_item(count, location_1, location_1_data, location_2, location_2_data):
    if len(location_1_data) == 0:
        item = location_2_data.pop()
        print_move(count, item, location_2, location_1)
        location_1_data.append(item)
    elif len(location_2_data) == 0:
        item = location_1_data.pop()
        print_move(count, item, location_1, location_2)
        location_2_data.append(item)
    elif location_1_data[-1] > location_2_data[-1]:
        item = location_2_data.pop()
        print_move(count, item, location_2, location_1)
        location_1_data.append(item)
    else:
        item = location_1_data.pop()
        print_move(count, item, location_1, location_2)
        location_2_data.append(item)

def stock_moving_algorithm_2(number_of_items, location_1, location_2, location_3):
    if number_of_items % 2 == 0:
        # If we have an even number of items, we need to swap the last two locations
        temp = location_2
        location_2 = location_3
        location_3 = temp

    # Calculate the number of moves we need to make
    total_number_of_moves = int(pow(2, number_of_items) - 1)

    # Initialize the three locations and add all the items to the first location
    location_1_data = []
    location_2_data = []
    location_3_data = []
    for loop in range(number_of_items, 0, -1):
        location_1_data.append(loop)

    # Move the items between each location
    for loop in range(1, total_number_of_moves + 1):
        match loop % 3:
            case 1:
                move_item(
                    loop, location_1, location_1_data, location_3, location_3_data
                )

            case 2:
                move_item(
                    loop, location_1, location_1_data, location_2, location_2_data
                )

            case 0:
                move_item(
                    loop, location_2, location_2_data, location_3, location_3_data
                )

    return total_number_of_moves
    # O(N2)  as there are two loops


if __name__ == "__main__":
    number_of_items = 3
    count = stock_moving_algorithm_1(
        number_of_items, "Factory 1", "Factory 2", "Warehouse"
    )

    count = stock_moving_algorithm_2(
        number_of_items, "Factory 1", "Factory 2", "Warehouse"
    )
