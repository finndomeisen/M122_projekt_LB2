import configparser
import datetime
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
import time
import os


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
        "sound": config["sound"]
    }

def upload_to_tiktok(upload_data):
    options = Options()
    options.add_experimental_option("detach", True)

    # 🧠 Hier gibst du deinen echten Chrome-Profilpfad an:
    # Ersetze diesen Pfad durch deinen tatsächlichen Benutzerordnerpfad:
    profile_path = r"C:\Users\Finn Domeisen\AppData\Local\Google\Chrome\User Data\Default"
    options.add_argument(f"--user-data-dir={profile_path}")
    options.add_argument("--profile-directory=Default")  # oder z. B. "Profile 1"

    driver_path = os.path.abspath("chromedriver.exe")
    service = Service(executable_path=driver_path)
    driver = webdriver.Chrome(service=service, options=options)

    driver.get("https://www.tiktok.com/upload")

    time.sleep(5)

    video_input = driver.find_element(By.XPATH, '//input[@type="file"]')
    abs_path = os.path.abspath(upload_data["video"])
    video_input.send_keys(abs_path)

    time.sleep(10)
    desc_area = driver.find_element(By.XPATH, '//div[@data-e2e="caption"]//div[@role="textbox"]')
    desc_area.click()
    desc_area.send_keys(upload_data["description"] + " " + upload_data["hashtags"])

    print("📤 Bitte prüfe und klicke manuell auf 'Posten'. ENTER zum Beenden...")
    input()
    driver.quit()
    print("✅ Upload abgeschlossen")
    
    

