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

def get_spotify_track(url):
    with tqdm(**tqdm_params) as pb:
        # Get track name 
        driver.get(url)
        span = driver.find_element(By.CLASS_NAME, "rEN7ncpaUeSGL9z0NGQR")
        h1 = span.find_element(By.CSS_SELECTOR, "h1.encore-text.encore-text-headline-large.encore-internal-color-text-base")
        track_name = h1.text
        pb.update()

        #get author
        author_div = driver.find_element(By.CSS_SELECTOR, "div.RANLXG3qKB61Bh33I0r2.NO_VO3MRVl9z3z56d8Lg")
        span_name = author_div.find_element(By.CSS_SELECTOR, "span.encore-text.encore-text-body-small-bold")
        name = span_name.find_element(By.TAG_NAME, "a")
        author_name = name.text
        pb.update()

        #get album cover
        cover_div = driver.find_element(By.CLASS_NAME, "CmkY1Ag0tJDfnFXbGgju")
        cover = cover_div.find_element(By.CSS_SELECTOR, "img.mMx2LUixlnN_Fu45JpFB.CmkY1Ag0tJDfnFXbGgju._EShSNaBK1wUIaZQFJJQ.Yn2Ei5QZn19gria6LjZj")
        cover_url = cover.get_property('src') 
        pb.update()

        driver.quit()

    return [author_name, track_name, cover_url]

