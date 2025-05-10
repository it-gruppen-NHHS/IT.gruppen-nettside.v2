# Genreisk framework 
## Hvordan komme i gang med nytt prosjekt
1. Åpne en bash terminal, og skriv følgende `. create.sh`
- Denne vil kjøre et shell script som setter opp kodebasen med unike nøkler, og endrer på nødvendige configs. Når denne er ferdig skal appen i bunn og grunn være klar for å jobbes med.
- Default templaten er ikke konfigurert med databasetilkobling eller google login.

## Hvordan komme igang med lokal utvikling?
1. Clone prosjektet ved å kopiere SSH linken, og skriv inn følgende kommando i terminalen (Windows: Git Bash) 

Windows:
``` bash
git clone <url> <file_path>
```
Mac:
``` terminal
git clone <url> <file_path>
```

2. Åpne prosjektet i din IDE
3. Virtual environment \
Førstegang må du lage et virtual environment: 

Windows:
``` terminal
python -m venv .venv
```
Mac:
``` terminal
python3 -m venv .venv
```

4. Så må vi aktivere virtual environment, dette må gjøres hver gang du åpner prosjektet 

Windows:
``` terminal
.\.venv\Scripts\activate
```
Mac: 
``` terminal
source .venv/bin/activate
```

5. Installer requirements.txt, dette må gjøres hver gang denne filen blir oppdatert 

Windows:
``` terminal
pip install -r requirements.txt
```
Mac:
``` terminal
python3 -m pip install -r requirements.txt
```

## Hvordan kjører man siden?
For å kjøre siden er det viktig av filepathen er `../<prosjekt>/app` Dersom den ikke er det, vil ikke det interne filsystemet fungere. For å navigere seg inn i `app` folderen, så skriver man følgende kommando
``` bash
cd app
```
Når filepathen er korrekt, så kan man skrive: \
Windows:
``` terminal
py app.py
```
Mac:
``` terminal
python3 app.py
```
Da skal en lokal server starte på pcen/macen deres, og siden skal være tilgjengelig gjennom `localhost:5000` eller `127.0.0.1:5000`


## Hvordan lager man en ny side?
- Lager en ny HTML fil 
1. Høyreklikk på mappen som heter "templates", og velg "new file...". 
2. Skriv inn navnet på filen, og legg til ".html". F.eks. test.html
3. I HTML filen skriv html:5 og trykk på enter. 
4. På linje 7 skriv inn titelen du ønsker at skal dukke opp i fanen
5. Etter body-tagen skriv inn følgende 
    ```
    {% extends "template.html" %}
    {% set active_page = "home" %}
    {% block content %}


    {% endblock %} 
    ```
6. Endre set active_page til navnet på filen under .html på slutten
- Lage ny route i app.py
1. Åpne filen app.py
2. Legg til følgende kode der du føler det er relevant
``` python
@app.route("/<navn_på_routen", methods=['GET', 'POST'])
def <navn_på_routen>():
    return flask.render_template("<navn_på_html_siden>")
```
Dette er en veldig kort beskrivelse av hvordan man lager en ny side, og tilhørende backend logikk. 


## Sette opp ny database
Følgende kode må limes inn i `config.py:`
``` python
app.config['SQLALCHEMY_DATABASE_URI'] = f"mysql+pymysql://{os.getenv('MY_SQL_USER')}:{os.getenv('MY_SQL_PASSWORD')}@{os.getenv('MY_SQL_URL')}/vareflyt"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
app.config['SQLALCHEMY_POOL_SIZE'] = 50
app.config['SQLALCHEMY_MAX_OVERFLOW'] = 50
```

``` python
with app.app_context():
    db.init_app(app) #adds the app to the database from models.py
    db.create_all()
```


## Koble til Google sign in
Følgende kode må limes inn i `config.py:`.
``` python

GOOGLE_CLIENT_ID = "<google_client_id>"
GOOGLE_CLIENT_SECRET = "<google_client_secret>"
GOOGLE_DISCOVERY_URL = (
    "https://accounts.google.com/.well-known/openid-configuration"
)
client_secret = os.path.join(pathlib.Path(__file__).parent, "client_secret.json")

if mode == 'production':
    app.config['DEBUG'] = False
    flow = Flow.from_client_secrets_file(client_secrets_file = client_secret, 
                    scopes = ["https://www.googleapis.com/auth/userinfo.email", "https://www.googleapis.com/auth/userinfo.profile", "openid"],
                    redirect_uri= "https://www.<prod_name>.nhhs.no/callback" )
else :
    flow = Flow.from_client_secrets_file(client_secrets_file = client_secret, 
                    scopes = ["https://www.googleapis.com/auth/userinfo.email", "https://www.googleapis.com/auth/userinfo.profile", "openid"],
                    redirect_uri= "http://localhost:5000/callback" )


client  = WebApplicationClient(GOOGLE_CLIENT_ID)

```



 




