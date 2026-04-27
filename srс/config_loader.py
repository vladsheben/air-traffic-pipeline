import json
import logging
from pathlib import Path

CONFIG_JSON = Path(__file__).parent.parent / "config" / "etl_config.json"

logger = logging.getLogger(__name__)


def load_config() -> dict:
    '''
    Lädt die ETL-Konfiguration aus der JSON-Datei.

    Ein Konfigurations-Dictionary, das Folgendes enthalten muss:
        - "api_key": Der Name der Umgebungsvariable, die den RapidAPI-Schlüssel enthält.
        - "airports": Eine Liste von Strings (IATA-Codes, z. B. ["TXL", "MUC"]).
    '''
    try:
        with open(CONFIG_JSON, mode="r", encoding="UTF-8") as file:
            myconfig = json.load(file)
            logger.info("Konfigurationsdatei geladen")
            return myconfig
    except FileNotFoundError:
        logger.error(f"Konfigurationsdatei nicht gefunden!: {CONFIG_JSON}")
        raise
    except json.JSONDecodeError as e:
        logger.error(f"Ungültiges JSON in Konfigurationsdatei: {e}")
        raise
    except Exception as e:
        logger.error(f"Unerwarteter Fehler beim Laden der Konfiguration: {e}")
        raise