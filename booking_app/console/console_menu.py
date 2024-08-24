from booking_app.booking.booking_manager import create_booking_details
from booking_app.booking.booking_postgres import save_booking, find_all
from booking_app.flight.flight_manager import create_flight_details
from booking_app.flight.flight_postgres import save_flight
from booking_app.config import postgres_connection


def console_menu():
    print("-"*30)
    print("Please choose an option:")
    print("1. Create a new flight")
    print("2. Create a new booking")
    print("3. Get all bookings")
    print("4. Exit")
    choice = input("Enter your choice: ")
    return choice


def main():
    print("Welcome to the Booking App!")
    choice = console_menu()
    postgres = postgres_connection.connect_to_database()
    while choice != '4':
        if choice == '1':
            flight_details = create_flight_details()
            save_flight(flight_details, postgres)
        elif choice == '2':
            booking_details = create_booking_details()
            save_booking(booking_details, postgres)
        elif choice == '3':
            bookings = find_all(postgres)
            for booking in bookings:
                print(booking)
        elif choice == '4':
            break
        else:
            print("Invalid choice. Please try again.")
        choice = console_menu()
    print("Exiting the Booking App. Goodbye!")
