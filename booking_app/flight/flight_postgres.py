
def save_flight(flight_details,conn):
    insert_query = """
    INSERT INTO public.flights(id, flight_number, date, time, origin, destination, seats)
    VALUES (%s, %s, %s, %s, %s, %s, %s)
    """
    cursor = conn.cursor()
    try:
        cursor.execute(insert_query, (
            flight_details['id'],
            flight_details['flight_number'],
            flight_details['date'],
            flight_details['time'],
            flight_details['origin'],
            flight_details['destination'],
            flight_details['seats']
        ))
        conn.commit()
    except Exception as e:
        print(f"Error: {e}")
        conn.rollback()
    finally:
        conn.close()

