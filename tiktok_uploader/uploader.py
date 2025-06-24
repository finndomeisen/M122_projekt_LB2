import configparser
import datetime

def load_config():
    config = configparser.ConfigParser()
    config.read("config.cfg")
    return config["UPLOAD"]

def prepare_upload(config):
    today = datetime.date.today().strftime("%d.%m.%Y")
    description = config["description"].replace("{date}", today)
    return {
        "video": config["video_path"],
        "description": description,
        "hashtags": config["hashtags"],
        "sound": config["sound"],
        "token": config["token"]
    }

def upload_to_tiktok(upload_data):
    # Hier würdet ihr `selenium` oder eine API verwenden.
    # Das ist nur ein Platzhalter.
    print("Video wird hochgeladen...")
    print(f"Pfad: {upload_data['video']}")
    print(f"Beschreibung: {upload_data['description']}")
    print(f"Hashtags: {upload_data['hashtags']}")
    print(f"Sound: {upload_data['sound']}")
    print("✅ Upload erfolgreich!")

