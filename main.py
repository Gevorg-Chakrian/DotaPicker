import requests
from bs4 import BeautifulSoup


players = {}
HEADERS = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                  'Chrome/81.0.4044.138 YaBrowser/20.4.2.201 Yowser/2.5 Safari/537.36',
    'accept': '*/*'
}
def parse_users():
    sum = 0
    page = 1
    with open("users.txt", "w") as f:
        while True:
            url = f"https://www.dotabuff.com/players/leaderboard?page={page}"
            html = requests.get(url, headers=HEADERS, params=None)
            soup = BeautifulSoup(html.text, 'html.parser')
            players_ = soup.find('tbody').find_all("tr")
            for player in players_:
                matches = int(player.find("td", class_="cell-divider").find("div").contents[0])
                if matches > 5:
                    id_ = int(player.find("a", class_="link-type-player").get("href").split("/")[-1])
                    # players[id_] = id_
                    f.write(f'{id_}\n')
                    url1 = "https://www.dotabuff.com"+player.find("a", class_="link-type-player")\
                                                       .get("href")+"/matches"
                    html1 = requests.get(url1, headers=HEADERS, params=None)
                    soup1 = BeautifulSoup(html1.text, 'html.parser')
                    matches_ = soup1.find('section')
                    if matches_:
                        matches_ = matches_.find_next('section').find_next('section')\
                            .find('tbody').find_all("tr")
                        match_count = 0
                        for match in matches_:
                            tds = match.find_all("td")
                            # match_id_ = tds[3].find("a").get("href").split("/")[-1]
                            # print("match_id ="+match_id_)
                            if "Ranked" == tds[4].getText()[:6]:
                                if "Random Draft" == tds[4].getText()[6:] or \
                                        "All Pick" == tds[4].getText()[6:]:
                                    # time = tds[3].find("time").get("datetime")[:10]
                                    # year, month, day = int(time[:4]), int(time[5:7]), int(time[-2:])
                                    # if year == 2022:
                                    #     if month > 9:
                                    #         pass
                                    #     elif month < 9:
                                    #         break
                                    #     else:
                                    #         if day < 22:
                                    #             break

                                    match_id = tds[3].find("a").get("href").split("/")[-1]
                                    url = f"https://www.dotabuff.com/matches/{match_id}"
                                    html = requests.get(url, headers=HEADERS, params=None)
                                    soup = BeautifulSoup(html.text, 'html.parser').find("div",
                                                                                            class_="team-results")
                                    if soup:
                                        soup = soup.find_all("tr")
                                        plrs = soup[2:7] + soup[10:15]
                                        for i in plrs:
                                            id = int(i.attrs.get("class")[-1].split("-")[-1])
                                            if id != id_:
                                                f.write(f'{id}\n')
                                        if match_count > 6:
                                            break
                                    match_count += 1
            if page == 177:
                f.write(f"matches with duplicates {sum}")
                f.close()
                break
            page += 1
            print(page)


parse_users()
