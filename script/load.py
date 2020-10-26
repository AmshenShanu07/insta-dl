from datetime import datetime
from tqdm import tqdm
import requests
import re
import shutil, os
result='--/--'

#Checking connection
def connection(url='http://www.google.com/', timeout=5):
    global result
    try:
        req = requests.get(url, timeout=timeout)
        req.raise_for_status()
        return True
    except requests.HTTPError as e:
        print("Checking internet connection failed, status code {0}.".format(
        e.response.status_code))
    except requests.ConnectionError:
        result='No Internet'
    return False

#Download Post
def download(link):
    global result

    url = link
    x = re.match(r'^(https:)[/][/]www.([^/]+[.])*instagram.com', url)

    try:
        if x:
            request_image = requests.get(url)
            src = request_image.content.decode('utf-8')
            check_type = re.search(r'<meta name="medium" content=[\'"]?([^\'" >]+)', src)
            check_type_f = check_type.group()
            final = re.sub('<meta name="medium" content="', '', check_type_f)

            if final == "image":
                extract_image_link = re.search(r'meta property="og:image" content=[\'"]?([^\'" >]+)', src)
                image_link = extract_image_link.group()
                final = re.sub('meta property="og:image" content="', '', image_link)
                _response = requests.get(final).content
                file_size_request = requests.get(final, stream=True)
                file_size = int(file_size_request.headers['Content-Length'])
                block_size = 1024 
                filename = datetime.strftime(datetime.now(), '%Y-%m-%d-%H-%M-%S')
                t=tqdm(total=file_size, unit='B', unit_scale=True, desc=filename, ascii=True)
                with open(filename + '.jpg', 'wb') as f:
                    for data in file_size_request.iter_content(block_size):
                        t.update(len(data))
                        f.write(data)
                t.close()
                shutil.move(filename+'.jpg','Downloads')
                result="Sucessfully Downloaded"

            if final == "video":
                extract_video_link = re.search(r'meta property="og:video" content=[\'"]?([^\'" >]+)', src)
                video_link = extract_video_link.group()
                final = re.sub('meta property="og:video" content="', '', video_link)
                _response = requests.get(final).content
                file_size_request = requests.get(final, stream=True)
                file_size = int(file_size_request.headers['Content-Length'])
                block_size = 1024
                filename = datetime.strftime(datetime.now(), '%Y-%m-%d-%H-%M-%S')
                t=tqdm(total=file_size, unit='B', unit_scale=True, desc=filename, ascii=True)
                with open(filename+'.mp4', 'wb') as f:
                    for data in file_size_request.iter_content(block_size):
                        t.update(len(data))
                        f.write(data)
                t.close()
                shutil.move(filename+'.mp4','Downloads')
                result="Sucessfully Downloaded"  
        else:
            result="Invalid url"
    except AttributeError:
        result="Unknown URL"

