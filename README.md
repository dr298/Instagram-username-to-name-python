# Instagram-username-to-name-python
Scrap instagram name with username input


## Instagram Username Scraper
This Python script scrapes Instagram profiles for the name associated with a given username. It reads a list of usernames from a file, processes each username, and saves the results to another file.

## Usage
Ensure that you have Python, requests, and BeautifulSoup installed.
Save the script to your desired directory.
Create a file named username.txt in the same directory, containing the list of usernames to be scraped, with each username on a separate line.
Run the script by executing python username_scraper.py.
The script will process each username in the username.txt file and save the results to a file named result.txt. The format of the results file is <username> : <name>, where <username> is the username being scraped and <name> is the name associated with that username (if found).

## Example
Suppose we have a file named username.txt containing the following usernames:
```
john_doe
jane_smith
foo_bar
```

After running the script, we would have a file named result.txt containing the following:
```
john_doe : John Doe
jane_smith : Jane Smith
foo_bar : Not Found.
```

### Note: This tool is for educational purposes only. Use it at your own risk. The author is not responsible for any illegal activities conducted using this tool.

## License
This project is licensed under the MIT License.

Support me at : https://trakteer.id/dr298
[![@dr298's Holopin board](https://holopin.me/dr298)](https://holopin.io/@dr298)
