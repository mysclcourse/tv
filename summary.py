import requests
from bs4 import BeautifulSoup
def find_class_info(url, class_name):
    global first_class_info, second_class_info, third_class_info
    try:
        response = requests.get(url)
        response.raise_for_status()  # Check for any errors in the HTTP response
        soup = BeautifulSoup(response.content, 'html.parser')
        class_elements = soup.find_all(class_=class_name)
        if len(class_elements) >= 3:
            first_class_info = class_elements[0].text.strip()  # Remove leading and trailing spaces or newlines
            second_class_info = class_elements[1].text.strip()  # Remove leading and trailing spaces or newlines
            third_class_info = class_elements[2].text.strip()  # Remove leading and trailing spaces or newlines
    except requests.RequestException as e:
        return f"An error occurred: {e}"

url = "https://fofa.info/result?qbase64=cmVnaW9uPSJHdWFuZ2RvbmciICYmIGNpdHk9Ikd1YW5nemhvdSIgJiYgc2VydmVyPSJ1ZHB4eSIg"
class_name = "hsxa-host"
result = find_class_info(url, class_name)

with open(r"C:\Users\user\Desktop\old.m3u", 'r') as old:
    old_lines = old.readlines()
    if len(old_lines) >= 3:
        old_ip_address_1 = old_lines[0].strip()
        old_ip_address_2 = old_lines[1].strip()
        old_ip_address_3 = old_lines[2].strip()

with open(r"C:\Users\user\Desktop\TV.m3u", 'r', encoding='utf-8') as file:
    lines = file.readlines()
    with open(r"C:\Users\user\Desktop\TV.m3u", 'w', encoding='utf-8') as file:
        for line in lines:
            line = line.strip()
            if old_ip_address_1 in line:
                line = line.replace(old_ip_address_1, first_class_info)
            if old_ip_address_2 in line:
                line = line.replace(old_ip_address_2, second_class_info)
            if old_ip_address_3 in line:
                line = line.replace(old_ip_address_3, third_class_info)
            file.write(line + '\n')
