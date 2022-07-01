## Webscraping Product Page with Selenium

There are several methods when we want to scrape data from a website. The method used is based on the structure of the website, and whether there is a protection on the website. In this page, I show how to scrape the data from a website that is protected by Cloudflare. After trying to use request HTML and BeautifulSoup, the response is forbidden or showing the HTML of captcha page. So, I tried to scrape the website using Selenium libray on Python.

You can use the [editor on GitHub](https://github.com/bagz6/bike-selenium/edit/gh-pages/index.md) to maintain and preview the content for your website in Markdown files.

Whenever you commit to this repository, GitHub Pages will run [Jekyll](https://jekyllrb.com/) to rebuild the pages in your site, from the content in your Markdown files.

### The Code
Before we start scraping, we should import several libraries
```makrdown
from selenium import webdriver
from selenium.webdriver import Chrome
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
import time
import pandas as pd
```
Selenium is a headless browser so that it will not detected by the cloudflare protecting the webpage. In this case, I use chromewebdriver, and the chromedriver version should be the same as the chrome browser version in our computer. I also imported `time` to create a pause between codes, so that it is fully loaded before we scrape the data. Pandas is used to later save the scraped data to csv file and creating dataframe to see the structure of the data.


```markdown
Syntax highlighted code block

# Header 1
## Header 2
### Header 3

- Bulleted
- List

1. Numbered
2. List

**Bold** and _Italic_ and `Code` text

[Link](url) and ![Image](src)
```

For more details see [Basic writing and formatting syntax](https://docs.github.com/en/github/writing-on-github/getting-started-with-writing-and-formatting-on-github/basic-writing-and-formatting-syntax).

### Jekyll Themes

Your Pages site will use the layout and styles from the Jekyll theme you have selected in your [repository settings](https://github.com/bagz6/bike-selenium/settings/pages). The name of this theme is saved in the Jekyll `_config.yml` configuration file.

### Support or Contact

Having trouble with Pages? Check out our [documentation](https://docs.github.com/categories/github-pages-basics/) or [contact support](https://support.github.com/contact) and we’ll help you sort it out.
