import requests
from bs4 import BeautifulSoup

# with open("users_filtered.txt", "r") as f:
#     users = f.read().split("\n")
#     users = list(dict.fromkeys(users))
#
# with open("users_filtered.txt", "w") as f:
#     for i in users:
#         f.write(f"{i}\n")

HEADERS = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                  'Chrome/81.0.4044.138 YaBrowser/20.4.2.201 Yowser/2.5 Safari/537.36',
    'accept': '*/*'
}
# id_ = 855450670
# with open("users_filtered_add.txt", "w") as f:
#     url1 = f"https://www.dotabuff.com/players/{id_}/matches"
#     html1 = requests.get(url1, headers=HEADERS, params=None)  # proxies
#     soup1 = BeautifulSoup(html1.text, 'html.parser')
#     matches_ = soup1.find('section')
#     if matches_:
#         matches_ = matches_.find_next('section').find_next('section').find('tbody').find_all("tr")
#         match_count = 0
#         for match in matches_:
#             tds = match.find_all("td")
#             if "Ranked" == tds[4].getText()[:6]:
#                 if "Random Draft" == tds[4].getText()[6:] or \
#                         "All Pick" == tds[4].getText()[6:]:
#                     match_id = tds[3].find("a").get("href").split("/")[-1]
#                     url = f"https://www.dotabuff.com/matches/{match_id}"
#                     html = requests.get(url, headers=HEADERS, params=None)
#                     soup = BeautifulSoup(html.text, 'html.parser').find("div", class_="team-results")
#                     if soup:
#                         soup = soup.find_all("tr")
#                         plrs = soup[2:7] + soup[10:15]
#                         for i in plrs:
#                             id = int(i.attrs.get("class")[-1].split("-")[-1])
#                             if id != id_:
#                                 f.write(f'{id}\n')
#                         if match_count > 46:
#                             break
#                     match_count += 1


with open("to_parse.txt", "r") as f:
    ids = f.read().split("\n")
    f.close()
with open("new_match_ids.txt", "w") as f:
    for id_ in ids:
        page = 1
        flag = True
        while flag:
            url1 = f"https://www.dotabuff.com/players/{id_}/matches?enhance=overview&lobby_type=ranked_matchmaking&page={page}"
            html1 = requests.get(url1, headers=HEADERS, params=None)  # proxies
            soup1 = BeautifulSoup(html1.text, 'html.parser')
            matches_ = soup1.find('section')
            if not matches_:
                print("bruh")
                f.close()
                print(soup1)
                break
            else:
                matches_ = matches_.find_next('section').find_next('section') \
                    .find('tbody').find_all("tr")
                for match in matches_:
                    tds = match.find_all("td")
                    # if "Ranked" == tds[4].getText()[:6]:
                    if "Random Draft" == tds[4].getText()[6:] or \
                            "All Pick" == tds[4].getText()[6:]:
                        time = tds[3].find("time").get("datetime")[:10]
                        year, month, day = int(time[:4]), int(time[5:7]), int(time[-2:])
                        # if year == 2022:
                        if month > 9:
                            pass
                        elif month == 9:
                            if day < 22:
                                flag = False
                                break
                        elif month < 9:
                            flag = False
                            break
                        match_id = tds[3].find("a").get("href").split("/")[-1]
                        f.write(f"{match_id}\n")
                print(f"{page}")
                page += 1

