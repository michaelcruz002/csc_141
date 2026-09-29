current_users = {"admin": "password123", "michael": "mysecretpassword", "xxGamerzxx": "gamerpass", "jaden": "jaden123", "kitty": "kittylove"}

new_users = ["admin", "michael", "xxGamerzxx", "jaden", "kitty"]

current_users_lowered = [username.lower() for username in current_users]

for new_user in new_users:
    if new_user.lower() in current_users_lowered:
        print(f"{new_user} is already taken.")
        continue
    print(f"{new_user} is available.")