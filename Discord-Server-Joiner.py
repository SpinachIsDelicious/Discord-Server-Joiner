from time import sleep as wait
from requests import post
from win10toast import ToastNotifier

print("          DISCLAIMER          ")
print("This program is for educational purposes only and is against Discord TOS. Use it at your\nown risk. I am not responsible for anything you do with this tool.")

DELAY = 2.5
# i suggest keeping this value higher the more invite codes, the more tokens you have.
# i might add proxy support in the future
# you should keep the delay higher because you can either get rate limited
# or discord can detect that you're using a self bot and ban your account

INVITE_CODES = []

TOKENS = []

for TOKEN in TOKENS:
    print("New token detected, joining servers...")
    for INVITE_CODE in INVITE_CODES:
        wait(DELAY)
        URL = f"https://discord.com/api/v9/invites/{INVITE_CODE}"
        post(URL, headers={"authorization":TOKEN})
        print("Attempted to send POST request to join server for TOKEN")

ToastNotifier().show_toast("Finished.","Finished the server joining tasks.",icon_path="resources/Discord.ico",duration=10)
input("FINISHED EXECUTING PROGRAM. PRESS ENTER TO CLOSE WINDOW >>> ")