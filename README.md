Teilnehmer/innen des Teams:
===========================

| **Klasse**: | **Team**: |
| --- | --- |
| *PE24a* | *Finn, Fabio* |

Anforderungsdefinition mit KI-Einsatz (Meilenstein A)
=====================================================

| *Projektname* | **Fachlicher Inhalt:** (Allgemeine Beschreibung) |
| :-- | :-- |
| *Automatisierter TikTok Uploader* | *Der Script soll täglich automatisch ein vordefiniertes TikTok-Video mit Beschreibung und Sound hochladen.* |
| **Kundennutzen**: | *Mit dem Skript sollen täglich automatisch Videos auf TikTok hochgeladen werden, ohne dass der Kunde selbst aktiv werden muss. Das spart Zeit und stellt eine konstante Online-Präsenz sicher.* |
| **Setup und Automation:** | *Der Kundendienst ist ein automatisierter Video-Uploader, der lokal gespeicherte Videos verarbeitet und über ein Skript auf TikTok hochlädt. Dabei wird pro Tag ein Video veröffentlicht, inklusive Beschreibung und Sound.* |
| **Detailierte Beschreibung der einzelnen Aspekte:** | - *Konfiguration (.cfg): In der Konfigurationsdatei werden Sound, Videopfad, Beschreibung und Upload-Zeitpunkt definiert.* - *Get-Prozedur (.raw): Das Skript lädt automatisch die in der Konfiguration hinterlegte Videodatei und prüft, ob sie bereit für den Upload ist.* - *Verarbeitung (process): Beschreibung und Sound werden formatiert und dem Video zugeordnet, inklusive dynamischer Anpassungen wie z. B. Datum im Beschreibungstext.* - *Weiterreichung (.fmt): Das fertige Paket wird lokal vorbereitet und auf den Kundenserver geladen, von dort erfolgt der Transfer zu TikTok.* - *Sicherheitsaspekte: Das Skript enthält Authentifizierung für den Upload, validiert Dateiformate und protokolliert alle Upload-Aktivitäten zur Nachvollziehbarkeit.* |
| **(Skizze / Mockup)**: | [Einfügen eines Bildes, das Text, Screenshot, Diagramm, Design enthält. Automatisch generierte Beschreibung](https://gitlab.com/ch-tbz-it/Stud/m122/-/tree/main/10_Projekte_LB2/x_gitressourcen/Systemdesign.png) → [**Copy**](https://gitlab.com/ch-tbz-it/Stud/m122/-/blob/main/10_Projekte_LB2/m122-Projekte.rtb) **board and edit.** *Wir werden mit der Vorlage vom Miro arbeiten.* |
| **Erkenntnisse aus der Machbarkeitsabklärung in Bash (oder Python):** | *Noch keine Tests durchgeführt. Die ersten Funktionen werden in den nächsten Tagen mit Python evaluiert.* |

| Kriterien | Angaben |
| :-- | :-- |
| **MUSS Kriterien:** (Konkrete Features, die umzusetzen sind) | - *Folgende Features sollen implementiert werden, um einen produktiven Ablauf sicherzustellen:* - *Ein abgelegtes Video wird automatisch täglich auf TikTok hochgeladen.* - *Die Beschreibung und der Sound werden entsprechend der Konfiguration gesetzt.* - *Folgende Tests sollen durchgeführt werden:* Kontrolle der Upload-Zeit, Sichtbarkeit des Videos (öffentlich) |
| **KANN Kriterien:** (Konkrete Features, die optional sind) | *Folgende Features können zusätzlich implementiert werden: (Varianten, Kreativität)* - *Automatische Anpassung der Beschreibung mit aktuellem Datum* - *Automatischer Videoabruf über eine täglich wechselnde API* |

* * * * *

**Hinweise:**

-   Ein **UML Aktivitätsdiagramm** ist zu erstellen; entweder von der Aufgabenstellung (Benutzersicht) oder von einem komplexen Programmteil (als Systemdokumentation).

-   Durch **KI** erstellte Scripts müssen in der Dokumentation als solche **ausgewiesen** werden (Modell, Prompt), mit **Tests** auf ihre Funktionstüchtigkeit überprüft und in der Doku **erklärt** werden.

* * * * *

**KI-Einsatz:**

-   *Wir werden alle Programmteile, die wir nicht selbst umsetzen können, mithilfe von KI erstellen.*

-   *Verwendetes Modell: ChatGPT-4o.*

-   *Prompts werden im Verlauf dokumentiert.*

-   *Die Funktionalität wird laufend mit Testläufen, Protokollen und Logs geprüft.*
