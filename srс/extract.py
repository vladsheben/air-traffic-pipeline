import requests
import os
import time
import json
import logging
from dotenv import load_dotenv

load_dotenv()
logger = logging.getLogger(__name__)


def request_api_data(myconfig: dict) -> dict:
    """
    Diese Funktion iteriert durch eine Liste von IATA-Flughafencodes, sendet HTTP-Anfragen
    an RapidAPI, speichert die erhaltenen JSON-Antworten lokal im Dateisystem und
    gibt ein konsolidiertes Wörterbuch zurück.
    """

    API_KEY = os.getenv(myconfig["api_key"])
    if not API_KEY:
        logger.error("API-Schlüssel nicht in den Umgebungsvariablen gefunden.")
        raise ValueError("API-Schlüssel fehlt")

    airports = myconfig["airports"]
    results = {}

    for airport in airports:
        time.sleep(1)

        url = f"https://aerodatabox.p.rapidapi.com/flights/airports/iata/{airport}/2026-03-11T08:00/2026-03-11T12:00"

        headers = {
            "x-rapidapi-key": API_KEY,
            "x-rapidapi-host": "aerodatabox.p.rapidapi.com"
        }

        try:
            response = requests.get(url, headers=headers, timeout=10)
            response.raise_for_status()

            data = response.json()

            with open(f"data/result_{airport}.json", "w", encoding="utf-8") as f:
                json.dump(data, f, indent=4)

            results[airport] = data
            logger.info(f"Data für {airport} wurde gespeichert")

        except requests.RequestException as e:
            logger.error(f"Fehler bei der Flughafen {airport}: {e}")
        except Exception as unknown_error:
            logger.exception(f"Unbekannte Fehler für {airport}, {unknown_error}")

    return results