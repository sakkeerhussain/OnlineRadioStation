set("init.allow_root",true)

# Log dir
set("log.file.path","/var/log/liquidsoap-out.log")

# Serveur settings
set("harbor.bind_addr","0.0.0.0")

def get_schedule_file() = 
  # Get the URI
  # lines = get_process_lines("curl http://localhost:5000/scheduler/v1/next/")
  lines = get_process_lines("curl http://host.docker.internal:5000/scheduler/v1/next/")
  uri = list.hd(default="",lines)
  log("play: #{uri}")
  request.create(uri)
end

# An emergency file
emergency = single("./music/emergency.mp3")

# A playlist
# sceduled = playlist(mode="normal","./music/songs",reload_mode="watch")
# sceduled = random([sceduled])
sceduled = request.dynamic(id="schedule", get_schedule_file)

# A live source
live = input.harbor(
       "mount",
       port=8080,
       password="tomsradio321"
)
radio = fallback(track_sensitive=false, [live,sceduled])

# fallback
radio = fallback(track_sensitive=false, [radio,emergency])
radio = mksafe(radio)

# Stream it out
output.icecast(
    %mp3,
    host = "host.docker.internal",
    mount = "stream",
    user = "source",
    public = true,
    port = 8000, password = "tomsradio",
    genre = "Surprise",
    name = "TomsRadioStream",
    radio)