import requests
from bs4 import BeautifulSoup
# Print banner and prompt user to continue
print(f"""
         .___      ________  ________  ______  
       __| _/______\_____  \/   __   \/  __  \ 
      / __ |\_  __ \/  ____/\____    />      < 
     / /_/ | |  | \/       \   /    //   --   \\
     \____ | |__|  \_______ \ /____/ \______  /
          \/               \/               \/ 
== good or bad? it depends on your point of view! ==

Follow this step to login to your truecaller account :
1. On Truecaller Android, tap on the 3 line menu on top left then click on setting's.
2. Tap on Privacy Center and then click on Download my data.
3. Now a JSON file is downloaded.
4. Save the JSON file at this tools file location
5. Rename the JSON file to truecaller.json

""")
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
