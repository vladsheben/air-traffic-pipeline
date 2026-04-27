from datetime import datetime
import logging

logger = logging.getLogger(__name__)


def parse_json(conn, data):
    """
    Wandelt rohe JSON-Flugdaten in ein für die Datenbank geeignetes Format um.
    """
    flights_data = []

    for airport, data_airport in data.items():
        if not data_airport:
            continue

        movements = data_airport.get("departures", []) + data_airport.get("arrivals", [])

        for mov in movements:
            try:
                flight_number = mov.get("number") or "N/A"

                arrival_section = mov.get("arrival")
                if not arrival_section:
                    continue

                arrival_time_str = (
                    arrival_section.get("revisedTime", {}).get("utc") or
                    arrival_section.get("scheduledTime", {}).get("utc")
                )

                if not arrival_time_str:
                    continue

                dt = datetime.fromisoformat(arrival_time_str.replace('Z', '+00:00'))

                flights_data.append((
                    airport,
                    flight_number,
                    f"{dt.year}",
                    f"{dt.month:02d}",
                    f"{dt.day:02d}",
                    f"{dt.hour:02d}",
                    f"{dt.minute:02d}",
                    f"{dt.second:02d}",
                ))

            except Exception as e:
                logger.warning(f"Fehler beim Parsen: {e}")

    return flights_data