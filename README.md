# News Scraper Parser

A script that scraps and parses news articles

-------------------------

- [Introduction](#introduction)
- [Usage](#usage)
- [Challenges](#challenges)
- [Current Approach](#current-approach)
- [How to Contribute](#how-to-contribute)

-------------------------

## Introduction

In the information era, browsing and learning information from news articles is supposed to be easy. However, in reality, many main stream news sites are filled with noises like advertisements, clickbaits, and pop-up windows. Also, different news sites organize their articles differently, forcing readers to adjust to different formattings. 

This program is designed for Professor Wojcieszak, Menchen-Trevino, and their colleagues at the EXPO project (Europeans Exposed to Dissimilar Views: Investigating Backfire Effects). They are trying to study the dynamic between news articles and the stratification of the society. To do so, they are currently reviewing more than 30,000 articles. Manually visiting every page is simply not viable. Therefore, I created this script that scrape and parse articles from  given urls and store them in a database to help the EXPO project.

-------------------------

## Usage

```
python3 parse_engine.py <domain name> <url>
```
Due to copyright issues, I cannot post the driver that repeatively call the engine to scrape and parse multiple urls from databases. Still, you can always make your own driver!

-------------------------

## Challenges

The current database contains articles from more than 300 sites, and that number is expected to increase in the future. Also, most articles have too little contents in too much noise. It is normal for a 400kB html file to have only 6 sentences of actual content. Also, every news site has an unique layout. Thus, eliminating noises while keep all the actual content is the biggest challenge of this project.

-------------------------

## Current Approach

After trials and errors, the current approach is using xpath and Selenium to accurately scrape and parse contents. We store \<domain name\>, \<xpath to contents\> pairs in parsing_info.csv, and the parser will look up the xpath for the domain of the given url. There are two main downsides to this approach. First, it is slower than tools such as Beautiful Soup. Second, we must manually add xpath information for every site. However, none of these could compare with the key strength of this approach: accuracy. We are almost guarenteed to parse every article from a particular site with 100% accuracy as long as we have the correct xpath.

-------------------------

## How to Contribute

In parsing_info.csv, you can add \<domain name\>, \<xpath to contents\> if that xpath is tested to always contain noise-free content. We are welcoming any domain from any language, as doing so will increase the datapoints for the research and make this program more universal.
If you spot an issue with current xpath, feel free to report it too!
