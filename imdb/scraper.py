from requests import get
from bs4 import BeautifulSoup
import csv
from time import sleep
genres = [
    'action',
    'adventure',
    'animation',
    'biography',
    'comedy',
    'crime',
    'drama',
    'family',
    'fantasy',
    'film_noir',
    'history',
    'horror',
    'music',
    'musical',
    'mystery',
    'romance',
    'sci_fi',
    'sport',
    'thriller',
    'war',
    'western',
]



def scrapedata():
    with open('topmovies.csv', 'a', newline='') as file:
        writer = csv.writer(file)
        # writer.writerow(['Name','Runtime','Genre','Rating'])
        for j in genres:
            siteid = 'https://www.imdb.com/search/title/?genres='+j+'&sort=user_rating,desc&title_type=feature&num_votes=25000,&pf_rd_m=A2FGELUUNOQJNL&pf_rd_p=5aab685f-35eb-40f3-95f7-c53f09d542c3&pf_rd_r=FYNW4RFB6YAFPDEHT1BH&pf_rd_s=right-6&pf_rd_t=15506&pf_rd_i=top&ref_=chttp_gnr_2'
            response = get(siteid)
            html_ka_soup = BeautifulSoup(response.text, 'html.parser')
            movie_containers = html_ka_soup.find_all('div', class_ = 'lister-item mode-advanced')
            movie=list(movie_containers)

    # name,runtime,genre,rating
            
            for i in range(len(movie)):
                row=[list(movie[i].children)[5].h3.a.text.split(',',1)[0],
                #  list((list(movie[i].children)[7].p).children)[1].text.split(' ', 1)[0],
                int((movie[i].p.find('span', class_ = 'runtime').text).split(' ',1)[0]),
                j,
                float(list((list(movie[i].children)[5].div).children)[1].strong.text)]
                writer.writerow(row)
            sleep(2)

    file.close()
    
scrapedata()
    
    
    
    
    
    
