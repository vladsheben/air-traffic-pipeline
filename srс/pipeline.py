from config_loader import load_config
from db import create_db_connect, create_table
from extract import request_api_data
from transform import parse_json
from load import save_to_db


def run_pipeline():
    """
    Der primäre Einstiegspunkt in den ETL-Prozess.
    Koordiniert die Extraktion, Transformation und das Laden von Daten.
    """

    myconfig = load_config()

    conn = create_db_connect()
    create_table(conn)

    data = request_api_data(myconfig)

    flights_data = parse_json(conn, data)

    if flights_data:
        save_to_db(conn, flights_data)

    conn.close()