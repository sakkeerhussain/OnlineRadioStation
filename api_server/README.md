
@app.route("/next")
def next_track():
    global iteration_test
    if iteration_test == 0:
        resp = './test-files-server-flask/music/Gunda-Gunda-Gundajayan-Shabareesh-Varma.mp3'
    elif iteration_test == 1:
        resp = './test-files-server-flask/music/Kannamma--From-Veyil--Pradeep-Kumar.mp3'
    else:
        resp = './test-files-server-flask/music/sample-3s.mp3'

    iteration_test = (iteration_test + 1) % 3
    return resp
    # return 'annotate:title="Chamakay",artist="Blood Orange",album="Cupid Deluxe":http://localhost:5000/music/sample-3s.mp3'
