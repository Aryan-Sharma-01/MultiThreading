
#Webscrapping
from concurrent.futures import ThreadPoolExecutor
import threading
import requests
from bs4 import BeautifulSoup 
 
urls=[ "https://langchain-ai.github.io/langgraph/concepts/why-langgraph/",
      "https://langchain-ai.github.io/langgraph/tutorials/get-started/1-build-basic-chatbot/"
      ] 

def fetch_content(url):
    response=requests.get(urls)
    soup=BeautifulSoup(response.content,'html.parser')
    print(f'Fetched{len(soup.text)}characters from {url}')
threads=[]
for url in urls:
    thread=threading.Thread(target=fetch_content,args=(url,))
    threads.append(thread)
    thread.start()
for th in threads:
    th.join()
print("All WEB PAGES FETCHED")         