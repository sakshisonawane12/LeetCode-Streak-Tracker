# LeetCode Streak Tracker

LeetCode Streak Tracker is a python script designed to help users track their daily unofficial LeetCode streaks and compete against their friends to maintain the longest streak.

## Features

- Track daily non-contest LeetCode streaks for multiple users.
- Add friends to the competition and view their streaks using their username only.
- Leaderboard to display the longest streaks among friends.

## Screenshot
<img width="400px" src="https://github.com/AzeemIdrisi/LeetCode-Streak-Tracker/assets/112647789/104ced2e-beb1-4d4f-9619-13581377388f"/>

## Requirements

- Python
- Selenium
- BeautifulSoup
- LXML
- Firefox

## Installation

1. Clone the repository:

   ```sh
   git clone https://github.com/your-username/leetcode-streak-tracker.git
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

