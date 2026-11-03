
# 8-7 Album: Store an artist and album in a dictionary.
def make_album(artist, title, songs=None):
    album = {"artist": artist, "title": title}
    if songs is not None:
        album["songs"] = songs
    return album


print(make_album("Kendrick Lamar", "DAMN."))
print(make_album("Travis Scott", "ASTROWORLD"))
print(make_album("J. Cole", "2014 Forest Hills Drive", 13))
