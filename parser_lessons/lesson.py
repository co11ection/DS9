import re
import time
import requests
from bs4 import BeautifulSoup
import pandas as pd
BASE_URL = "https://house.kg"
LIST_PATH = "/kupit-kvartiru"
HEADERS =  {
    "User-Agent": 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36'
}
PAGE_PAUSE_SECONDS = 1.5
DETAIL_PAUSE_SECOND = 1.0

PARSE_PAGE = 20

TITLE_RE = re.compile(
    r"(?:(?P<rooms>\d+)-комн\.|(?P<free>свободная планировка))\s*кв\.,\s*"
    r"(?P<area>[\d,.]+)\s*м²,\s*"
    r"(?P<floor>\d+)\s*этаж\s*из\s*(?P<total_floors>\d+)"
)

PRICCE_SOM_RE = re.compile(r"[\d\s]+⃀")

def get_html(url, params):
    response = requests.get(url=url, headers=HEADERS, params=params, timeout=10)
    response.raise_for_status()
    return response.text

def parse_title(title_text):
    if not title_text:
        return None, None, None, None
    m = TITLE_RE.search(title_text)
    print(m)
    if not m:
        return None, None, None, None
    rooms = int(m.group('rooms')) if m.group("rooms") else None
    area = float(m.group('area').replace(',', "."))
    floor = int(m.group('floor'))
    total_floors = int(m.group("total_floors"))
    
    return rooms, area, floor, total_floors


def extract_card(article, href):
    title_a = article.select_one("a.text-house-text-link")
    title_text = title_a.get_text(strip=True) if title_a else None
    rooms, area, floor, total_floor = parse_title(title_text)
    
    addr_span = article.select_one("span.text-house-text-secondary-text")
    address = addr_span.get_text(strip=True) if addr_span else None
    
    price_som = None
    for span in article.select("span.text-house-text-primary-text"):
        text = span.get_text(strip=True)
        if PRICCE_SOM_RE.fullmatch(text):
            price_som = int(re.sub(r'\D', "", text))
            break
    
    img = article.find("img")
    image_url = img.get('src') if img else None
    
    return {
        "url": BASE_URL + href,
        "title": title_text,
        'address': address,
        "price_som": price_som,
        "rooms": rooms,
        "area_m2": area,
        "floor": floor,
        "total_floor": total_floor,
        "img_url": image_url
        }
    

def  parse_catalog_page(html):
    soup = BeautifulSoup(html, 'html.parser')
    seen_href = set()
    cards = []
    for article in soup.find_all("article"):
        link = article.select_one('a[href^="/details/"]')
        if link is None:
            continue
        href = link.get('href')
        seen_href.add(href)
        cards.append(extract_card(article, href))
        
    return cards


def scrape_catalog(n_pages):
    all_cards = []
    for page_number in range(1, n_pages+1):
        html = get_html(
            BASE_URL+LIST_PATH, params={"page": page_number}
        )
        cards = parse_catalog_page(html)
        all_cards.extend(cards)
        if page_number < n_pages:
            time.sleep(PAGE_PAUSE_SECONDS)
    
    return all_cards


def main():
    cards = scrape_catalog(PARSE_PAGE)
    print(cards)
    df = pd.DataFrame(cards)
    df.to_csv('house.csv', index=False, encoding='utf-8-sig')
    print(df.head())
    

if __name__ == "__main__":
    main()


