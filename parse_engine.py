"""This Script contains a scraper parser class that
extract body text from the given url"""

import sys
import csv

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager


class ParseEngine:

  """A parser that takes an url and xpath and a method that returns bodytext.

  This class asks for a url and a xpath that leads to the content for that url.
  Then, call the get_body_text method to return a string of body text
  Best used when reading url and xpath from a database

    Typical usage example:

    engine = ParseEngine(url = reader.url, xpath = reader.xpath)
    text = engine.get_body_text()

"""
  def __init__(self, url, xpath, headless=True):
    self.xpath = xpath

    chrome_options = Options()
    chrome_options.add_argument('window-size=1200x1000')
    if headless: chrome_options.add_argument('--headless')
    self.driver = webdriver.Chrome(
                    ChromeDriverManager().
                    install(),
                    options=chrome_options
    )
    self.driver.get(url)

  def get_body_text(self):
    i = 1
    body_text = ''
    element = self.driver.find_elements_by_xpath(self.xpath)
    for i in element:
      body_text += i.text

    return body_text


def main(domain, url):

  with open('parsing_info.csv') as csvfile:
    xpath = ''
    reader = csv.reader(csvfile, delimiter = ',')
    for row in reader:
      if domain == row[0]:
        xpath = row[1]
        break
    if not xpath:
      print('Domain info not in database')
      print(domain, url)
      sys.exit(1)

  text = ParseEngine(url = url, xpath = xpath).get_body_text()
  return text


if __name__ ==  '__main__':
  print(main(sys.argv[1], sys.argv[2]))
