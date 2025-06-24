import time
import logging
from datetime import datetime
from uploader import load_config, prepare_upload, upload_to_tiktok
from hash_check import is_file_unchanged
from logger import setup_logger

CONFIG_PATH = "config.cfg"
EXPECTED_HASH = "DEIN_ERWARTETER_HASHWERT"  # später einfügen

def main():
    setup_logger()
    if not is_file_unchanged(CONFIG_PATH, EXPECTED_HASH):
        logging.error("❌ Konfigurationsdatei wurde verändert!")
        return

    config = load_config()
    now = datetime.now().strftime("%H:%M")
    if now == config["upload_time"]:
        try:
            upload_data = prepare_upload(config)
            upload_to_tiktok(upload_data)
            logging.info("✅ Upload erfolgreich durchgeführt.")
        except Exception as e:
            logging.error(f"❌ Fehler beim Upload: {e}")
    else:
        print(f"⏳ Noch nicht Zeit: Aktuell ist {now}")

if __name__ == "__main__":
    main()

