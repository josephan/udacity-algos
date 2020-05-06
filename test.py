def min_platforms(arrival, departure):
    """
    :param: arrival - list of arrival time
    :param: departure - list of departure time
    TODO - complete this method and return the minimum number of platforms (int) required
    so that no train has to wait for other(s) to leave
    """
    max_trains = 0
    current_trains = 0
    a_index = 0
    d_index = 0
    while a_index < len(arrival) or d_index < len(departure):
        print('arrival index:', a_index)
        print('arrival length:', len(arrival))
        print('departure index:', d_index)
        print('departure length:', len(departure))
        # step through arrival/departure
        # update current train and max train as we go
        if a_index == len(arrival):
            d_index += 1
            current_trains -= 1
        if d_index == len(arrival):
            a_index += 1
            current_trains += 1
            
        next_arrival = arrival[a_index]
        next_departure = departure[d_index]
        __import__('pdb').set_trace()
        
        if next_arrival == next_departure:
            d_index += 1
            a_index += 1
        elif next_arrival < next_departure:
            a_index += 1
            current_trains += 1
        elif next_arrival > next_departure:
            d_index += 1
            current_trains -= 1
        
        if current_trains > max_trains:
            max_trains = current_trains
    
    return max_trains

def test_function(test_case):
    arrival = test_case[0]
    departure = test_case[1]
    solution = test_case[2]
    
    output = min_platforms(arrival, departure)
    if output == solution:
        print("Pass")
    else:
        print("Fail")

arrival = [900,  940, 950,  1100, 1500, 1800]
departure = [910, 1200, 1120, 1130, 1900, 2000]
test_case = [arrival, departure, 3]

test_function(test_case)
