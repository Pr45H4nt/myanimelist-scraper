# MyAnimeList Top Anime Scrapy Project

Welcome! This project focuses on scraping the top anime listings from [MyAnimeList](https://myanimelist.net/topanime.php). Though the structure of the website might seem intricate, we've effectively navigated and scraped the necessary data!

## 🚀 Quick Start

1. **Install necessary packages**

    Before proceeding, ensure you have all the essential packages installed. Check the `requirements.txt` file for a comprehensive list.

    ```bash
    pip install -r requirements.txt
    ```

2. **Run the Spider**

    Once in the project directory, execute the `myanimelist_spider`.

    ```bash
    scrapy crawl myanimelist_spider -O anime_data.csv
    ```

## 📦 Output

The retrieved data will be stored in a CSV file named `anime_data.csv`. For convenient data analysis, open the file using spreadsheet tools such as Microsoft Excel or Google Sheets.

## 📋 Data Columns

The scraper extracts the following columns:
- TITLE
- PLOT
- POSTER
- RATING
- PEOPLE_RATED
- JAPANESE_NAME
- EPISODES
- STATUS
- AIRED
- DURATION
- POPULARITY
- RANKED
- CERTIFICATE
- MEMBERS
- FAVOURITES
- PRODUCERS
- LICENSORS
- GENRE
- STUDIOS

## 🔍 Challenges Faced

- **Complex HTML Structure:** The website's HTML was intricate, but we meticulously decoded the essential sections to ensure accurate data scraping.

- **Pagination Issues:** With the pagination feature, we had to ensure continuous and seamless scraping across multiple pages.

## 📚 Resources

- **Scrapy Documentation:** If you wish to delve deeper or encounter any challenges, the official Scrapy documentation can be a valuable guide: [Scrapy Documentation](https://docs.scrapy.org/en/latest/)

## 🙌 Contributions

Do you have ideas or improvements in mind? Jump right in! Whether you want to open an issue, suggest enhancements, or fix existing bugs, your contributions are highly appreciated!

## 📃 License

This project is open-source and accessible to everyone. You're free to use, modify, and distribute it as you wish. Happy scraping!

---
