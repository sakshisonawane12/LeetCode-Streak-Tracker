# [LeetCode Streak Tracker](https://azeemidrisi.github.io/LeetCode-Streak-Tracker/)

__LeetCode Streak Tracker__ is a powerful Python script that automates the tracking of daily unofficial LeetCode streaks. It's perfect for those who love a little friendly competition, allowing users to compete against their friends to maintain the longest streak. With automatic updates every day, it's never been easier to stay on top of your game.

**Are you doing 100 days of code challenge?**

Add your LeetCode username to `usernames.txt` and make a pull request to see your streaks on the page.

## Features

- Track daily non-contest LeetCode streaks for multiple users.
- Add friends to the competition and view their streaks using their username only.
- Leaderboard to display the longest streaks among friends.
- Daily automatic updates.

## Screenshot
<img width="1000px" src="https://github.com/AzeemIdrisi/LeetCode-Streak-Tracker/assets/112647789/a3db31e0-4adb-4a05-b360-f262b40d218e"/>

## Requirements

- Python
- Selenium
- BeautifulSoup
- LXML
- Firefox

## Installation

### GitHub Actions
1. Fork this repository.
2. Enable GitHub actions workflow associated with the repository.
3. Enable GitHub Pages for this repository to see deployed page.

### Local
1. Clone the repository:

   ```sh
   git clone https://github.com/AzeemIdrisi/leetcode-streak-tracker.git
   ```

2. Install the required dependencies:

   ```sh
   pip install selenium beautifulsoup4 lxml
   ```

3. Download the latest version of Firefox from the [official website](https://www.mozilla.org/en-US/firefox/new/) if you haven't already.

> [!NOTE] 
> Chrome version does not work properly hence Firefox is recommended

4. Create a file `usernames.txt`:
- Add each user's username in new line (Do not leave any empty lines at last).
- Example:
```
AzeemIdrisi
MridulTiwari
k-Sameer_701
```

5. Run the program:

   ```sh
   python main.py
   ```

## Contributing

Contributions are welcome! Please open an issue or submit a pull request with your suggestions.

## License

This project is licensed under the GPL License - see the [LICENSE](LICENSE) file for details.

