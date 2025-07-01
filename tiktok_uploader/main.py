import time
import logging
from datetime import datetime
from uploader import load_config, prepare_upload, upload_to_tiktok
from logger import setup_logger

CONFIG_PATH = "config.cfg"


def main():
    setup_logger()
    config = load_config()
    upload_time = config["upload_time"]

    logging.info(f"⏳ Warte auf Upload-Zeit: {upload_time}")

    while True:
        now = datetime.now().strftime("%H:%M")
        if now == upload_time:
            try:
                upload_data = prepare_upload(config)
                upload_to_tiktok(upload_data)
                logging.info("✅ Upload abgeschlossen.")
                break
            except Exception as e:
                logging.error(f"❌ Fehler beim Upload: {e}")
                break
        else:
            time.sleep(30)


if __name__ == "__main__":
    main()
    
    


