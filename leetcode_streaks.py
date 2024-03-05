from bs4 import BeautifulSoup
import requests

with open("usernames.txt", "r") as file:
    streaks = dict()
    usernames = file.read().split("\n")
    for username in usernames:
        print(f"Getting streaks for {username}...")
        html_text = requests.get(f"https://leetcode.com/{username}").text
        soup = BeautifulSoup(html_text, "lxml")
        rectangles = soup.find_all("rect", class_="cursor-pointer")

        for i in range(len(rectangles)):
            rectangles[i] = str(rectangles[i].get("fill")).find("green")

        streak = 0
        i = len(rectangles) - 1
        while rectangles[i] != -1:
            streak += 1
            i -= 1
        if streak == 0:
            i = len(rectangles) - 2
            while rectangles[i] != -1:
                streak += 1
                i -= 1
        streaks[username] = streak
        print("Done.")

    def value_getter(item):
        """helper function for sorting according to values, returns value"""
        return item[1]

    streaks = sorted(streaks.items(), key=value_getter, reverse=True)

    print("\n🔥 STREAKS 🔥\n")

    for username in streaks:
        print(username[0], ":", username[1])
