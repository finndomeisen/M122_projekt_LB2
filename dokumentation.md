# Dokumentation: Automatisierter TikTok Uploader


Wir haben ein Skript mit Python programmiert, das automatisch ein Video auf TikTok hochladen soll. Das Ziel war, dass das Video aus einem Ordner genommen wird, dann eine Beschreibung und ein Sound hinzugefügt werden und alles zu einer bestimmten Uhrzeit automatisch hochgeladen wird. Wir wollten, dass das auch ohne manuelles Eingreifen funktioniert. Wichtig war uns, dass es sicher ist und alle Schritte protokolliert werden.

Wir haben uns für Python entschieden, weil es einfach zu verstehen ist und viele Funktionen schon mitbringt. Man kann damit Dateien verarbeiten, Log-Dateien schreiben und Sachen zeitlich steuern. Außerdem ist es einfacher, wenn man mit KI zusammenarbeitet oder später etwas am Code ändern will.

Unser Projekt ist in mehrere Dateien aufgeteilt. Das Hauptskript heisst `main.py`, das startet alles. Dann gibt es `uploader.py`, das bereitet das Video, die Beschreibung und den Sound für den Upload vor. Mit `hash_check.py` wird geprüft, ob jemand die Konfigurationsdatei verändert hat. In `logger.py` wird festgelegt, was ins Log geschrieben wird. Die Einstellungen sind in `config.cfg`. Dort steht zum Beispiel, wann das Video hochgeladen werden soll und wie die Beschreibung aussieht.

Beispiel für die Konfig:

```
[UPLOAD]
video_path = videos/video1.mp4
description = Das ist ein automatischer Upload am {date}.
hashtags = #fun #dailyupload #auto
sound = sounds/my_cool_sound.mp3
upload_time = 15:00
token = SECRET_TOKEN_123
```

Das `{date}` wird automatisch durch das aktuelle Datum ersetzt, wenn das Skript läuft.

Wenn das Skript gestartet wird, prüft es zuerst die Uhrzeit. Nur wenn die mit der in der Konfig-Datei übereinstimmt, geht es weiter. Danach schaut es, ob die Konfig-Datei echt ist (also nicht verändert wurde). Wenn alles passt, wird das Video vorbereitet und hochgeladen (aktuell nur simuliert). Am Ende wird alles, was passiert ist, in eine Log-Datei geschrieben.

Wir haben mehrere Tests gemacht. Zum Beispiel haben wir geschaut, ob das Skript die Uhrzeit beachtet, ob es Fehler erkennt, wenn der Pfad zum Video falsch ist, oder ob die Manipulation der Konfig-Datei erkannt wird. Die meisten Sachen haben funktioniert. Nur bei einer zu langen Beschreibung fehlt noch eine Warnung.

Was wir gelernt haben: Python ist gut für so etwas, man sollte immer auf Sicherheit achten und Logs helfen, Fehler zu finden. Konfigurationsdateien machen alles viel flexibler.

In Zukunft würden wir gerne eine echte Upload-Funktion einbauen, zum Beispiel mit `selenium` oder einer API von TikTok. Bisher ist nur alles vorbereitet. Wir sind aber zufrieden, wie weit wir gekommen sind.
