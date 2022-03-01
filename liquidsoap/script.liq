set("init.allow_root",true)

# Log dir
set("log.file.path","/var/log/liquidsoap/radioliq.log")

# Serveur settings
set("harbor.bind_addr","0.0.0.0")

icecast_source_password = getenv("ICECAST_SOURCE_PASSWORD")
liquidsoap_source_password = getenv("LIQUIDSOAP_SOURCE_PASSWORD")
api_server_host = getenv("API_SERVER_HOST")
icecast_server_host = getenv("ICECAST_SERVER_HOST")

log("icecast_source_password: #{icecast_source_password}")
log("liquidsoap_source_password: #{liquidsoap_source_password}")
log("api_server_host: #{api_server_host}")

def get_schedule_file() = 
  # Get the URI
  lines = get_process_lines("curl #{api_server_host}/scheduler/v1/next/")
  uri = list.hd(default="",lines)
  log("Music from server: #{uri}")
  request.create(uri)
end

# An emergency file
emergency = single("./music/emergency.mp3")

# A playlist
scheduled = request.dynamic(id="schedule", get_schedule_file)

# A live source
live = input.harbor(
       "mount",
       port=8080,
       password=liquidsoap_source_password
)
radio = fallback(track_sensitive=false, [live,scheduled])

# fallback
radio = fallback(track_sensitive=false, [radio,emergency])
radio = mksafe(radio)

# Stream it out
output.icecast(
    %mp3,
    host = icecast_server_host,
    mount = "stream",
    user = "source",
    public = true,
    port = 80,
    password = icecast_source_password,
    genre = "Surprise",
    name = "RadioStream",
    radio)