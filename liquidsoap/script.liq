set("init.allow_root",true)

# Log dir
set("log.file.path","./log/liquidsoap/out.log")

# Serveur settings
set("harbor.bind_addr","0.0.0.0")

# An emergency file
emergency = single("./liquidsoap/music/emergency.mp3")

# A playlist
playlist = playlist(mode="normal","./music/songs",reload_mode="watch")
playlist = random([playlist])

# A live source
live = input.harbor(
       "mount",
       port=8080,
       password="tomsradio321"
)
radio = fallback(track_sensitive=false, [live,playlist])

# fallback
radio = fallback(track_sensitive=false, [radio,emergency])
radio = mksafe(radio)

# Stream it out
output.icecast(
    %mp3,
    host = "localhost",
    mount = "stream",
    user = "source",
    public = true,
    port = 8000, password = "tomsradio",
    genre = "Surprise",
    name = "TomsRadioStream",
    radio)