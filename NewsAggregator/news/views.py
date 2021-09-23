
from django.shortcuts import render
import requests
from bs4 import BeautifulSoup

# Create your views here.

  
#MSNBC NEWS
msnbc_r = requests.get("https://www.politico.com/news/msnbc")
msnbc_soup = BeautifulSoup(msnbc_r.content, 'html5lib')
msnbc_headings = msnbc_soup.find_all('h3')
msnbc_headings = msnbc_headings[0:]
 
msnbc_news = []

for mh in msnbc_headings:
    msnbc_news.append(mh.text)

#MSNBC NEWS 2
msnbc_r2 = requests.get("https://www.politico.com/news/msnbc/2")
msnbc_soup2 = BeautifulSoup(msnbc_r2.content, 'html5lib')
msnbc_headings2 = msnbc_soup2.find_all('h3')
msnbc_headings2 = msnbc_headings2[0:]

msnbc_news2 = []

for mh2 in msnbc_headings2:
    msnbc_news2.append(mh2.text)


#MSNBC NEWS 3
msnbc_r3 = requests.get("https://www.politico.com/news/msnbc/3")
msnbc_soup3 = BeautifulSoup(msnbc_r2.content, 'html5lib')
msnbc_headings3 = msnbc_soup3.find_all('h3')
msnbc_headings3 = msnbc_headings3[0:]

msnbc_news3 = []

for mh3 in msnbc_headings3:
    msnbc_news3.append(mh3.text)


#MSNBC NEWS 4
msnbc_r4 = requests.get("https://www.politico.com/news/msnbc/4")
msnbc_soup4 = BeautifulSoup(msnbc_r4.content, 'html5lib')
msnbc_headings4 = msnbc_soup4.find_all('h3')
msnbc_headings4 = msnbc_headings4[0:]

msnbc_news4 = []

for mh4 in msnbc_headings4:
    msnbc_news4.append(mh4.text)

#MSNBC NEWS 5
msnbc_r5 = requests.get("https://www.politico.com/news/msnbc/5")
msnbc_soup5 = BeautifulSoup(msnbc_r5.content, 'html5lib')
msnbc_headings5 = msnbc_soup5.find_all('h3')
msnbc_headings5 = msnbc_headings5[0:]

msnbc_news5 = []

for mh5 in msnbc_headings5:
    msnbc_news5.append(mh5.text)

#MSNBC NEWS 6
msnbc_r6 = requests.get("https://www.politico.com/news/msnbc/6")
msnbc_soup6 = BeautifulSoup(msnbc_r6.content, 'html5lib')
msnbc_headings6 = msnbc_soup6.find_all('h3')
msnbc_headings6 = msnbc_headings6[0:]

msnbc_news6 = []

for mh6 in msnbc_headings6:
    msnbc_news6.append(mh6.text)

  

#NBC NEWS
nbc_r= requests.get("https://www.nbcnews.com/us-news")
nbc_soup = BeautifulSoup(nbc_r.content, 'html5lib')
nbc_headings = nbc_soup.find_all('h2')
nbc_headings = nbc_headings[1:]
indices_to_access = [0,2,4,8,11,14,17,20,23,26,29,32,35,38]
accessed_mapping = map(nbc_headings.__getitem__, indices_to_access)
nbc_headings = list(accessed_mapping)
  
nbc_news = []

for nh in nbc_headings:
    nbc_news.append(nh.text)

#NBC NEWS
nbc2_r= requests.get("https://www.nbcnews.com/business")
nbc2_soup = BeautifulSoup(nbc2_r.content, 'html5lib')
nbc2_headings = nbc2_soup.find_all('h2')
nbc2_headings = nbc2_headings[1:112:2]
nbc_news2 = []

for nh2 in nbc2_headings:
    nbc_news2.append(nh2.text)


  

 
def index2(req):

    return render(req, 'news/index2.html', {'msnbc_news':msnbc_news, 'msnbc_news2':msnbc_news2,'msnbc_news3':msnbc_news3,'msnbc_news4':msnbc_news4,'msnbc_news5':msnbc_news5,
    'msnbc_news6':msnbc_news6, 'nbc_news':nbc_news, 'nbc_news2':nbc_news2})


  
      