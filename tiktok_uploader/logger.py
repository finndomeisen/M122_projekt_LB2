import logging

def setup_logger():
    logging.basicConfig(
        filename="log.txt",
        level=logging.INFO,
        format="%(asctime)s - %(levelname)s - %(message)s"
    )

