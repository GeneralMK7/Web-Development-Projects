import creds
import spotipy
from spotipy.oauth2 import SpotifyOAuth
from billboard_scraping import song_names

#authentication
sp = spotipy.Spotify(
    auth_manager=SpotifyOAuth(
        client_id=creds.SPOTIPY_CLIENT_ID,
        client_secret=creds.SPOTIPY_CLIENT_SECRET,
        redirect_uri=creds.SPOTIPY_REDIRECT_URI,
        scope="playlist-modify-public playlist-modify-private"
    )
)

#creating playlist
user_id = sp.current_user()["id"]
playlist = sp.user_playlist_create(
    user=user_id,
    name="Hot Billboard 100",
    description="Playlist made by using Web scraping of Billboard hot top 100",
    public=False
)

#adding songs via uri
playlist_id = playlist["id"]
track_uri = []
for song in song_names:
    result = sp.search(q=song,type="track",limit=1)
    if result["tracks"]["items"]:
        track_uri.append(result["tracks"]["items"][0]["uri"])
    else:
        print("Not found")

sp.playlist_add_items(playlist_id, track_uri)



