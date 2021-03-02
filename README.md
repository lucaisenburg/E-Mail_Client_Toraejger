# E-Mail_Client_Toraejger
An E-mail_Client, which sends you an E-mail, if the first place on the goalgetter ranking of the Bundesliag (football) has recently changed.Else, the Code will emit to you in the shell, that nothing has changed.


Python-Projekt: Bundesliga-Torschützen

E-Mail-Client:
Python greift auf das angegebene Gmail Konto zu, in dem er sich mit meinen Daten, die ich oben definiert habe, einloggt.
Durch das Integrieren von MIMEmultipart ist es möglich, die E-Mail in mehrere Parts aufzuteilen.
So habe ich über der Liste mittels einer HTML-Formatierung einen Text & Betreff verfasst, der über der Tabelle der Toptorjäger steht.

Webscraper:
Auf der Website https://www.kicker.de/bundesliga/torjaeger/2020-21/ habe ich mittels eines Webscrapers die Torjägerliste herausgeschnitten und in meine E-Mail eingefügt.
Mithilfe von BeautifulSoup parse ich mir den Teil der Webseite, die in einer E-Mail verschickt wird. Dieser wird ausgelesen und in Tabellenform in der E-Mail eingefügt.

Trigger:
Zuerst wird geprüft, ob ein Dokument mit dem Namen des Torjägerlistenersten vorhanden ist. Trifft dies nicht zu, wird eines erstellt, dass den Namen des Toptorjägers zeigt.
Ist ein Dokument vorhanden, wird der Name mit dem aktuellen Namen, der auf kicker.de als Erstplatzierter angezeigt, verglichen.
Ist dieser gleich, wird keine E-Mail verschickt und das Programm gibt eine kurze Meldung zurück.
Ist der Name unterschiedlich, wird das E-Mail-Client-Programm gestartet und die E-Mail mit der aktuellen Liste verschickt. 

