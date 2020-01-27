import requests
from bs4 import BeautifulSoup


Test_link = 'https://www.youtube.com/watch?v=rfscVS0vtbw'
#python for begginers by codecamp . org

class YTScraper():
    def __init__(self,url = Test_link):
        '''
                Access Check
                '''
        self.link = url
        self.page = requests.get(self.link)
        if self.page.status_code != 200:
            raise Exception('Page Not available')
        '''
        creation of primary_soup object
        '''
        print(self.page.content)
        self.soup = BeautifulSoup(self.page.content, 'html.parser')
        '''
                extraction of title
                '''
        titles = self.soup.find_all('h1')
        titles_soup = BeautifulSoup(str(titles),'html.parser')
        title_block = titles_soup.prettify()
        next = False
        self.title = ''
        for each in title_block.splitlines():
            if next is True:
                self.title = each
                next = False
            if ' <span class="watch-title"' in each:
                next = True
        '''
        views
        '''
        views_tags = self.soup.find_all('yt-view-count-renderer')
        #print(self.soup)




    def print_raw_content(self):
        return self.soup


alex = YTScraper()

