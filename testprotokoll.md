# Testprotokoll: Automatisierter TikTok Uploader

---

## Testübersicht

| Testfall | Thema                           | Ressourcen                       | Resultat                                              |
| -------- | ------------------------------- | -------------------------------- | ----------------------------------------------------- |
| A1       | Uhrzeitgesteuerter Upload       | `main.py`, `config.cfg`          | ✅ Upload erfolgt nur zur definierten Uhrzeit          |
| A2       | Beschreibung mit Datum          | `uploader.py`, `config.cfg`      | ✅ {date} wird durch aktuelles Datum ersetzt           |
| A3       | Logfile-Erstellung              | `logger.py`, `log.txt`           | ✅ Log wird mit Zeit, Status und Fehlern erstellt      |
| A4       | Manipulationsschutz aktiv       | `hash_check.py`, `main.py`       | ✅ Abbruch bei falschem Hash, Fehler wird geloggt      |
| A5       | Fehlende Videodatei erkennen    | Video bewusst gelöscht           | ✅ Fehler erkannt und protokolliert                    |
| A6       | Sound-Zuordnung korrekt         | `config.cfg`, `sounds/`          | ✅ Soundpfad wird korrekt geladen                      |
| A7       | Ungültiger Dateipfad            | Falscher Pfad in `config.cfg`    | ✅ Fehler erkannt, Logeintrag erstellt                 |
| A8       | Upload bei Zeitabweichung       | Uhrzeit falsch gesetzt           | ✅ Kein Upload außerhalb der Zeit                      |
| A9       | Wiederholter Start des Skripts  | `main.py` mehrfach ausgeführt    | ✅ Kein mehrfacher Upload, Skript verhält sich korrekt |
| A10      | Leere Beschreibung              | `description = ` in `config.cfg` | ⚠️ Beschreibung leer, Hinweis fehlt im Log            |
| A11      | Beschreibung länger als erlaubt | Beschreibung > 300 Zeichen       | ⚠️ Wird nicht abgeschnitten, Info fehlt im Log        |
| A12      | Sound-Datei fehlt               | Sound bewusst gelöscht           | ✅ Fehler erkannt und gemeldet                         |
| A13      | Logging bei Upload-Abbruch      | Hash falsch + falsche Uhrzeit    | ✅ Zwei Fehler korrekt geloggt                         |

---

## Hinweise:

* Test A11 zeigt, dass eine Längenprüfung für die TikTok-Beschreibung noch fehlt.
* Test A10 sollte zukünftig einen Hinweis im Log erzeugen.
* Die wichtigsten Tests zur Dateiüberprüfung, Uhrzeitsteuerung und Sicherheit wurden erfolgreich durchgeführt.

---

**Fazit:** Die Grundlogik, Dateiverarbeitung, Zeitsteuerung, Sicherheit und Logging funktionieren wie geplant. Der Code ist bereit für die Erweiterung mit einer echten Upload-Funktion.
