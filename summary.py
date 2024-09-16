import requests
from bs4 import BeautifulSoup
import urllib.request

# capture IPs
def find_class_info(url, class_name):
    try:
        response = requests.get(url)
        response.raise_for_status()  # 检查 HTTP 响应状态
        soup = BeautifulSoup(response.content, 'html.parser')
        class_elements = soup.find_all(class_=class_name)

        if not class_elements:  # 检查是否找到了任何匹配的元素
            return f"No elements with class '{class_name}' found."

        for i, element in enumerate(class_elements):
            if i <= 1:  # 遍历前10个元素
                code_response = test_url(element.text.strip())
                if code_response == 200:
                    return element.text.strip()
            else:
                break

        return 0

    except requests.RequestException as e:
        return f"An error occurred: {e}"

# test IP if ok
def test_url(ip):
    full_url = "http://" + ip + "/udp/239.77.0.4:5146"
    try:
        code = urllib.request.urlopen(full_url).getcode()
    except Exception as e:  # 捕获可能的网络或 HTTP 错误
        return 0  # 返回0表示URL不可用
    return code



url_zh = "https://fofa.info/result?qbase64=cmVnaW9uPSJHdWFuZ2RvbmciICYmIGNpdHk9IlpodWhhaSIgJiYgc2VydmVyPSJ1ZHB4eSI%3D"
url_gz = "https://fofa.info/result?qbase64=cmVnaW9uPSJHdWFuZ2RvbmciICYmIGNpdHk9Ikd1YW5nemhvdSIgJiYgc2VydmVyPSJ1ZHB4eSIg"
url_sz = "https://fofa.info/result?qbase64=cmVnaW9uPSJHdWFuZ2RvbmciICYmIGNpdHk9IlNoZW56aGVuIiAmJiBzZXJ2ZXI9InVkcHh5Ig%3D%3D"
url_sc = "https://fofa.info/result?qbase64=cmVnaW9uPSJTaWNodWFuIiAgJiYgc2VydmVyPSJ1ZHB4eSI%3D"
url_fj = "https://fofa.info/result?qbase64=cmVnaW9uPSJGdWppYW4iICYmIHNlcnZlcj0idWRweHki"
class_name = "hsxa-host"

# capture old IP
with open("old.m3u", 'r') as old:
    old_lines = old.readlines()
    if len(old_lines) >= 2:
        old_ip_address_zh = old_lines[0].strip()
        old_ip_address_gz = old_lines[1].strip()
        old_ip_address_sz = old_lines[2].strip()

# get new valid IP
result_gz = find_class_info(url_gz, class_name)
result_zh = find_class_info(url_zh, class_name)
result_sz = find_class_info(url_sz, class_name)

# if still no find valid IP, using the old IP:
if result_gz == 0:
    result_gz = old_ip_address_gz
if result_zh == 0:
    result_zh = old_ip_address_zh
if result_sz == 0:
    result_sz = old_ip_address_sz

# up new valid IP to TV file
with open("TV.m3u", 'r', encoding='utf-8') as file:
    lines = file.readlines()
    with open("TV.m3u", 'w', encoding='utf-8') as file:
        for line in lines:
            line = line.strip()
            if old_ip_address_zh in line:
                line = line.replace(old_ip_address_zh, result_zh)
            if old_ip_address_gz in line:
                line = line.replace(old_ip_address_gz, result_gz)
            if old_ip_address_sz in line:
                line = line.replace(old_ip_address_sz, result_sz)
            file.write(line + '\n')

#save new valid IP
with open("old.m3u", 'w') as file:
#    file.write(f"{result_zh}" + "\n" + f"{result_gz}"+"\n" + f"{result_sz}"+"\n" + f"{result_sc}" +"\n" + f"{result_fj}")
    file.write(f"{result_zh}" + "\n" + f"{result_gz}"+"\n" + f"{result_sz}"+"\n")
