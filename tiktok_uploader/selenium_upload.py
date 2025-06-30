import time
import pickle
from selenium import webdriver
from selenium.webdriver.common.by import By

def start_driver():
    options = webdriver.ChromeOptions()
    options.add_argument("--start-maximized")
    driver = webdriver.Chrome(options=options)
    return driver

def login_and_save_cookies(driver):
    driver.get("https://www.tiktok.com/login")
    print("Logge dich manuell ein. Du hast 60 Sekunden.")
    time.sleep(60)
    cookies = driver.get_cookies()
    with open("cookies.pkl", "wb") as f:
        pickle.dump(cookies, f)
    print("Cookies gespeichert.")

def load_cookies(driver):
    driver.get("https://www.tiktok.com/")
    with open("cookies.pkl", "rb") as f:
        cookies = pickle.load(f)
    for cookie in cookies:
        try:
            driver.add_cookie(cookie)
        except:
            pass
    driver.get("https://www.tiktok.com/upload?lang=de")

def upload_video(driver, video_path, description):
    time.sleep(5)
    file_input = driver.find_element(By.XPATH, '//input[@type="file"]')
    file_input.send_keys(video_path)

    print("Video wird hochgeladen...")
    time.sleep(15)

    # Beschreibung
    desc_box = driver.find_element(By.XPATH, '//div[contains(@data-e2e, "caption-input")]//p')
    desc_box.click()
    desc_box.send_keys(description)

    time.sleep(2)

    # Veröffentlichen
    post_button = driver.find_element(By.XPATH, '//button[@data-e2e="publish-button"]')
    post_button.click()

    print("✅ Video wurde gepostet.")

def run_upload(video_path, description):
    driver = start_driver()
    load_cookies(driver)
    upload_video(driver, video_path, description)
    driver.quit()
