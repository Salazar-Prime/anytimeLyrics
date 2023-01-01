import syncedlyrics

artist = "Tool"
song = "Pneuma"
searchTerm = f"[{song}] [{artist}]"
lrc = syncedlyrics.search(
    searchTerm, allow_plain_format=True, providers=["Deezer", "NetEase"]
)
print(lrc)
