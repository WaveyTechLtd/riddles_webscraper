# -*- coding: utf-8 -*-
"""
Created on Fri Jan 21 10:37:42 2022

@author: cns

Responding to UpWork post, wanting to scrap the riddles from a websitewww.riddles.com
I used the example set - "best riddles" ... 100 pages of riddles
"""

from bs4 import BeautifulSoup
import pandas as pd
import requests
import re

def scrape_riddles (url):
    
    page = requests.get(url)
    results = BeautifulSoup(page.content, "html.parser")
    page_results = []
    
    # find all h3 classes
    job_elements = results.find_all("div", class_ ="panel panel-default")

    for job_element in job_elements:
        
        # Get ID
        riddle_id = job_element.get("id")
        
        # Get Title
        riddle_title = job_element.find("h3", class_="panel-title lead inline").get_text()
        
        # Get Question
        raw_q = job_element.find("div", class_="panel-body lead").get_text()
        riddle_question = re.search(r'Riddle:\s (.*?)\n', raw_q).group(1)
        
        # Get Answer
        riddle_answer = re.search(r'Answer:\s(.*?)\n\t', raw_q).group(1)
        
        page_results.append([riddle_id, riddle_title, riddle_question, riddle_answer])
        
        
    # return a DataFrame of that page's riddles  
    return pd.DataFrame(page_results, columns=['riddle_id', 'riddle_title', 'riddle_question', 'riddle_answer'])
    
def main (base_url, n_pages, working_dir):
    
    for page in n_pages:
        if page == 1:
            
            url = base_url
            total_results = scrape_riddles(url=url)
            continue 
        
        elif page > 1:
            
            url = f"{base_url}?page={page}"
            total_results = total_results.append(scrape_riddles(url=url), ignore_index=True)
            continue
        
    total_results.to_csv(f"{working_dir}example_riddles.tsv", sep="\t", index=False)
    
if __name__ == "__main__":
    
    n_pages=list(range(1,5))
    base_url = "https://www.riddles.com/best-riddles"
    
    # Insert your own working directory here
    working_dir = ""
    
    main(base_url, n_pages, working_dir)