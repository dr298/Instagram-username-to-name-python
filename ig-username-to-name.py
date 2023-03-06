import requests
from bs4 import BeautifulSoup

# Read usernames from file
with open("username.txt") as f:
    usernames = [line.strip() for line in f]

# Process each username and save results to file
with open("result.txt", "w") as f:
    for username in usernames:
        url = f"https://www.instagram.com/{username}/"
        response = requests.get(url)
        soup = BeautifulSoup(response.content, "html.parser")
        try:
            name = soup.find("title").text.split("•")[0].strip()
            f.write(f"{username} : {name}\n")
            print(f"{username} : {name}")
        except AttributeError:
            f.write(f"{username} : Not Found.\n")
            print(f"{username} : Not Found")
