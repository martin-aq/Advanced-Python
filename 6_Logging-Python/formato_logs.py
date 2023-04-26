import logging

logging.basicConfig(
    level=logging.DEBUG,
    format="%(asctime)s - %(levelname)s - %(message)s",
    datefmt="%H:%M:%S"
)

nombre = "Paco"
logging.error(f"{nombre} creo el error")

logging.warning("Log de advertencia")
logging.error("Log de error")
logging.critical("Log de error critico")

try:
    division = 2 / 0
except:
    logging.exception("Division por cero")