# The code below will make a request to the starting_url 
# and extract all links on the page. Then it will iterate 
# over all the new links and gather new links from the new pages. 
# It will continue this recursive process until all links have been 
# scraped that are possible from the starting point. 
# Some websites don't link outside of themselves 
# so these sites will stop sooner than sites that do link to other sites.

import requests    
import re    
from urllib.parse import urlparse    

class PyCrawler(object):    
    def __init__(self, starting_url):    
        self.starting_url = starting_url    
        self.visited = set()    

	# Is used to get the HTML at the current link
    def get_html(self, url):    
        try:    
            html = requests.get(url)    
        except Exception as e:    
            print(e)    
            return ""    
        return html.content.decode('latin-1')    

 	# Extracts links from the current page
	def get_links(self, url):    
        html = self.get_html(url)    
        parsed = urlparse(url)    
        base = f"{parsed.scheme}://{parsed.netloc}"    
        links = re.findall('''<a\s+(?:[^>]*?\s+)?href="([^"]*)"''', html)    
        for i, link in enumerate(links):    
            if not urlparse(link).netloc:    
                link_with_base = base + link    
                links[i] = link_with_base    

        return set(filter(lambda x: 'mailto' not in x, links))    

    # Will be used to extract specific info on the page.
    def extract_info(self, url):    
        html = self.get_html(url)    
        meta = re.findall("<meta .*?name=[\"'](.*?)['\"].*?content=[\"'](.*?)['\"].*?>", html)    
        return dict(meta)    

    def crawl(self, url):    
        for link in self.get_links(url):    
            if link in self.visited:    
                continue    
            self.visited.add(link)    
            info = self.extract_info(link)    

            print(f"""Link: {link}    
Description: {info.get('description')}    
Keywords: {info.get('keywords')}    
            """)    

            self.crawl(link)    

    def start(self):    
        self.crawl(self.starting_url)    

if __name__ == "__main__":    
    crawler = PyCrawler("https://google.com")     
    crawler.start() 
