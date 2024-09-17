import requests
import time
from bs4 import BeautifulSoup
import urllib.request
import urllib.error

MAX_ELEMENTS = 20  # 用常量替代魔法数字

# capture IPs
def find_class_info(url, class_name):
    try:
        response = requests.get(url)
        response.raise_for_status()  # 检查 HTTP 响应状态
        soup = BeautifulSoup(response.content, 'html.parser')
        class_elements = soup.find_all(class_=class_name)

        if not class_elements:  # 检查是否找到了任何匹配的元素
            return f"No elements with class '{class_name}' found."

        unique_elements = set()  # 用来存储不重复的元素
        for element in class_elements:
            element_text = element.text.strip()
            if element_text not in unique_elements:  # 确保是不重复的元素
                unique_elements.add(element_text)
                print(element_text)

            if len(unique_elements) >= MAX_ELEMENTS:  # 控制元素数量
                break

        # 将不重复的元素集合传入 test_url 函数
        result = test_url(unique_elements)
        return result

    except requests.RequestException as e:
        return f"An error occurred: {e}"

# test IP if ok
def test_url(ips):
    min_time = float('inf')  # 初始化最短时间为正无穷大
    best_ip = None           # 初始化最优 ip

    for ip in ips:           # 逐一访问集合中的每个 ip
        try:
            full_url = "http://" + ip + "/udp/239.77.0.4:5146" # 广东新闻
            print(full_url)
            start_time = int(round(time.time() * 1000))
            code = urllib.request.urlopen(full_url).getcode()
            print("Testing: " + ip)
            if code == 200:
                end_time = int(round(time.time() * 1000))
                use_time = end_time - start_time
                print(ip + " is valid, use time is: " + str(use_time))
                # 如果当前 URL 的访问时间小于已知最短时间，更新最短时间和最优 URL
                if use_time < min_time:
                    min_time = use_time
                    best_ip = ip
        except urllib.error.URLError:
            print(ip + " is not valid")
            continue  # 如果访问 URL 发生异常，跳过该 URL
        except Exception as e:
            print(f"Unexpected error with {ip}: {e}")
            continue
    print (str(best_ip) + " useTime : " + str(min_time))
    return best_ip  # 返回访问耗时最短的 URL



url_zh = "https://fofa.info/result?qbase64=cmVnaW9uPSJHdWFuZ2RvbmciICYmIGNpdHk9IlpodWhhaSIgJiYgc2VydmVyPSJ1ZHB4eSI%3D&page=1&page_size=20"
url_gz = "https://fofa.info/result?qbase64=cmVnaW9uPSJHdWFuZ2RvbmciICYmIGNpdHk9Ikd1YW5nemhvdSIgJiYgc2VydmVyPSJ1ZHB4eSIg&page=1&page_size=20"
url_sz = "https://fofa.info/result?qbase64=cmVnaW9uPSJHdWFuZ2RvbmciICYmIGNpdHk9IlNoZW56aGVuIiAmJiBzZXJ2ZXI9InVkcHh5Ig%3D%3D&page=1&page_size=20"
url_sc = "https://fofa.info/result?qbase64=cmVnaW9uPSJTaWNodWFuIiAgJiYgc2VydmVyPSJ1ZHB4eSI%3D&page=1&page_size=20"
url_fj = "https://fofa.info/result?qbase64=cmVnaW9uPSJGdWppYW4iICYmIHNlcnZlcj0idWRweHki"
class_name = "hsxa-host"

# capture old IP
with open("old.m3u", 'r') as old:
    old_lines = old.readlines()
    if len(old_lines) >= 3:
        old_ip_address_zh = old_lines[0].strip()
        old_ip_address_gz = old_lines[1].strip()
        old_ip_address_sz = old_lines[2].strip()
        old_ip_address_sc = old_lines[3].strip()

# get new valid IP
print ("Test GZ")
result_gz = find_class_info(url_gz, class_name)
print ("Finish testing GZ" + "\n")

print ("Test ZH")
result_zh = find_class_info(url_zh, class_name)
print ("Finish testing ZH" + "\n")

print ("Test SZ")
result_sz = find_class_info(url_sz, class_name)
print ("Finish testing SZ" + "\n")

print ("Test SC")
result_sc = find_class_info(url_sc, class_name)
print ("Finish testing SC" + "\n")

# if no valid IP, using the old IP:
if result_gz == None:
    result_gz = old_ip_address_gz
if result_zh == None:
    result_zh = old_ip_address_zh
if result_sz == None:
    result_sz = old_ip_address_sz
if result_sc == None:
    result_sc = old_ip_address_sc

# update new valid IP to TV file
with open(r"C:\Users\lizon\Desktop\TV.m3u", 'r', encoding='utf-8') as file:
    lines = file.readlines()
    with open(r"C:\Users\lizon\Desktop\TV.m3u", 'w', encoding='utf-8') as file:
        for line in lines:
            line = line.strip()
            if old_ip_address_zh in line:
                line = line.replace(old_ip_address_zh, result_zh)
            if old_ip_address_gz in line:
                line = line.replace(old_ip_address_gz, result_gz)
            if old_ip_address_sz in line:
                line = line.replace(old_ip_address_sz, result_sz)
            if old_ip_address_sc in line:
                line = line.replace(old_ip_address_sc, result_sc)
            file.write(line + '\n')

#save new valid IP
with open(r"C:\Users\lizon\Desktop\old.m3u", 'w') as file:
#    file.write(f"{result_zh}" + "\n" + f"{result_gz}"+"\n" + f"{result_sz}"+"\n" + f"{result_sc}" +"\n" + f"{result_fj}")
    file.write(f"{result_zh}" + "\n" + f"{result_gz}"+"\n" + f"{result_sz}"+"\n" + f"{result_sc}")
