
# 8-8 User Albums: Ask for album information until the user quits.
def make_album(artist, title):
    return {"artist": artist, "title": title}


while True:
    artist = input("Enter an artist (or quit): ")
    if artist.lower() == "quit":
        break

    title = input("Enter an album title (or quit): ")
    if title.lower() == "quit":
        break

    print(make_album(artist, title))
