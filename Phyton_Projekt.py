#importieren der benötigten Bibliotheken 
import smtplib, ssl
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from urllib.request import Request, urlopen
from bs4 import BeautifulSoup
from pathlib import Path

def parseSourceCode(my_url):
    #Header-Parameter
    hdr = {'User-Agent': 'Mozilla/5.0'}
    #URL anfordern mithilfe des Header-Parameter
    req = Request(my_url,headers=hdr)
    #öffnen der URL
    uClient = urlopen(req)
    #Lesen der Seite
    page_html = uClient.read() 
    uClient.close()
    #Code mit BeautifulSoup parsen
    return BeautifulSoup(page_html, "html.parser") 

#URL auf die zugegriffen wird
bundesliga_source = parseSourceCode("https://www.kicker.de/bundesliga/torjaeger/2020-21/")
#definieren der Tabelle, sowie Ort des Inhaltes auf der Webseite
tabelle = bundesliga_source.find("table", {"class": "kick__table kick__table--ranking kick__table--alternate kick__table--resptabelle"})
 
def Emailsenden():
    #Absender Email Adresse
    sender_email = "Absender der Email-Adresse"
    #Empfänger Email Adresse
    receiver_email = "Empfänger-Email-Adresse"
    #Passwort
    password = "Passwort des Absender-Email-Kontos"

    #Aufteilen der einzelnen Parts der Email
    message = MIMEMultipart("alternative")
    #Betreff
    message["Subject"] = "Die aktuellen Top-Torschützen der Fussball-Bundesliga"
    #beide darauffolgenden Parts
    message["From"] = sender_email 
    message["To"] = receiver_email

    #beschreiben des Email-textes und HTML-Parts
    text = """\
    Hier sieht man eine Auflistung der aktuellen Bundesliga-Torschützen"""
    html = ("""\
    <html>
      <body>
        <h1>Hier siehst du die aktuellen Toptorschützen der Bundesliga. </h1>       
        """
    +str(tabelle)#einfügen der oben definierten Tabelle
    +"""
      </body>
    </html>
    """)

    #erster Part der Email(Text)
    part1 = MIMEText(text, "plain")
    #zweiter Part 'html-basiert' der Email
    part2 = MIMEText(html, "html") 

    #hinzufügen des beiden Parts zur Email
    message.attach(part1)
    message.attach(part2)

    #sichere Connection zum Server 
    context = ssl.create_default_context()
    #erstellt die Verbindung zu Gmail
    with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as server:
        #loggt sich in den Server ein
        server.login(sender_email, password)
        #sendet die Email vom Server
        server.sendmail(
            sender_email, receiver_email, message.as_string() 
        )

#definition eines bodys, welcher von der zugehörigen Webseite stammt
body = bundesliga_source.find("tbody")
#Ort des Namens des Erstplatzierten der Torjägerliste
Toptorjaeger = body.find("a", {"class": "kick__table--ranking__playername"})
#erstellen der Textdatei, indem der Name des Erstplatzierten steht
path = Path("Toptorjaeger.txt")

#prüfen der Vorhandenheit des Dokuments
if path.is_file():
    #Öffnen der Datei "Toptorjaeger"
    with open("Toptorjaeger.txt","r+") as datei:
        #lesen der Datei
        bisherigerToptorjaeger = datei.read()
        #abgleichen der Dtei mit dem Inhalt der Webseite(Ist der Toptorjaeger immer noch derselbe?)
        if bisherigerToptorjaeger == str(Toptorjaeger.contents):
            #ausgeben folgenden Satzes, wenn der Toptorjaeger gleich geblieben ist
            print("Der Toptorjaeger der Fussball-Bundesliga hat sich nicht verändert")
            exit()
        #trifft zu, wenn sich der Toptorjäger verändert hat
        else:
            #öffnet die Datei und schreibt den neuen Toptorjaeger rein
            datei.write(str(Toptorjaeger.contents))
            #schließen der Datei
            datei.close()
            #Email mit der Tabelle der aktuelle Torjäger wird versendet
            Emailsenden()
#ist keine Datei mit dem Torjäger vorhanden:
else:
    #öffnen und auslesen der Textdatei
    with open("Toptorjaeger.txt","w") as datei:
        #schreibt in die Datei den Namend des Toptorjaegers
        datei.write(str(Toptorjaeger.contents))
        #Schließen der Datei
        datei.close()
        #Email mit der Tabelle der aktuelle Torjäger wird versendet
        Emailsenden()

    


