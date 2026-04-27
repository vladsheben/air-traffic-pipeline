import sqlite3
import logging

logger = logging.getLogger(__name__)


def create_db_connect():
    """
    Stellt eine Verbindung zur SQLite-Datenbank her und konfiguriert Leistungsparameter.

    Beinhaltet:
        - WAL-Modus und NORMALE Synchronisierung (5- bis 20-fache Schreibgeschwindigkeit).
        - Unterstützung für Fremdschlüssel (Foreign Keys), die in SQLite standardmäßig deaktiviert ist.
    """
    try:
        conn = sqlite3.connect("data/etl_rapid.db")

        conn.execute("PRAGMA journal_mode=WAL")
        conn.execute("PRAGMA synchronous=NORMAL")
        conn.execute("PRAGMA foreign_keys = ON")

        logger.info("SQLite-Verbindung erfolgreich mit FK- und WAL-Unterstützung hergestellt.")
        return conn

    except sqlite3.Error as e:
        logger.error("SQLite-Verbindungsfehler: %s", e)
        raise
    except sqlite3.OperationalError as e:
        logger.error("Fehler beim Herstellen der Verbindung: %s", e)
        raise
    except Exception as e:
        logger.error("Unerwarteter Fehler beim Herstellen der Verbindung: %s", e)
        raise


def create_table(conn):
    """
    Erstellt die Datenbankstruktur (Airlines, Airports, Flights).

    Strukturmerkmale:
    - Verwendet UNIQUE für Fluggesellschafts- und Flughafencodes.
    - Zusammengesetzter UNIQUE-Index für Flüge zur Vermeidung von Duplikaten.
    - Fremdschlüssel (FK)
    """
    try:
        cursor = conn.cursor()

        cursor.execute("""
        CREATE TABLE IF NOT EXISTS airlines (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            airline_code TEXT UNIQUE,
            airline_name TEXT NOT NULL,
            country TEXT
        )
        """)

        cursor.execute("""
        CREATE TABLE IF NOT EXISTS airports (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            iata_code TEXT UNIQUE
        )
        """)

        cursor.execute("""
        CREATE TABLE IF NOT EXISTS flights (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            airport_id INTEGER NOT NULL,
            airline_id INTEGER NOT NULL,
            flight_number TEXT NOT NULL,
            flight_origin_country TEXT,
            arrival_year TEXT NOT NULL,
            arrival_month TEXT NOT NULL,
            arrival_day TEXT NOT NULL,
            arrival_hour TEXT NOT NULL,
            arrival_minute TEXT NOT NULL,
            arrival_second TEXT,

            UNIQUE(
                airport_id,
                flight_number,
                arrival_year,
                arrival_month,
                arrival_day,
                arrival_hour,
                arrival_minute
            ),

            FOREIGN KEY (airport_id) REFERENCES airports(id) ON DELETE CASCADE,
            FOREIGN KEY (airline_id) REFERENCES airlines(id) ON DELETE SET NULL
        )
        """)

        logger.info("Die SQLite-Tabelle wurde erfolgreich erstellt oder existiert bereits.")

    except sqlite3.Error as e:
        logger.error("Fehler beim Erstellen der Tabelle: %s", e)
        raise
    except Exception as e:
        logger.error("Unerwarteter Fehler beim Erstellen der Tabelle: %s", e)
        raise