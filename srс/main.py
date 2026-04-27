"""
ETL-Pipeline: Flugdaten von europäischen Flughäfen via AeroDataBox API
=====================================================================

Extrahiert Flugbewegungen (Ankünfte + Abflüge) für gegebene IATA-Codes,
parst relevante Felder und speichert sie idempotent in SQLite.
"""

import logging.config
import os

os.makedirs("logs", exist_ok=True)

logging.config.fileConfig("config/logging_config.ini")

from pipeline import run_pipeline

if __name__ == "__main__":
    logging.info("Pipeline started")
    run_pipeline()


