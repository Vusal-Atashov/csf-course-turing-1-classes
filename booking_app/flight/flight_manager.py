

def create_flight_details():
    flight_details = {}
    flight_details['id'] = input("Enter Flight ID: ")
    flight_details['flight_number'] = input("Enter Flight Number: ")
    flight_details['date'] = input("Enter Flight Date (YYYY-MM-DD): ")
    flight_details['time'] = input("Enter Flight Time (HH:MM): ")
    flight_details['origin'] = input("Enter Origin: ")
    flight_details['destination'] = input("Enter Destination: ")
    flight_details['seats'] = input("Enter Number of Seats: ")
    return flight_details