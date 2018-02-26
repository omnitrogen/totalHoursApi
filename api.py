from flask_api import FlaskAPI
from ics import Calendar
import requests
import arrow

app = FlaskAPI(__name__)

@app.route('/')
def example():
    url = "http://planning.isep.fr/Telechargements/ical/EdT_DEFRANCE_Felix.ics?version=2017.0.3.5&idICal=7A5727D5CB08E04B8C4ABC5071874F49&param=643d5b312e2e36325d2666683d3126663d31"
    c = Calendar(requests.get(url).text)
    listeEvAVenir = [i for i in c.events if arrow.utcnow() < i.begin]
    totalDur = 0
    for elt in listeEvAVenir:
        totalDur += elt.duration.seconds // 3600
    return {'totalHours': totalDur}

if __name__ == "__main__":
    app.run()