import mysql.connector  # type: ignore


class DB:
    def __init__(self):
        try:
            self.conn = mysql.connector.connect(
                host="127.0.0.1", user="root", password="", database="flight_dashboard"
            )
            self.mycursor = self.conn.cursor()
            print("Connection established")

        except Exception:
            print("Connection error")

    def fetch_city_name(self):
        city = []
        self.mycursor.execute(
            """
            SELECT DISTINCT(Source) FROM flights_cleaned
            UNION
            SELECT DISTINCT(Destination) FROM flights_cleaned
            """
        )

        data = self.mycursor.fetchall()

        for item in data:
            city.append(item[0])

        return city

    def fetch_all_flights(self, source, destination):
        self.mycursor.execute(
            """
        SELECT Airline, Route, Dep_Time, Duration, Price FROM flights_cleaned
        WHERE Source = '{}' AND Destination = '{}'
        """.format(
                source, destination
            )
        )

        data = self.mycursor.fetchall()
        return data

    def fetch_airline_frequency(self):

        airline = []
        frequency = []
        self.mycursor.execute(
            """
        SELECT Airline, COUNT(*) AS 'no_of_flight' FROM flights_cleaned
        GROUP BY Airline
        """
        )

        data = self.mycursor.fetchall()
        for item in data:
            airline.append(item[0])
            frequency.append(item[1])

        return airline, frequency

    def busy_airport(self):
        self.mycursor.execute(
            """
        SELECT Source, COUNT(*) FROM (
            SELECT Source FROM flights_cleaned
            UNION ALL
            SELECT Destination FROM flights_cleaned
        ) t
        GROUP BY t.Source
        ORDER BY COUNT(*) DESC
        """
        )

        city = []
        frequency = []

        data = self.mycursor.fetchall()
        for item in data:
            city.append(item[0])
            frequency.append(item[1])

        return city, frequency

    def daily_frequency(self):
        self.mycursor.execute(
            """
        SELECT Date_of_Journey, COUNT(*) FROM flights_cleaned
        GROUP BY Date_of_Journey 
        """
        )

        date = []
        frequency = []

        data = self.mycursor.fetchall()
        for item in data:
            date.append(item[0])
            frequency.append(item[1])

        return date, frequency
