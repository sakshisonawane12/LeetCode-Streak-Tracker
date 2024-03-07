from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from bs4 import BeautifulSoup

options = webdriver.FirefoxOptions()
options.add_argument("--headless")
driver = webdriver.Firefox(options=options)


with open("usernames.txt", "r") as file:
    streaks = dict()
    usernames = file.read().split("\n")
    for username in usernames:
        print(f"Getting streaks for {username}...")
        driver.get(f"https://leetcode.com/{username}")
        element = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.TAG_NAME, "rect"))
        )
        html_text = driver.page_source
        soup = BeautifulSoup(html_text, "lxml")
        rectangles = soup.find_all("rect", class_="cursor-pointer")

        for i in range(len(rectangles)):
            rectangles[i] = str(rectangles[i].get("fill")).find("green")

        streak = 0
        i = len(rectangles) - 1

        # Checking if you have not submitted today's question yet
        if rectangles[i] == -1:
            i -= 1
        while rectangles[i] != -1:
            streak += 1
            i -= 1
        # if streak == 0:
        #     i = len(rectangles) - 2
        #     while rectangles[i] != -1:
        #         streak += 1
        #         i -= 1
        streaks[username] = streak
        print("Done.")

    def value_getter(item):
        """helper function for sorting according to values, returns value"""
        return item[1]

    streaks = sorted(streaks.items(), key=value_getter, reverse=True)

    print("\n🔥 STREAKS 🔥\n")

    for username in streaks:
        print(username[0], ":", username[1])

    # HTML Generation
    with open("index.html", "w") as file:
        pass
    with open("index.html", "a") as f:
        with open("./templates/body.html", "r") as body:
            f.write(body.read())

        rank = 1
        for username, streak in streaks:
            if rank <= 3:
                f.write(
                    f'<a href="https://leetcode.com/{username}"><li>&#12935{rank}; <span>{username}</span> : {streak}</li></a>'
                )
                rank += 1
            else:
                f.write(
                    f'<a href="https://leetcode.com/{username}"><li><span>{username}</span> : {streak}</li></a>'
                )

        with open("./templates/footer.html", "r") as footer:
            f.write(footer.read())

    print("Streaks saved to index.html")
