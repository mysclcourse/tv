import requests
from bs4 import BeautifulSoup
#def find_class_info(url, class_name):
#    global first_class_info, second_class_info, third_class_info
#    try:
#        response = requests.get(url)
#        response.raise_for_status()  # Check for any errors in the HTTP response
#        soup = BeautifulSoup(response.content, 'html.parser')
#        class_elements = soup.find_all(class_=class_name)
#        if len(class_elements) >= 3:
#            first_class_info = class_elements[0].text.strip()  # Remove leading and trailing spaces or newlines
#            second_class_info = class_elements[1].text.strip()  # Remove leading and trailing spaces or newlines
#            third_class_info = class_elements[2].text.strip()  # Remove leading and trailing spaces or newlines
#    except requests.RequestException as e:
#        return f"An error occurred: {e}"

def find_class_info(url, class_name):
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

url = "https://fofa.info/result?qbase64=cmVnaW9uPSJHdWFuZ2RvbmciICYmIGNpdHk9Ikd1YW5nemhvdSIgJiYgc2VydmVyPSJ1ZHB4eSIg"
class_name = "hsxa-host"
result = find_class_info(url, class_name)

with open("old.m3u", 'r') as old:
    old_lines = old.readlines()
    if len(old_lines) >= 3:
        old_ip_address_1 = old_lines[0].strip()
        old_ip_address_2 = old_lines[1].strip()
        old_ip_address_3 = old_lines[2].strip()

with open("TV-new.m3u", 'r', encoding='utf-8') as file:
    lines = file.readlines()
    with open("TV-new.m3u", 'w', encoding='utf-8') as file:
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
    file.write(f"{first_class_info}"+"\n" +f"{second_class_info}""\n" +f"{third_class_info}")
