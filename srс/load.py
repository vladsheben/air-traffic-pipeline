import logging

logger = logging.getLogger(__name__)


def save_to_db(conn, flights_data):
    """
    Speichert eine Liste von Flügen in der Tabelle 'flights'.
    Verwendet INSERT OR IGNORE, um Duplikate zu vermeiden.
    """
    try:
        cursor = conn.cursor()

        for f in flights_data:
            airport, flight_number, y, m, d, h, min_, sec = f

            cursor.execute("INSERT OR IGNORE INTO airports (iata_code) VALUES (?)", (airport,))
            cursor.execute("SELECT id FROM airports WHERE iata_code = ?", (airport,))
            airport_id = cursor.fetchone()[0]

            cursor.execute("""
            INSERT OR IGNORE INTO flights (
                airport_id,
                flight_number,
                arrival_year,
                arrival_month,
                arrival_day,
                arrival_hour,
                arrival_minute,
                arrival_second
            ) VALUES (?, ?, ?, ?, ?, ?, ?, ?)
            """, (airport_id, flight_number, y, m, d, h, min_, sec))

        conn.commit()
        logger.info("Flugdaten erfolgreich gespeichert")

    except Exception as e:
        logger.error(f"Fehler beim Speichern: {e}")
        raise