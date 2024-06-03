from bs4 import BeautifulSoup
import requests
from pathlib import Path



def main(url,folder_name):
    listt = []
    data = requests.get(url)
    soup = BeautifulSoup(data.text, 'html.parser')
    imgage = soup.find_all("img")
    for img in imgage:
        try:
            listt.append(img["data-srcset"])
        except:
            try:
                listt.append(img["src"])
            except:
                listt.append(img["data-src"])
            try:
                listt.append(img["data-fallback-src"])
            except:
                pass
        
    folder(listt, folder_name)

def folder(listt, folder_name):
    count=0
    path =Path(folder_name)
    path.mkdir(parents=True,exist_ok=True)
    for i, j in enumerate(listt):
        img_link = requests.get(j).content
        with open(f"{folder_name}/images{i+1}.jpg", "wb+") as f:
            f.write(img_link)
            count+=1

    print(f'Number of images downloded out of :{len(listt)} is {count}') 

url = input("Enter the URL: ")
folder_name = input("Enter the folder name: ")
main(url,folder_name)
