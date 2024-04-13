from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.options import Options

from time import sleep
from tqdm import tqdm

firefox_options = Options()
firefox_options.add_argument('--headless')
driver = webdriver.Firefox(options=firefox_options)

tqdm_params = {
    "unit_scale": True,
    "miniters": 1,
    "total": 3,
}

def get_spotify_track():
    url = input("Spotify track link:\n")

    with tqdm(**tqdm_params) as pb:
        # Get track name 
        driver.get(url)
        span = driver.find_element(By.CLASS_NAME, "rEN7ncpaUeSGL9z0NGQR")
        h1 = span.find_element(By.CSS_SELECTOR, "h1.Text__TextElement-sc-if376j-0.ksSRyh.encore-text-headline-large")
        track_name = h1.text
        pb.update()

        #get author
        div_name = driver.find_element(By.CSS_SELECTOR, "div.Type__TypeElement-sc-goli3j-0.gZImOH.t5WPFlGTY6GCd9UOFfLu")
        author_name = div_name.text
        pb.update()

        #get album cover
        cover_div = driver.find_element(By.CLASS_NAME, "CmkY1Ag0tJDfnFXbGgju")
        cover = cover_div.find_element(By.CSS_SELECTOR, "img.mMx2LUixlnN_Fu45JpFB.CmkY1Ag0tJDfnFXbGgju._EShSNaBK1wUIaZQFJJQ.Yn2Ei5QZn19gria6LjZj")
        cover_url = cover.get_property('src') 
        pb.update()

        driver.quit()

    return [author_name, track_name, cover_url]

