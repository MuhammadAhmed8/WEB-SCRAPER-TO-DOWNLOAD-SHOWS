import requests
from bs4 import BeautifulSoup
import os
import sys



def getVideoLinks(url):
    request_data = requests.get(url)
    soup = BeautifulSoup(request_data.content, 'html5lib')

    links = soup.findAll('a')
    video_links = [link.get('onclick') for link in links if link.get('onclick') is not None]
    video_links = [link.split("'")[1] for link in video_links]

    return video_links

def downloadAll(video_links, folder, skip_seasons):
    video_links = video_links[skip_seasons:]
    for link in video_links:

        '''iterate through all links in video_links 
        and download them one by one'''

        # obtain filename by splitting url and getting
        # last string
        file_name = link.split('/')[-1]

        print("Downloading file: %s" % file_name)

        # create response object
        r = requests.get(link, stream=True)

        # download started
        file = folder + "\\" + file_name
        print(file_name)
        with open(file, 'wb') as f:
            size_mb = 0
            for chunk in r.iter_content(chunk_size=1024 * 1024):
                current_size = os.path.getsize(file)
                size_mb = current_size / (1024 * 1024)
                if size_mb % 3 == 0:
                    sys.stdout.write("Download progress: %d mb  \r" % (size_mb))
                    sys.stdout.flush()
                if chunk:
                    f.write(chunk)



    print("All videos downloaded!")

    return


if __name__ == "__main__":
    url = input("enter url:")
    folder = input("enter destination folder path: ")
    skip_seasons = int(input("How many parts do you wish to skip from the start? "))
    links = getVideoLinks(url)
    #downloadAll(links, folder, skip_seasons)
    file_name = url.split('/')[-1]

    print("Downloading file: %s" % file_name)

    # create response object
    r = requests.get(url, stream=True)

    # download started
    file = folder + "\\" + "shakespear.txt"
    print(file_name)
    with open(file, 'wb') as f:
        size_mb = 0
        for chunk in r.iter_content(chunk_size=1024 * 1024):
            current_size = os.path.getsize(file)
            size_mb = current_size / (1024 * 1024)
            if size_mb % 3 == 0:
                sys.stdout.write("Download progress: %d mb  \r" % (size_mb))
                sys.stdout.flush()
            if chunk:
                f.write(chunk)
