import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin

def scrape_hellaheels_uk():
    base_url_uk = "https://uk.hellaheels.com"
    target_url_uk = "https://uk.hellaheels.com/collections/stilettos?filter.v.option.size=UK11+%2F+EU44+%2F+US13+%2F+AU13+-+Wide+Fit&filter.v.price.gte=&filter.v.price.lte=&sort_by=created-descending"

    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
    }
    
    try:
        # Fetch the page content
        response_uk = requests.get(target_url_uk, headers=headers)
        response_uk.raise_for_status()

        soup_uk = BeautifulSoup(response_uk.text, 'html.parser')

        product_items_uk = soup_uk.find_all('h3', class_='card__heading h5')

        print("UK Items:<br>")
        print("<br>")
        for item in product_items_uk:
            print(item)

    except requests.RequestException as e:
        print(f"Error fetching the page: {e}")
    except Exception as e:
        print(f"An error occurred: {e}")

def scrape_hellaheels_us():
    base_url_us = "https://us.hellaheels.com"
    target_url_us = "https://us.hellaheels.com/collections/stilettos?filter.v.availability=1&filter.v.option.size=UK11+%2F+EU44+%2F+US13+%2F+AU13+-+Wide+Fit&filter.v.price.gte=&filter.v.price.lte=&sort_by=created-descending"
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
    }
    
    try:
        # Fetch the page content
        response_us = requests.get(target_url_us, headers=headers)
        response_us.raise_for_status()

        soup_us = BeautifulSoup(response_us.text, 'html.parser')

        product_items_us = soup_us.find_all('h3', class_='card__heading h5')

        print("US Items:<br>")
        print("<br>")
        for item in product_items_us:
            print(item)

    except requests.RequestException as e:
        print(f"Error fetching the page: {e}")
    except Exception as e:
        print(f"An error occurred: {e}")


def scrape_hellaheels_au():
    base_url_au = "https://au.hellaheels.com"
    target_url_au = "https://au.hellaheels.com/collections/stilettos?filter.v.option.size=UK11+%2F+EU44+%2F+US13+%2F+AU13+-+Wide+Fit&filter.v.price.gte=&filter.v.price.lte=&sort_by=manual"

    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
    }
    
    try:
        # Fetch the page content
        response_au = requests.get(target_url_au, headers=headers)
        response_au.raise_for_status()

        soup_au = BeautifulSoup(response_au.text, 'html.parser')

        product_items_au = soup_au.find_all('h3', class_='card__heading h5')

        print("AU Items:<br>")
        print("<br>")
        for item in product_items_au:
            print(item)

    except requests.RequestException as e:
        print(f"Error fetching the page: {e}")
    except Exception as e:
        print(f"An error occurred: {e}")

def main():
    print("Scraping Hella Heels for UK11/EU44/US13/AU13 Wide Fit shoes...<br>")
    print("<br>")
    scrape_hellaheels_uk()
    scrape_hellaheels_us()
    scrape_hellaheels_au()


if __name__ == "__main__":
    main()