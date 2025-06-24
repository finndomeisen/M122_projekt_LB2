Natürlich! Hier ist eine einfache, gut verständliche **Dokumentation**, die ihr direkt abgeben oder als `README.md` in euer GitHub-Projekt legen könnt. Sie erklärt das Projekt, den Aufbau und wie man es benutzt.

---

## 📄 Dokumentation: Automatisierter TikTok Uploader

**Projekt:** Automatisierter TikTok Video Upload
**Team:** Finn, Fabio
**Modul:** M122 – Applikationen mit Skriptsprachen realisieren

---

### 🧠 Projektidee

Unser Ziel war es, ein Python-Skript zu erstellen, das automatisch jeden Tag ein TikTok-Video hochlädt. Dabei soll das Video aus einem lokalen Ordner genommen werden, mit Beschreibung, Hashtags und Sound versehen werden und zur gewünschten Uhrzeit online gehen – ganz ohne manuelles Eingreifen.

---

### 📁 Projektstruktur

```
tiktok_uploader/
│
├── main.py              # Startet das ganze Skript
├── uploader.py          # Lädt und verarbeitet Konfigurationsdaten
├── hash_check.py        # Prüft die Integrität der Konfigurationsdatei
├── logger.py            # Erstellt und verwaltet Log-Dateien
├── config.cfg           # Konfigurationsdatei für Beschreibung, Uhrzeit usw.
├── log.txt              # Log-Datei mit allen Uploads und Fehlern
├── code_to_get_hash.py  # Generiert den Sicherheits-Hash der config.cfg
│
├── videos/              # Ordner mit dem TikTok-Video
│   └── video1.mp4
├── sounds/              # Ordner mit dem Soundfile
│   └── my_cool_sound.mp3
```

---

### ⚙️ Funktionsweise

1. Beim Start prüft `main.py`, ob die aktuelle Uhrzeit mit der in der `config.cfg` hinterlegten Upload-Zeit übereinstimmt.
2. Vor dem Upload wird die Konfigurationsdatei auf Manipulation geprüft (per SHA-256-Hash).
3. Das Video, die Beschreibung und der Sound werden vorbereitet.
4. Die Upload-Funktion wird aufgerufen (derzeit noch simuliert).
5. Alle Vorgänge werden mit Zeitstempel in `log.txt` dokumentiert.

---

### 🔐 Sicherheit

* Vor jedem Upload prüft das Skript, ob die `config.cfg` manipuliert wurde.
* Dazu wird mit `code_to_get_hash.py` ein Hashwert erzeugt, der in `main.py` eingetragen wird.
* Bei Abweichungen wird der Upload abgebrochen und ein Fehler ins Log geschrieben.

---

### 🧪 Tests

Wir haben mehrere Tests durchgeführt:

* **Uhrzeitsteuerung** funktioniert: Der Upload passiert nur zur eingestellten Zeit.
* **Datumsplatzhalter** in der Beschreibung wird korrekt ersetzt.
* **Logs** werden korrekt erstellt.
* **Manipulationsschutz** erkennt Änderungen in der Config.

---

### 🔄 Nächste Schritte

Aktuell ist der Upload nur eine Simulation. Später wollen wir entweder `selenium` oder eine TikTok-API verwenden, um den Upload wirklich auszuführen. Die Projektstruktur ist dafür schon vorbereitet.

---

Wenn du willst, kann ich daraus auch ein abgabefertiges Markdown-File zum Download machen (`/03`) oder das Ganze als PDF verpacken. Sag einfach Bescheid!



