#!/usr/bin/env python
# coding: utf-8

# In[36]:



from splinter import Browser
import pymongo
from bs4 import BeautifulSoup as bs

# In[37]:


def init_browser():
    executable_path = {"executable_path": "chromedriver"}
    return Browser("chrome", **executable_path, headless=True)


# In[40]:


def scrape_info():
    from splinter import Browser
    import pymongo
    from bs4 import BeautifulSoup as bs

    browser = init_browser()
    url = "https://www.glassdoor.com/Reviews/Google-Reviews-E9079.htm"
    browser.visit(url)

     # Scrape page into Soup
    html = browser.html
    soup = bs(html, "html.parser")
    score_list = []

    # Get the first div 
    
    score = soup.find("div", class_= "ratingNum").text
    Pros = soup.find("p", class_=" pros mainText truncateThis wrapToggleStr").text
    

    Cons = soup.find("p", class_=" cons mainText truncateThis wrapToggleStr").text
    

    review_dict = {"rating":score, "pros":Pros, "cons":Cons}
    
    browser.quit()

    # Return results
    return review_dict



# In[ ]:




