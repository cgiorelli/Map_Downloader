"""Carlo Giorelli - 3/16/2017"""

import urllib
from multiprocessing.dummy import Pool as ThreadPool
import string

sections = [32,41,42,53] # Numbers of wanted sections
letters = string.ascii_lowercase # All lowercase letters, in an array
numbers = range(1,17) # 16 + 1 for loop purposes

#url = ### Full URL here for reference purposes
base = ### Repo URL

urls = []

for sec in range(0,len(sections)):
    for let in letters:
        for num in numbers:
            if num > 9:
                filename = "toporama_0" + str(sections[sec]) + let + str(num) + "_utm.zip"
            else:
                filename = "toporama_0" + str(sections[sec]) + let + '0' + str(num) + "_utm.zip"
            url = base + str(sections[sec]) + '/' + let + '/' + filename
            urls.append(url)
            
# Clearing variables from RAM       
del filename, sections, letters, numbers, base, url
            
def URL_download(url):
    filename = url[-23:]
    if filename[:1] != 't':
        filename = 't' + filename
    try:
        urllib.urlretrieve (url, filename)
    except urllib.error.URLError:
        return

Tp = ThreadPool(4) # Number of threads used

Tp.map(URL_download,urls)