# WebScanner

WebScanner is a Python-based web scraping tool designed to extract and save web pages while recursively following links. This tool can be helpful for web developers, researchers, and anyone interested in analyzing website content.

## Features

- Scrapes web pages from a list of specified URLs.
- Recursively follows links found on the scraped pages.
- Saves each page as an HTML file in a specified output directory.
- Configurable number of threads and request timeout.
- Option to skip invalid URLs.

## Requirements

- Python 3.x
- Required Python packages:
  - `requests`
  - `beautifulsoup4`

You can install the required packages using pip:

```bash
pip install -r requirements.txt
```

## Usage

### Command-Line Arguments

To run WebScanner, use the following command:

```bash
python WebScanner.py --urls <URL1> <URL2> ... --output-dir <OUTPUT_DIRECTORY> [--threads <NUMBER>] [--timeout <TIMEOUT>] [--skip-invalid]
```

### Parameters

- `--urls`: List of URLs to scrape (space-separated).
- `--output-dir`: Directory to save the scraped pages.
- `--threads`: (Optional) Number of threads to use (default is 10).
- `--timeout`: (Optional) Timeout for requests in seconds (default is 5).
- `--skip-invalid`: (Optional) Flag to skip displaying invalid URLs.

### Example

```bash
python WebScanner.py --urls https://example1.com https://example2.com --output-dir ./output --threads 10
```

## Important Notes

- If you are not on a robust network, consider using a cloud hosting service like **OVH**, **AWS**, or **Heroku** to run this tool. This will help prevent rate limits and potential blocks by target websites.
- I am not responsible for any rate limits or blocks that may occur as a result of using this tool. Use it responsibly and in accordance with the terms of service of the websites you are scraping.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for more details.
