from booking_app.config import postgres_connection
from booking_app.booking import booking_manager

def save_booking(booking_details, conn):
    insert_query = """
    INSERT INTO public.bookings(id, passenger_name, flight_id, seat_count)
    VALUES (%s, %s, %s, %s)
    """
    with conn.cursor() as curr:
        try:
            curr.execute(insert_query, (
                booking_details['id'],
                booking_details['passenger_name'],
                booking_details['flight_id'],
                booking_details['seat_count']
            ))
            conn.commit()
        except Exception as e:
            print(f"Error: {e}")
            conn.rollback()
        finally:
            conn.close()


def find_all(conn):
    select_query = """
    SELECT
        b.id AS booking_id,
        b.passenger_name,
        b.seat_count,
        f.flight_number,
        f.date AS flight_date,
        f.time AS flight_time,
        f.origin,
        f.destination
    FROM
        public.bookings b
    JOIN
        public.flights f
    ON
        b.flight_id = f.id;
    """
    with conn.cursor() as curr:
        curr.execute(select_query)
        bookings = curr.fetchall()
        return bookings

if __name__ == '__main__':
    print(find_all())





