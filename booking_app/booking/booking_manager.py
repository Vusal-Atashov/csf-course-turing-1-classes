
def create_booking_details():
    booking_details = {}
    booking_details['id'] = input("Enter Booking ID: ")
    booking_details['passenger_name'] = input("Enter Passenger Name: ")
    booking_details['flight_id'] = input("Enter Flight ID: ")
    booking_details['seat_count'] = input("Enter Number of Seats: ")

    return booking_details

