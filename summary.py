import requests
from bs4 import BeautifulSoup

'''
def find_class_info_zh(url, class_name):
    global class_info_zh
    try:
        response = requests.get(url)
        response.raise_for_status()  # Check for any errors in the HTTP response
        soup = BeautifulSoup(response.content, 'html.parser')
        class_elements = soup.find_all(class_=class_name)
        if len(class_elements) >= 3:
            class_info_zh = class_elements[0].text.strip()  # Remove leading and trailing spaces or newlines

    except requests.RequestException as e:
        return f"An error occurred: {e}"
def find_class_info_sz(url, class_name):
    global class_info_sz
    try:
        response = requests.get(url)
        response.raise_for_status()  # Check for any errors in the HTTP response
        soup = BeautifulSoup(response.content, 'html.parser')
        class_elements = soup.find_all(class_=class_name)
        if len(class_elements) >= 3:
            class_info_sz = class_elements[0].text.strip()  # Remove leading and trailing spaces or newlines

    except requests.RequestException as e:
        return f"An error occurred: {e}"

def find_class_info_gz(url, class_name):
    global class_info_gz
    try:
        response = requests.get(url)
        response.raise_for_status()  # Check for any errors in the HTTP response
        soup = BeautifulSoup(response.content, 'html.parser')
        class_elements = soup.find_all(class_=class_name)
        if len(class_elements) >= 3:
            class_info_gz = class_elements[0].text.strip()  # Remove leading and trailing spaces or newlines

    except requests.RequestException as e:
        return f"An error occurred: {e}"

def find_class_info_sc(url, class_name):
    global class_info_sc
    try:
        response = requests.get(url)
        response.raise_for_status()  # Check for any errors in the HTTP response
        soup = BeautifulSoup(response.content, 'html.parser')
        class_elements = soup.find_all(class_=class_name)
        if len(class_elements) >= 3:
            class_info_sc = class_elements[0].text.strip()  # Remove leading and trailing spaces or newlines

    except requests.RequestException as e:
        return f"An error occurred: {e}"

def find_class_info_fj(url, class_name):
    global class_info_fj
    try:
        response = requests.get(url)
        response.raise_for_status()  # Check for any errors in the HTTP response
        soup = BeautifulSoup(response.content, 'html.parser')
        class_elements = soup.find_all(class_=class_name)
        if len(class_elements) >= 3:
            class_info_fj = class_elements[0].text.strip()  # Remove leading and trailing spaces or newlines

    except requests.RequestException as e:
        return f"An error occurred: {e}"
'''
def find_class_info_gz(url, class_name):
    global first_class_info, second_class_info, third_class_info
    try:
        response = requests.get(url)
        response.raise_for_status()  # Check for any errors in the HTTP response
        soup = BeautifulSoup(response.content, 'html.parser')
        class_elements = soup.find_all(class_=class_name)

        # Extract text from the first 6 elements
        class_texts = [element.text.strip() for element in class_elements[:6]]

        # Remove duplicates by converting to a set, then back to a list
        unique_texts = list(set(class_texts))

        # If there are not enough unique elements, keep only the first 3
        if len(unique_texts) < 3:
            unique_texts = class_texts[:3]

        # Assign the first 3 unique elements to the global variables
        first_class_info = unique_texts[0] if len(unique_texts) > 0 else None
        second_class_info = unique_texts[1] if len(unique_texts) > 1 else None
        third_class_info = unique_texts[2] if len(unique_texts) > 2 else None

    except requests.RequestException as e:
        return f"An error occurred: {e}"

url_zh = "https://fofa.info/result?qbase64=cmVnaW9uPSJHdWFuZ2RvbmciICYmIGNpdHk9IlpodWhhaSIgJiYgc2VydmVyPSJ1ZHB4eSI%3D"
url_gz = "https://fofa.info/result?qbase64=cmVnaW9uPSJHdWFuZ2RvbmciICYmIGNpdHk9Ikd1YW5nemhvdSIgJiYgc2VydmVyPSJ1ZHB4eSIg"
url_sz = "https://fofa.info/result?qbase64=cmVnaW9uPSJHdWFuZ2RvbmciICYmIGNpdHk9IlNoZW56aGVuIiAmJiBzZXJ2ZXI9InVkcHh5Ig%3D%3D"
url_sc = "https://fofa.info/result?qbase64=cmVnaW9uPSJTaWNodWFuIiAgJiYgc2VydmVyPSJ1ZHB4eSI%3D"
url_fj = "https://fofa.info/result?qbase64=cmVnaW9uPSJGdWppYW4iICYmIHNlcnZlcj0idWRweHki"
class_name = "hsxa-host"

'''
result_gz = find_class_info_gz(url_gz, class_name)
result_zh = find_class_info_zh(url_zh, class_name)
result_sz = find_class_info_sz(url_sz, class_name)
result_sc = find_class_info_sc(url_sc, class_name)
result_fj = find_class_info_fj(url_fj, class_name)
'''
result_gz = find_class_info_gz(url_gz, class_name)

with open("old.m3u", 'r') as old:
    old_lines = old.readlines()
    if len(old_lines) >= 5:
        old_ip_address_1 = old_lines[0].strip()
        old_ip_address_2 = old_lines[1].strip()
        old_ip_address_3 = old_lines[2].strip()
        old_ip_address_4 = old_lines[3].strip()
        old_ip_address_5 = old_lines[4].strip()
'''
with open("TV.m3u", 'r', encoding='utf-8') as file:
    lines = file.readlines()
    with open("TV.m3u", 'w', encoding='utf-8') as file:
        for line in lines:
            line = line.strip()
            if old_ip_address_1 in line:
                line = line.replace(old_ip_address_1, class_info_zh)
            if old_ip_address_2 in line:
                line = line.replace(old_ip_address_2, class_info_gz)
            if old_ip_address_3 in line:
                line = line.replace(old_ip_address_3, class_info_sz)
            if old_ip_address_4 in line:
                line = line.replace(old_ip_address_4, class_info_sc)
            if old_ip_address_5 in line:
                line = line.replace(old_ip_address_5, class_info_fj)
            file.write(line + '\n')

with open("old.m3u", 'w') as file:
    file.write(f"{class_info_zh}" + "\n" + f"{class_info_gz}" + "\n" + f"{class_info_sz}" + "\n" + f"{class_info_sc}" + "\n" +f"{class_info_fj}")
'''

with open("TV.m3u", 'r', encoding='utf-8') as file:
    lines = file.readlines()
    with open("TV.m3u", 'w', encoding='utf-8') as file:
        for line in lines:
            line = line.strip()
            if old_ip_address_1 in line:
                line = line.replace(old_ip_address_1, first_class_info)
            if old_ip_address_2 in line:
                line = line.replace(old_ip_address_2, second_class_info)
            if old_ip_address_3 in line:
                line = line.replace(old_ip_address_3, third_class_info)
            file.write(line + '\n')

with open("old.m3u", 'w') as file:
    file.write(f"{first_class_info}" + "\n" + f"{csecond_class_info}" + "\n" + f"{third_class_info}")
