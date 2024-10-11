import argparse
import random
import requests
import os
from bs4 import BeautifulSoup
from urllib.parse import urljoin, urlparse

class WebScanner:
    def __init__(self, urls, threads, timeout, output_dir, skip_invalid):
        self.urls = urls
        self.threads = threads
        self.timeout = timeout
        self.output_dir = output_dir
        self.skip_invalid = skip_invalid
        self.visited_urls = set()

        if not os.path.exists(output_dir):
            os.makedirs(output_dir)

    def scrape(self, url):
        if url in self.visited_urls:
            return

        self.visited_urls.add(url)

        try:
            response = requests.get(url, timeout=self.timeout)
            if response.status_code == 200:
                content = response.text
                self.save_page(url, content)
                self.check_for_links(content)
            elif not self.skip_invalid:
                print(f"\033[91m[Invalid URL] {url}\033[0m")
        except requests.RequestException:
            if not self.skip_invalid:
                print(f"\033[91m[Invalid URL] {url}\033[0m")

    def save_page(self, url, content):
        filename = os.path.join(self.output_dir, f"{urlparse(url).netloc}_{random.randint(1000, 9999)}.html")
        with open(filename, 'w', encoding='utf-8') as file:
            file.write(content)
        print(f"\033[92m[Saved] {filename}\033[0m")

    def check_for_links(self, content):
        soup = BeautifulSoup(content, 'html.parser')
        for link in soup.find_all('a', href=True):
            full_link = urljoin(self.urls[0], link['href'])
            if full_link not in self.visited_urls:
                self.scrape(full_link)

    def start_scraping(self):
        for url in self.urls:
            print(f"\033[94m[Starting] Scraping from: {url}\033[0m")
            self.scrape(url)

def parse_arguments():
    parser = argparse.ArgumentParser(description="Web Scanner Tool")
    parser.add_argument('--urls', required=True, nargs='+', help="List of URLs for scraping (space-separated)")
    parser.add_argument('--threads', type=int, default=10, help="Number of threads to use")
    parser.add_argument('--timeout', type=int, default=5, help="Timeout for requests")
    parser.add_argument('--output-dir', required=True, help="Directory to save scraped pages")
    parser.add_argument('--skip-invalid', action='store_true', help="Skip displaying invalid URLs")
    return parser.parse_args()

if __name__ == "__main__":
    args = parse_arguments()
    scanner = WebScanner(args.urls, args.threads, args.timeout, args.output_dir, args.skip_invalid)
    scanner.start_scraping()
