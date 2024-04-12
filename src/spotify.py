from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.options import Options
import requests
import time

firefox_options = Options()
firefox_options.add_argument('--headless')

driver = webdriver.Firefox(options=firefox_options)

def get_spotify_track():
    url = input("Spotify track link:\n")

    driver.get(url)
    span = driver.find_element(By.CLASS_NAME, "rEN7ncpaUeSGL9z0NGQR")
    h1 = span.find_element(By.CSS_SELECTOR, "h1.Text__TextElement-sc-if376j-0.ksSRyh.encore-text-headline-large")

    track_name = h1.text

    # span_name = driver.find_element(By.CSS_SELECTOR, "span.Text__TextElement-sc-if376j-0.gYdBJW.encore-text-body-small-bold") 

    div_name = driver.find_element(By.CSS_SELECTOR, "div.Type__TypeElement-sc-goli3j-0.gZImOH.t5WPFlGTY6GCd9UOFfLu")
    author_name = div_name.text

    time.sleep(20)
    driver.quit()

    return [author_name, track_name]






