from bs4 import BeautifulSoup
import requests
import os

try:
    os.makedirs('Pictures')
except:
    pass
print("\nPictures will be saved in the following directory:")
os.chdir("Pictures/")
print(os.getcwd())

print("\nParsing Pages...")
overall_links = []
page_no = 400
while(page_no<=476):
    print(page_no)
    source = requests.get('https://www.bwallpaperhd.com/page/' + str(page_no)).text
    soup = BeautifulSoup(source, 'lxml')

    image_links = soup.find_all('div',class_='view view-first')

    for image_link in image_links:
        overall_links.append(image_link.a['href'])

    page_no+=1

# print(overall_links)
print("\nAll pages parsed! Collecting download links...")

download_links = []
name_list = []
for link in overall_links:
    source = requests.get(link).text
    soup = BeautifulSoup(source,'lxml')

    download_list = soup.find('div',class_='download').find_all('a')
    for download_link in download_list:
        # print(download_link)
        if download_link.text == " Original":
            download_links.append(download_link['href'])
    # print("\n\n")

    file_name = soup.find('div',class_='post').h1.text
    name_list.append(file_name)

# print(download_links)
# print(name_list)

print("\nDownload links collected! Downloading now...")

for i in range(len(download_links)):
    temp = requests.get(download_links[i])

    with open(name_list[i] + ".jpg",'wb') as f:
        f.write(temp.content)

print("\nAll images downloaded! Enjoy!")
