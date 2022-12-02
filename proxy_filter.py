import requests
from bs4 import BeautifulSoup
# with open("Free_Proxy_List.txt", "r", encoding="utf-8") as f:
#     data = f.read()
#     data = data.split("\n")

# with open("free_proxy.txt", "w") as f:  # from the proxyscrape
#     for i in data:
#         dt = i.split(",")
#         check = 7
#         while True:
#             try:
#                 if not dt[check] == "port":
#                     if int(dt[check].replace('"','')):
#                         pass
#                 break
#             except:
#                 check += 1
#         dt = dt[0]+":"+dt[check]+"\n"
#         f.write(dt.replace('"', ''))

# with open("free_proxy.txt", "r") as f:
#     data = f.read()
#     data = data.split("\n")
#
# with open("free_proxy.txt", "w") as f:
#     data = list(dict.fromkeys(data))
#     for i in data:
#         f.write(i+"\n")

with open("free_proxy.txt", "r") as f:
    data = f.read()
    data = data.split("\n")

succeed = []
for proxy in data:
    try:
        url1 = f"https://www.dotabuff.com/players/876222934/matches?enhance=overview&lobby_type=ranked_matchmaking&page=1"
        html1 = requests.get(url1, params=None, proxies={'http': proxy, 'https': proxy})
        soup1 = BeautifulSoup(html1.text, 'html.parser')
        matches_ = soup1.find('section')
        if not matches_:
            print("bruh")
        else:
            matches_ = matches_.find_next('section').find_next('section').find('tbody').find_all("tr")
        print("succeed " + proxy)
        succeed.append(proxy)
    except:
        print("failed")

with open("checked.txt", "w") as f:
    for i in succeed:
        f.write(i+"\n")