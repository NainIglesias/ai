"""Descarga la SMS Spam Collection una vez y la carga como un DataFrame."""

import csv
import io
import urllib.request
import zipfile
from pathlib import Path

import pandas as pd

SOURCE_URL = "https://archive.ics.uci.edu/static/public/228/sms+spam+collection.zip"
DATA_FILE = Path(__file__).parent / "data" / "SMSSpamCollection"


def load_sms_spam() -> pd.DataFrame:
    """Devuelve una fila por mensaje, con las columnas `label` ("ham" o "spam") y `message`."""
    if not DATA_FILE.exists():
        DATA_FILE.parent.mkdir(exist_ok=True)
        with urllib.request.urlopen(SOURCE_URL) as response:
            archive = zipfile.ZipFile(io.BytesIO(response.read()))
        DATA_FILE.write_bytes(archive.read("SMSSpamCollection"))
    # Los mensajes contienen comillas que no delimitan campos, así que se desactiva el entrecomillado.
    return pd.read_csv(DATA_FILE, sep="\t", names=["label", "message"], quoting=csv.QUOTE_NONE, encoding="utf-8")
