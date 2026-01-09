"""
gbHam Translations
Multi-language support for German, English, Italian, Slovenian.
"""

from typing import Dict

SUPPORTED_LANGUAGES = ["de", "en", "it", "sl"]
DEFAULT_LANGUAGE = "de"

TRANSLATIONS: Dict[str, Dict[str, str]] = {
    # ===================
    # Navigation & Header
    # ===================
    "nav_guestbook": {
        "de": "Gästebuch",
        "en": "Guestbook",
        "it": "Libro degli ospiti",
        "sl": "Knjiga gostov",
    },
    "nav_privacy": {
        "de": "Datenschutz",
        "en": "Privacy",
        "it": "Privacy",
        "sl": "Zasebnost",
    },
    "nav_imprint": {
        "de": "Impressum",
        "en": "Imprint",
        "it": "Impronta",
        "sl": "Impressum",
    },
    "subtitle_guestbook": {
        "de": "Gästebuch",
        "en": "Guestbook",
        "it": "Libro degli ospiti",
        "sl": "Knjiga gostov",
    },

    # ===================
    # Entry Form
    # ===================
    "new_entry": {
        "de": "Neuer Eintrag",
        "en": "New Entry",
        "it": "Nuova voce",
        "sl": "Nov vnos",
    },
    "callsign": {
        "de": "Rufzeichen",
        "en": "Callsign",
        "it": "Nominativo",
        "sl": "Klicni znak",
    },
    "callsign_hint": {
        "de": "Europäisches Amateurfunk-Rufzeichen",
        "en": "European amateur radio callsign",
        "it": "Nominativo radioamatoriale europeo",
        "sl": "Evropski amaterski radijski klicni znak",
    },
    "message": {
        "de": "Nachricht",
        "en": "Message",
        "it": "Messaggio",
        "sl": "Sporočilo",
    },
    "message_hint": {
        "de": "Maximal {0} Zeichen",
        "en": "Maximum {0} characters",
        "it": "Massimo {0} caratteri",
        "sl": "Največ {0} znakov",
    },
    "message_placeholder": {
        "de": "Ihre Grußbotschaft...",
        "en": "Your greeting message...",
        "it": "Il tuo messaggio di saluto...",
        "sl": "Vaše pozdravno sporočilo...",
    },
    "submit": {
        "de": "Eintrag absenden",
        "en": "Submit Entry",
        "it": "Invia voce",
        "sl": "Pošlji vnos",
    },
    "privacy_hint": {
        "de": "Mit dem Absenden bestätigen Sie, dass Sie die {0} gelesen haben.",
        "en": "By submitting, you confirm that you have read the {0}.",
        "it": "Inviando, confermi di aver letto la {0}.",
        "sl": "Z oddajo potrjujete, da ste prebrali {0}.",
    },
    "privacy_policy": {
        "de": "Datenschutzerklärung",
        "en": "Privacy Policy",
        "it": "Informativa sulla privacy",
        "sl": "Pravilnik o zasebnosti",
    },

    # ===================
    # Messages
    # ===================
    "success_entry": {
        "de": "Vielen Dank für Ihren Eintrag!",
        "en": "Thank you for your entry!",
        "it": "Grazie per la tua voce!",
        "sl": "Hvala za vaš vnos!",
    },
    "error_readonly": {
        "de": "Das Gästebuch befindet sich im Nur-Lesen-Modus.",
        "en": "The guestbook is in read-only mode.",
        "it": "Il libro degli ospiti è in modalità di sola lettura.",
        "sl": "Knjiga gostov je v načinu samo za branje.",
    },
    "error_cooldown": {
        "de": "Bitte warten Sie noch {0} Sekunden zwischen Einträgen.",
        "en": "Please wait {0} more seconds between entries.",
        "it": "Attendere altri {0} secondi tra le voci.",
        "sl": "Počakajte še {0} sekund med vnosi.",
    },
    "error_validation": {
        "de": "Ungültige Eingabe. Bitte überprüfen Sie Rufzeichen und Nachricht.",
        "en": "Invalid input. Please check callsign and message.",
        "it": "Input non valido. Controlla nominativo e messaggio.",
        "sl": "Neveljaven vnos. Preverite klicni znak in sporočilo.",
    },
    "error_encoding": {
        "de": "Ungültige Zeichenkodierung. Bitte verwenden Sie nur UTF-8-Zeichen.",
        "en": "Invalid character encoding. Please use only UTF-8 characters.",
        "it": "Codifica caratteri non valida. Utilizzare solo caratteri UTF-8.",
        "sl": "Neveljavno kodiranje znakov. Uporabite samo znake UTF-8.",
    },
    "readonly_notice": {
        "de": "Das Gästebuch befindet sich derzeit im Nur-Lesen-Modus.",
        "en": "The guestbook is currently in read-only mode.",
        "it": "Il libro degli ospiti è attualmente in modalità di sola lettura.",
        "sl": "Knjiga gostov je trenutno v načinu samo za branje.",
    },

    # ===================
    # Entries List
    # ===================
    "entries": {
        "de": "Einträge",
        "en": "Entries",
        "it": "Voci",
        "sl": "Vnosi",
    },
    "no_entries": {
        "de": "Noch keine Einträge vorhanden. Seien Sie der Erste!",
        "en": "No entries yet. Be the first!",
        "it": "Nessuna voce ancora. Sii il primo!",
        "sl": "Še ni vnosov. Bodite prvi!",
    },

    # ===================
    # Pagination
    # ===================
    "page_of": {
        "de": "Seite {0} von {1}",
        "en": "Page {0} of {1}",
        "it": "Pagina {0} di {1}",
        "sl": "Stran {0} od {1}",
    },
    "first_page": {
        "de": "Erste Seite",
        "en": "First page",
        "it": "Prima pagina",
        "sl": "Prva stran",
    },
    "prev_page": {
        "de": "Zurück",
        "en": "Previous",
        "it": "Precedente",
        "sl": "Nazaj",
    },
    "next_page": {
        "de": "Weiter",
        "en": "Next",
        "it": "Successivo",
        "sl": "Naprej",
    },
    "last_page": {
        "de": "Letzte Seite",
        "en": "Last page",
        "it": "Ultima pagina",
        "sl": "Zadnja stran",
    },

    # ===================
    # Footer
    # ===================
    "powered_by": {
        "de": "Powered by",
        "en": "Powered by",
        "it": "Powered by",
        "sl": "Powered by",
    },
    "operator": {
        "de": "Betreiber",
        "en": "Operator",
        "it": "Operatore",
        "sl": "Operater",
    },

    # ===================
    # Privacy Page
    # ===================
    "privacy_title": {
        "de": "Datenschutzerklärung",
        "en": "Privacy Policy",
        "it": "Informativa sulla privacy",
        "sl": "Pravilnik o zasebnosti",
    },
    "privacy_responsible": {
        "de": "Verantwortlicher",
        "en": "Data Controller",
        "it": "Titolare del trattamento",
        "sl": "Upravljavec podatkov",
    },
    "privacy_responsible_text": {
        "de": "Verantwortlich für die Datenverarbeitung auf dieser Website ist:",
        "en": "Responsible for data processing on this website:",
        "it": "Responsabile del trattamento dei dati su questo sito:",
        "sl": "Odgovoren za obdelavo podatkov na tej spletni strani:",
    },
    "privacy_purpose": {
        "de": "Zweck der Datenverarbeitung",
        "en": "Purpose of Data Processing",
        "it": "Finalità del trattamento dei dati",
        "sl": "Namen obdelave podatkov",
    },
    "privacy_purpose_text": {
        "de": "Diese Website dient als freiwilliges Gästebuch für die Amateurfunk-Runde",
        "en": "This website serves as a voluntary guestbook for the amateur radio net",
        "it": "Questo sito serve come libro degli ospiti volontario per la rete radioamatoriale",
        "sl": "Ta spletna stran služi kot prostovoljna knjiga gostov za amatersko radijsko mrežo",
    },
    "privacy_purpose_note": {
        "de": "Dies ist kein Logbuch, kein soziales Netzwerk und kein Tracking-Tool. Es handelt sich um ein datensparsames, freiwilliges Gästebuch.",
        "en": "This is not a logbook, not a social network, and not a tracking tool. It is a data-minimal, voluntary guestbook.",
        "it": "Questo non è un logbook, non è un social network e non è uno strumento di tracciamento. È un libro degli ospiti volontario e minimale.",
        "sl": "To ni dnevnik, ni družbeno omrežje in ni orodje za sledenje. To je prostovoljna knjiga gostov z minimalnimi podatki.",
    },
    "privacy_legal_basis": {
        "de": "Rechtsgrundlage",
        "en": "Legal Basis",
        "it": "Base giuridica",
        "sl": "Pravna podlaga",
    },
    "privacy_legal_basis_text": {
        "de": "Die Verarbeitung Ihrer Daten erfolgt auf Grundlage Ihrer freiwilligen Einwilligung gemäß Art. 6 Abs. 1 lit. a DSGVO.",
        "en": "Your data is processed based on your voluntary consent according to Art. 6(1)(a) GDPR.",
        "it": "I tuoi dati vengono trattati sulla base del tuo consenso volontario ai sensi dell'Art. 6(1)(a) GDPR.",
        "sl": "Vaši podatki se obdelujejo na podlagi vašega prostovoljnega soglasja v skladu s čl. 6(1)(a) GDPR.",
    },
    "privacy_collected_data": {
        "de": "Erhobene Daten",
        "en": "Collected Data",
        "it": "Dati raccolti",
        "sl": "Zbrani podatki",
    },
    "privacy_collected_data_text": {
        "de": "Bei Nutzung des Gästebuchs werden folgende Daten gespeichert:",
        "en": "When using the guestbook, the following data is stored:",
        "it": "Quando utilizzi il libro degli ospiti, vengono memorizzati i seguenti dati:",
        "sl": "Pri uporabi knjige gostov se shranijo naslednji podatki:",
    },
    "privacy_data_callsign": {
        "de": "Ihr eingegebenes Amateurfunk-Rufzeichen",
        "en": "Your entered amateur radio callsign",
        "it": "Il tuo nominativo radioamatoriale inserito",
        "sl": "Vaš vneseni amaterski radijski klicni znak",
    },
    "privacy_data_message": {
        "de": "Ihre eingegebene Grußbotschaft (max. 300 Zeichen)",
        "en": "Your entered greeting message (max. 300 characters)",
        "it": "Il tuo messaggio di saluto inserito (max. 300 caratteri)",
        "sl": "Vaše vneseno pozdravno sporočilo (največ 300 znakov)",
    },
    "privacy_data_timestamp": {
        "de": "Datum und Uhrzeit des Eintrags",
        "en": "Date and time of the entry",
        "it": "Data e ora della voce",
        "sl": "Datum in čas vnosa",
    },
    "privacy_not_collected": {
        "de": "Nicht erhobene Daten",
        "en": "Data Not Collected",
        "it": "Dati non raccolti",
        "sl": "Podatki, ki se ne zbirajo",
    },
    "privacy_not_collected_text": {
        "de": "Folgende Daten werden ausdrücklich nicht gespeichert:",
        "en": "The following data is explicitly not stored:",
        "it": "I seguenti dati non vengono esplicitamente memorizzati:",
        "sl": "Naslednji podatki se izrecno ne shranjujejo:",
    },
    "privacy_no_ip": {
        "de": "IP-Adressen (werden nur temporär für Spam-Schutz verwendet und nicht protokolliert)",
        "en": "IP addresses (only used temporarily for spam protection, not logged)",
        "it": "Indirizzi IP (utilizzati solo temporaneamente per la protezione antispam, non registrati)",
        "sl": "IP naslovi (uporabljajo se samo začasno za zaščito pred vsiljeno pošto, ne beležijo se)",
    },
    "privacy_no_cookies": {
        "de": "Cookies (außer technisch notwendige Session-Cookies)",
        "en": "Cookies (except technically necessary session cookies)",
        "it": "Cookie (tranne i cookie di sessione tecnicamente necessari)",
        "sl": "Piškotki (razen tehnično potrebnih sejnih piškotkov)",
    },
    "privacy_no_tracking": {
        "de": "Tracking- oder Analysedaten",
        "en": "Tracking or analytics data",
        "it": "Dati di tracciamento o analisi",
        "sl": "Podatki o sledenju ali analitiki",
    },
    "privacy_no_location": {
        "de": "Standortdaten",
        "en": "Location data",
        "it": "Dati di posizione",
        "sl": "Podatki o lokaciji",
    },
    "privacy_no_device": {
        "de": "Geräteinformationen",
        "en": "Device information",
        "it": "Informazioni sul dispositivo",
        "sl": "Informacije o napravi",
    },
    "privacy_retention": {
        "de": "Speicherdauer",
        "en": "Data Retention",
        "it": "Conservazione dei dati",
        "sl": "Hramba podatkov",
    },
    "privacy_retention_text": {
        "de": "Ihre Einträge werden auf unbestimmte Zeit gespeichert, solange das Gästebuch betrieben wird. Sie können jederzeit die Löschung Ihrer Einträge beantragen.",
        "en": "Your entries are stored indefinitely as long as the guestbook is operated. You can request deletion of your entries at any time.",
        "it": "Le tue voci vengono conservate a tempo indeterminato finché il libro degli ospiti è in funzione. Puoi richiedere la cancellazione delle tue voci in qualsiasi momento.",
        "sl": "Vaši vnosi se hranijo nedoločen čas, dokler knjiga gostov deluje. Kadarkoli lahko zahtevate izbris svojih vnosov.",
    },
    "privacy_rights": {
        "de": "Ihre Rechte",
        "en": "Your Rights",
        "it": "I tuoi diritti",
        "sl": "Vaše pravice",
    },
    "privacy_rights_text": {
        "de": "Sie haben folgende Rechte bezüglich Ihrer personenbezogenen Daten:",
        "en": "You have the following rights regarding your personal data:",
        "it": "Hai i seguenti diritti riguardo ai tuoi dati personali:",
        "sl": "Imate naslednje pravice glede vaših osebnih podatkov:",
    },
    "privacy_right_access": {
        "de": "Auskunftsrecht (Art. 15 DSGVO): Sie können Auskunft über Ihre gespeicherten Daten verlangen.",
        "en": "Right of access (Art. 15 GDPR): You can request information about your stored data.",
        "it": "Diritto di accesso (Art. 15 GDPR): Puoi richiedere informazioni sui tuoi dati memorizzati.",
        "sl": "Pravica do dostopa (čl. 15 GDPR): Lahko zahtevate informacije o svojih shranjenih podatkih.",
    },
    "privacy_right_deletion": {
        "de": "Recht auf Löschung (Art. 17 DSGVO): Sie können die Löschung Ihrer Einträge verlangen.",
        "en": "Right to erasure (Art. 17 GDPR): You can request deletion of your entries.",
        "it": "Diritto alla cancellazione (Art. 17 GDPR): Puoi richiedere la cancellazione delle tue voci.",
        "sl": "Pravica do izbrisa (čl. 17 GDPR): Lahko zahtevate izbris svojih vnosov.",
    },
    "privacy_right_withdraw": {
        "de": "Widerrufsrecht (Art. 7 Abs. 3 DSGVO): Sie können Ihre Einwilligung jederzeit widerrufen.",
        "en": "Right to withdraw consent (Art. 7(3) GDPR): You can withdraw your consent at any time.",
        "it": "Diritto di revoca del consenso (Art. 7(3) GDPR): Puoi revocare il tuo consenso in qualsiasi momento.",
        "sl": "Pravica do preklica soglasja (čl. 7(3) GDPR): Svoje soglasje lahko kadarkoli prekličete.",
    },
    "privacy_right_complaint": {
        "de": "Beschwerderecht: Sie haben das Recht, sich bei einer Aufsichtsbehörde zu beschweren.",
        "en": "Right to complain: You have the right to lodge a complaint with a supervisory authority.",
        "it": "Diritto di reclamo: Hai il diritto di presentare un reclamo a un'autorità di controllo.",
        "sl": "Pravica do pritožbe: Imate pravico vložiti pritožbo pri nadzornem organu.",
    },
    "privacy_contact": {
        "de": "Kontakt für Datenschutzanfragen",
        "en": "Contact for Privacy Inquiries",
        "it": "Contatto per richieste sulla privacy",
        "sl": "Kontakt za poizvedbe o zasebnosti",
    },
    "privacy_contact_text": {
        "de": "Für alle Anfragen bezüglich Ihrer Daten (Auskunft, Löschung, Widerruf) wenden Sie sich bitte an:",
        "en": "For all inquiries regarding your data (access, deletion, withdrawal), please contact:",
        "it": "Per tutte le richieste riguardanti i tuoi dati (accesso, cancellazione, revoca), contatta:",
        "sl": "Za vse poizvedbe glede vaših podatkov (dostop, izbris, preklic) se obrnite na:",
    },
    "privacy_contact_hint": {
        "de": "Bitte geben Sie in Ihrer Anfrage Ihr Rufzeichen an, damit wir Ihre Einträge identifizieren können.",
        "en": "Please include your callsign in your inquiry so we can identify your entries.",
        "it": "Includi il tuo nominativo nella richiesta in modo che possiamo identificare le tue voci.",
        "sl": "V poizvedbi navedite svoj klicni znak, da lahko identificiramo vaše vnose.",
    },
    "privacy_security": {
        "de": "Technische Sicherheitsmaßnahmen",
        "en": "Technical Security Measures",
        "it": "Misure di sicurezza tecniche",
        "sl": "Tehnični varnostni ukrepi",
    },
    "privacy_security_text": {
        "de": "Wir setzen technische Maßnahmen zum Schutz Ihrer Daten und zur Missbrauchsprävention ein:",
        "en": "We implement technical measures to protect your data and prevent abuse:",
        "it": "Implementiamo misure tecniche per proteggere i tuoi dati e prevenire abusi:",
        "sl": "Izvajamo tehnične ukrepe za zaščito vaših podatkov in preprečevanje zlorab:",
    },
    "privacy_security_validation": {
        "de": "Eingabevalidierung und -bereinigung",
        "en": "Input validation and sanitization",
        "it": "Validazione e sanificazione dell'input",
        "sl": "Preverjanje in čiščenje vnosa",
    },
    "privacy_security_ratelimit": {
        "de": "Schutz vor automatisierten Anfragen (Rate Limiting)",
        "en": "Protection against automated requests (rate limiting)",
        "it": "Protezione contro richieste automatizzate (rate limiting)",
        "sl": "Zaščita pred avtomatiziranimi zahtevami (omejevanje hitrosti)",
    },
    "privacy_security_https": {
        "de": "Verschlüsselte Übertragung (HTTPS, sofern konfiguriert)",
        "en": "Encrypted transmission (HTTPS, if configured)",
        "it": "Trasmissione crittografata (HTTPS, se configurato)",
        "sl": "Šifriran prenos (HTTPS, če je konfiguriran)",
    },
    "privacy_security_nothirdparty": {
        "de": "Keine Weitergabe von Daten an Dritte",
        "en": "No sharing of data with third parties",
        "it": "Nessuna condivisione di dati con terze parti",
        "sl": "Brez deljenja podatkov s tretjimi osebami",
    },
    "privacy_voluntary": {
        "de": "Freiwilligkeit",
        "en": "Voluntary Participation",
        "it": "Partecipazione volontaria",
        "sl": "Prostovoljna udeležba",
    },
    "privacy_voluntary_text": {
        "de": "Die Nutzung dieses Gästebuchs ist vollständig freiwillig. Sie können die Funkrunde nutzen, ohne einen Gästebucheintrag zu hinterlassen. Ihre Teilnahme an der Funkrunde ist nicht an die Nutzung dieses Gästebuchs gekoppelt.",
        "en": "Using this guestbook is completely voluntary. You can participate in the radio net without leaving a guestbook entry. Your participation in the net is not tied to using this guestbook.",
        "it": "L'utilizzo di questo libro degli ospiti è completamente volontario. Puoi partecipare alla rete radio senza lasciare una voce nel libro degli ospiti. La tua partecipazione alla rete non è legata all'utilizzo di questo libro degli ospiti.",
        "sl": "Uporaba te knjige gostov je popolnoma prostovoljna. V radijski mreži lahko sodelujete brez vnosa v knjigo gostov. Vaša udeležba v mreži ni vezana na uporabo te knjige gostov.",
    },
    "privacy_cloudflare": {
        "de": "Cloudflare (CDN & Sicherheit)",
        "en": "Cloudflare (CDN & Security)",
        "it": "Cloudflare (CDN e sicurezza)",
        "sl": "Cloudflare (CDN in varnost)",
    },
    "privacy_cloudflare_text": {
        "de": "Diese Website nutzt Dienste von Cloudflare, Inc., einem US-amerikanischen Unternehmen, das Content Delivery Network (CDN), DDoS-Schutz und Sicherheitsdienste anbietet.",
        "en": "This website uses services from Cloudflare, Inc., a US company providing Content Delivery Network (CDN), DDoS protection, and security services.",
        "it": "Questo sito utilizza i servizi di Cloudflare, Inc., un'azienda statunitense che fornisce Content Delivery Network (CDN), protezione DDoS e servizi di sicurezza.",
        "sl": "Ta spletna stran uporablja storitve Cloudflare, Inc., ameriškega podjetja, ki ponuja omrežje za dostavo vsebin (CDN), zaščito DDoS in varnostne storitve.",
    },
    "privacy_cloudflare_data": {
        "de": "Verarbeitete Daten",
        "en": "Processed Data",
        "it": "Dati trattati",
        "sl": "Obdelani podatki",
    },
    "privacy_cloudflare_ip": {
        "de": "IP-Adressen: Für Routing und Sicherheitsfunktionen",
        "en": "IP addresses: For routing and security functions",
        "it": "Indirizzi IP: Per routing e funzioni di sicurezza",
        "sl": "IP naslovi: Za usmerjanje in varnostne funkcije",
    },
    "privacy_cloudflare_http": {
        "de": "HTTP-Anfragedaten: Header, URLs und Metadaten",
        "en": "HTTP request data: Headers, URLs, and metadata",
        "it": "Dati delle richieste HTTP: Header, URL e metadati",
        "sl": "Podatki HTTP zahtev: Glave, URL-ji in metapodatki",
    },
    "privacy_cloudflare_security": {
        "de": "Sicherheitsinformationen: Zur Erkennung und Abwehr von Angriffen",
        "en": "Security information: For detecting and preventing attacks",
        "it": "Informazioni di sicurezza: Per rilevare e prevenire attacchi",
        "sl": "Varnostne informacije: Za odkrivanje in preprečevanje napadov",
    },
    "privacy_cloudflare_functions": {
        "de": "Funktionen",
        "en": "Functions",
        "it": "Funzioni",
        "sl": "Funkcije",
    },
    "privacy_cloudflare_cdn": {
        "de": "CDN: Zwischenspeichern und Auslieferung statischer Inhalte von nahegelegenen Servern",
        "en": "CDN: Caching and delivering static content from nearby servers",
        "it": "CDN: Cache e distribuzione di contenuti statici da server vicini",
        "sl": "CDN: Predpomnjenje in dostava statične vsebine iz bližnjih strežnikov",
    },
    "privacy_cloudflare_ddos": {
        "de": "DDoS-Schutz: Schutz vor Distributed-Denial-of-Service-Angriffen",
        "en": "DDoS protection: Protection against Distributed Denial-of-Service attacks",
        "it": "Protezione DDoS: Protezione contro attacchi Distributed Denial-of-Service",
        "sl": "Zaščita DDoS: Zaščita pred napadi porazdeljene zavrnitve storitve",
    },
    "privacy_cloudflare_ssl": {
        "de": "SSL/TLS: Verschlüsselung der Datenübertragung",
        "en": "SSL/TLS: Encryption of data transmission",
        "it": "SSL/TLS: Crittografia della trasmissione dati",
        "sl": "SSL/TLS: Šifriranje prenosa podatkov",
    },
    "privacy_cloudflare_block": {
        "de": "Sicherheit: Blockade bösartigen Datenverkehrs und Bot-Angriffe",
        "en": "Security: Blocking malicious traffic and bot attacks",
        "it": "Sicurezza: Blocco del traffico malevolo e attacchi bot",
        "sl": "Varnost: Blokiranje zlonamernega prometa in napadov botov",
    },
    "privacy_cloudflare_legal": {
        "de": "Rechtsgrundlage & Datenschutz",
        "en": "Legal Basis & Privacy",
        "it": "Base giuridica e privacy",
        "sl": "Pravna podlaga in zasebnost",
    },
    "privacy_cloudflare_legal_text": {
        "de": "Die Nutzung von Cloudflare erfolgt auf Grundlage unseres berechtigten Interesses an einer sicheren und effizienten Bereitstellung dieser Website (Art. 6 Abs. 1 lit. f DSGVO).",
        "en": "The use of Cloudflare is based on our legitimate interest in providing this website securely and efficiently (Art. 6(1)(f) GDPR).",
        "it": "L'utilizzo di Cloudflare si basa sul nostro legittimo interesse a fornire questo sito in modo sicuro ed efficiente (Art. 6(1)(f) GDPR).",
        "sl": "Uporaba Cloudflare temelji na našem legitimnem interesu za varno in učinkovito zagotavljanje te spletne strani (čl. 6(1)(f) GDPR).",
    },
    "privacy_cloudflare_dpf": {
        "de": "Cloudflare ist nach dem EU-U.S. Data Privacy Framework zertifiziert, das einen angemessenen Schutz für Datenübermittlungen in die USA gewährleistet.",
        "en": "Cloudflare is certified under the EU-U.S. Data Privacy Framework, ensuring adequate protection for data transfers to the USA.",
        "it": "Cloudflare è certificato secondo l'EU-U.S. Data Privacy Framework, garantendo una protezione adeguata per i trasferimenti di dati negli USA.",
        "sl": "Cloudflare ima certifikat EU-U.S. Data Privacy Framework, ki zagotavlja ustrezno zaščito za prenose podatkov v ZDA.",
    },
    "privacy_cloudflare_more": {
        "de": "Weitere Informationen finden Sie in der Datenschutzrichtlinie von Cloudflare.",
        "en": "For more information, see Cloudflare's privacy policy.",
        "it": "Per maggiori informazioni, consulta l'informativa sulla privacy di Cloudflare.",
        "sl": "Za več informacij glejte pravilnik o zasebnosti Cloudflare.",
    },
    "privacy_changes": {
        "de": "Änderungen dieser Datenschutzerklärung",
        "en": "Changes to this Privacy Policy",
        "it": "Modifiche a questa informativa sulla privacy",
        "sl": "Spremembe tega pravilnika o zasebnosti",
    },
    "privacy_changes_text": {
        "de": "Wir behalten uns vor, diese Datenschutzerklärung bei Bedarf anzupassen. Die aktuelle Version ist stets auf dieser Seite abrufbar.",
        "en": "We reserve the right to update this privacy policy as needed. The current version is always available on this page.",
        "it": "Ci riserviamo il diritto di aggiornare questa informativa sulla privacy secondo necessità. La versione attuale è sempre disponibile su questa pagina.",
        "sl": "Pridržujemo si pravico do posodobitve tega pravilnika o zasebnosti po potrebi. Trenutna različica je vedno na voljo na tej strani.",
    },
    "privacy_date": {
        "de": "Stand: Januar 2026",
        "en": "Last updated: January 2026",
        "it": "Ultimo aggiornamento: Gennaio 2026",
        "sl": "Zadnja posodobitev: Januar 2026",
    },

    # ===================
    # Imprint Page
    # ===================
    "imprint_title": {
        "de": "Impressum",
        "en": "Imprint",
        "it": "Impronta",
        "sl": "Impressum",
    },
    "imprint_legal": {
        "de": "Angaben gemäß E-Commerce-Gesetz (ECG) § 5 und Mediengesetz (MedienG) § 25",
        "en": "Information according to E-Commerce Law (ECG) § 5 and Media Law (MedienG) § 25",
        "it": "Informazioni secondo la legge sull'e-commerce (ECG) § 5 e la legge sui media (MedienG) § 25",
        "sl": "Informacije v skladu z zakonom o e-trgovini (ECG) § 5 in medijskim zakonom (MedienG) § 25",
    },
    "imprint_operator": {
        "de": "Betreiber der Website",
        "en": "Website Operator",
        "it": "Gestore del sito",
        "sl": "Upravljavec spletne strani",
    },
    "imprint_contact": {
        "de": "Kontakt",
        "en": "Contact",
        "it": "Contatto",
        "sl": "Kontakt",
    },
    "imprint_liability_content": {
        "de": "Haftung für Inhalte",
        "en": "Liability for Content",
        "it": "Responsabilità per i contenuti",
        "sl": "Odgovornost za vsebino",
    },
    "imprint_liability_content_text": {
        "de": "Die Inhalte dieser Website wurden mit größtmöglicher Sorgfalt erstellt. Für die Richtigkeit, Vollständigkeit und Aktualität der Inhalte können wir jedoch keine Gewähr übernehmen. Als Diensteanbieter sind wir für eigene Inhalte auf diesen Seiten nach den allgemeinen Gesetzen verantwortlich.",
        "en": "The content of this website has been created with the greatest possible care. However, we cannot guarantee the accuracy, completeness, and timeliness of the content. As a service provider, we are responsible for our own content on these pages in accordance with general laws.",
        "it": "Il contenuto di questo sito è stato creato con la massima cura possibile. Tuttavia, non possiamo garantire l'accuratezza, la completezza e l'attualità del contenuto. Come fornitore di servizi, siamo responsabili dei nostri contenuti su queste pagine in conformità con le leggi generali.",
        "sl": "Vsebina te spletne strani je bila ustvarjena z največjo možno skrbnostjo. Vendar ne moremo jamčiti za točnost, popolnost in aktualnost vsebine. Kot ponudnik storitev smo odgovorni za lastno vsebino na teh straneh v skladu s splošnimi zakoni.",
    },
    "imprint_liability_links": {
        "de": "Haftung für Links",
        "en": "Liability for Links",
        "it": "Responsabilità per i link",
        "sl": "Odgovornost za povezave",
    },
    "imprint_liability_links_text": {
        "de": "Diese Website enthält möglicherweise Links zu externen Websites Dritter, auf deren Inhalte wir keinen Einfluss haben. Deshalb können wir für diese fremden Inhalte auch keine Gewähr übernehmen. Für die Inhalte der verlinkten Seiten ist stets der jeweilige Anbieter oder Betreiber der Seiten verantwortlich.",
        "en": "This website may contain links to external third-party websites over whose content we have no control. Therefore, we cannot assume any liability for these external contents. The respective provider or operator of the linked pages is always responsible for their content.",
        "it": "Questo sito potrebbe contenere link a siti esterni di terze parti sui cui contenuti non abbiamo alcun controllo. Pertanto, non possiamo assumerci alcuna responsabilità per questi contenuti esterni. Il rispettivo fornitore o gestore delle pagine collegate è sempre responsabile dei loro contenuti.",
        "sl": "Ta spletna stran lahko vsebuje povezave do zunanjih spletnih strani tretjih oseb, na katerih vsebino nimamo vpliva. Zato ne moremo prevzeti nobene odgovornosti za te zunanje vsebine. Za vsebino povezanih strani je vedno odgovoren posamezni ponudnik ali upravljavec strani.",
    },
    "imprint_liability_links_note": {
        "de": "Eine permanente inhaltliche Kontrolle der verlinkten Seiten ist jedoch ohne konkrete Anhaltspunkte einer Rechtsverletzung nicht zumutbar. Bei Bekanntwerden von Rechtsverletzungen werden wir derartige Links umgehend entfernen.",
        "en": "However, permanent monitoring of the content of linked pages is not reasonable without concrete evidence of a legal violation. If we become aware of any legal violations, we will remove such links immediately.",
        "it": "Tuttavia, il monitoraggio permanente del contenuto delle pagine collegate non è ragionevole senza prove concrete di una violazione legale. Se veniamo a conoscenza di violazioni legali, rimuoveremo immediatamente tali link.",
        "sl": "Vendar stalno spremljanje vsebine povezanih strani ni razumno brez konkretnih dokazov o pravni kršitvi. Če izvemo za kakršne koli pravne kršitve, bomo takšne povezave takoj odstranili.",
    },
    "imprint_copyright": {
        "de": "Urheberrecht",
        "en": "Copyright",
        "it": "Diritto d'autore",
        "sl": "Avtorske pravice",
    },
    "imprint_copyright_text": {
        "de": "Die durch den Betreiber dieser Website erstellten Inhalte und Werke unterliegen dem österreichischen Urheberrecht. Die Vervielfältigung, Bearbeitung, Verbreitung und jede Art der Verwertung außerhalb der Grenzen des Urheberrechtes bedürfen der schriftlichen Zustimmung des jeweiligen Erstellers.",
        "en": "The content and works created by the operator of this website are subject to Austrian copyright law. Duplication, processing, distribution, and any form of exploitation beyond the limits of copyright require the written consent of the respective creator.",
        "it": "I contenuti e le opere creati dal gestore di questo sito sono soggetti alla legge austriaca sul diritto d'autore. La duplicazione, l'elaborazione, la distribuzione e qualsiasi forma di sfruttamento al di fuori dei limiti del diritto d'autore richiedono il consenso scritto del rispettivo creatore.",
        "sl": "Vsebina in dela, ki jih ustvari upravljavec te spletne strani, so predmet avstrijskega zakona o avtorskih pravicah. Podvajanje, obdelava, distribucija in kakršna koli oblika izkoriščanja izven meja avtorskih pravic zahtevajo pisno soglasje posameznega ustvarjalca.",
    },
    "imprint_copyright_private": {
        "de": "Downloads und Kopien dieser Seite sind nur für den privaten, nicht kommerziellen Gebrauch gestattet.",
        "en": "Downloads and copies of this site are only permitted for private, non-commercial use.",
        "it": "I download e le copie di questo sito sono consentiti solo per uso privato e non commerciale.",
        "sl": "Prenosi in kopije te strani so dovoljeni samo za zasebno, nekomercialno uporabo.",
    },
    "imprint_ugc": {
        "de": "Nutzergenerierte Inhalte",
        "en": "User-Generated Content",
        "it": "Contenuti generati dagli utenti",
        "sl": "Vsebina, ki jo ustvarijo uporabniki",
    },
    "imprint_ugc_text": {
        "de": "Diese Website ermöglicht es Nutzern, Gästebucheinträge zu hinterlassen. Für diese nutzergenerierten Inhalte sind die jeweiligen Verfasser selbst verantwortlich. Wir behalten uns vor, rechtswidrige oder gegen unsere Nutzungsbedingungen verstoßende Inhalte ohne Vorankündigung zu entfernen.",
        "en": "This website allows users to leave guestbook entries. The respective authors are responsible for this user-generated content. We reserve the right to remove content that is illegal or violates our terms of use without prior notice.",
        "it": "Questo sito consente agli utenti di lasciare voci nel libro degli ospiti. I rispettivi autori sono responsabili di questi contenuti generati dagli utenti. Ci riserviamo il diritto di rimuovere contenuti illegali o che violano i nostri termini di utilizzo senza preavviso.",
        "sl": "Ta spletna stran uporabnikom omogoča, da pustijo vnose v knjigi gostov. Za to vsebino, ki jo ustvarijo uporabniki, so odgovorni posamezni avtorji. Pridržujemo si pravico, da brez predhodnega obvestila odstranimo vsebino, ki je nezakonita ali krši naše pogoje uporabe.",
    },
    "imprint_ugc_report": {
        "de": "Sollten Sie auf rechtswidrige Inhalte aufmerksam werden, bitten wir um einen entsprechenden Hinweis per E-Mail.",
        "en": "If you become aware of illegal content, please notify us by email.",
        "it": "Se noti contenuti illegali, ti preghiamo di segnalarcelo via email.",
        "sl": "Če opazite nezakonito vsebino, nas prosimo obvestite po e-pošti.",
    },
    "imprint_odr": {
        "de": "Online-Streitbeilegung",
        "en": "Online Dispute Resolution",
        "it": "Risoluzione delle controversie online",
        "sl": "Spletno reševanje sporov",
    },
    "imprint_odr_text": {
        "de": "Die Europäische Kommission stellt eine Plattform zur Online-Streitbeilegung (OS) bereit:",
        "en": "The European Commission provides a platform for online dispute resolution (ODR):",
        "it": "La Commissione Europea fornisce una piattaforma per la risoluzione delle controversie online (ODR):",
        "sl": "Evropska komisija zagotavlja platformo za spletno reševanje sporov (ODR):",
    },
    "imprint_odr_note": {
        "de": "Wir sind nicht bereit oder verpflichtet, an Streitbeilegungsverfahren vor einer Verbraucherschlichtungsstelle teilzunehmen.",
        "en": "We are not willing or obliged to participate in dispute resolution proceedings before a consumer arbitration board.",
        "it": "Non siamo disposti né obbligati a partecipare a procedimenti di risoluzione delle controversie davanti a un organismo di conciliazione dei consumatori.",
        "sl": "Nismo pripravljeni ali zavezani sodelovati v postopkih reševanja sporov pred potrošniško arbitražno komisijo.",
    },
    "imprint_privacy_link": {
        "de": "Informationen zur Verarbeitung Ihrer personenbezogenen Daten finden Sie in unserer",
        "en": "Information about the processing of your personal data can be found in our",
        "it": "Le informazioni sul trattamento dei tuoi dati personali sono disponibili nella nostra",
        "sl": "Informacije o obdelavi vaših osebnih podatkov najdete v našem",
    },

    # ===================
    # Admin Page
    # ===================
    "admin_title": {
        "de": "Admin",
        "en": "Admin",
        "it": "Admin",
        "sl": "Admin",
    },
    "admin_controls": {
        "de": "Steuerung",
        "en": "Controls",
        "it": "Controlli",
        "sl": "Nadzor",
    },
    "admin_total_entries": {
        "de": "Einträge gesamt",
        "en": "Total entries",
        "it": "Voci totali",
        "sl": "Skupaj vnosov",
    },
    "admin_mode": {
        "de": "Modus",
        "en": "Mode",
        "it": "Modalità",
        "sl": "Način",
    },
    "admin_readonly": {
        "de": "Nur-Lesen",
        "en": "Read-only",
        "it": "Sola lettura",
        "sl": "Samo za branje",
    },
    "admin_active": {
        "de": "Aktiv",
        "en": "Active",
        "it": "Attivo",
        "sl": "Aktivno",
    },
    "admin_enable_write": {
        "de": "Schreibmodus aktivieren",
        "en": "Enable write mode",
        "it": "Attiva modalità scrittura",
        "sl": "Omogoči način pisanja",
    },
    "admin_enable_readonly": {
        "de": "Nur-Lesen aktivieren",
        "en": "Enable read-only",
        "it": "Attiva sola lettura",
        "sl": "Omogoči samo za branje",
    },
    "admin_csv_export": {
        "de": "CSV-Export",
        "en": "CSV Export",
        "it": "Esporta CSV",
        "sl": "Izvoz CSV",
    },
    "admin_to_guestbook": {
        "de": "Zum Gästebuch",
        "en": "To Guestbook",
        "it": "Al libro degli ospiti",
        "sl": "V knjigo gostov",
    },
    "admin_id": {
        "de": "ID",
        "en": "ID",
        "it": "ID",
        "sl": "ID",
    },
    "admin_date": {
        "de": "Datum",
        "en": "Date",
        "it": "Data",
        "sl": "Datum",
    },
    "admin_action": {
        "de": "Aktion",
        "en": "Action",
        "it": "Azione",
        "sl": "Dejanje",
    },
    "admin_delete": {
        "de": "Löschen",
        "en": "Delete",
        "it": "Elimina",
        "sl": "Izbriši",
    },
    "admin_delete_confirm": {
        "de": "Eintrag von {0} wirklich löschen?",
        "en": "Really delete entry from {0}?",
        "it": "Eliminare davvero la voce di {0}?",
        "sl": "Res želite izbrisati vnos od {0}?",
    },
    "admin_no_entries": {
        "de": "Keine Einträge vorhanden.",
        "en": "No entries available.",
        "it": "Nessuna voce disponibile.",
        "sl": "Ni vnosov.",
    },

    # ===================
    # Error Pages
    # ===================
    "error_rate_limit_title": {
        "de": "Bitte etwas Geduld",
        "en": "Please be patient",
        "it": "Un po' di pazienza",
        "sl": "Prosimo za potrpljenje",
    },
    "error_rate_limit_message": {
        "de": "Sie haben zu viele Anfragen in kurzer Zeit gesendet. Bitte warten Sie einen Moment und versuchen Sie es dann erneut.",
        "en": "You've sent too many requests in a short time. Please wait a moment and try again.",
        "it": "Hai inviato troppe richieste in poco tempo. Attendi un momento e riprova.",
        "sl": "Poslali ste preveč zahtev v kratkem času. Počakajte trenutek in poskusite znova.",
    },
    "error_rate_limit_hint": {
        "de": "Versuchen Sie es in etwa einer Minute erneut.",
        "en": "Try again in about a minute.",
        "it": "Riprova tra circa un minuto.",
        "sl": "Poskusite znova čez približno minuto.",
    },
    "error_back_home": {
        "de": "Zurück zur Startseite",
        "en": "Back to home",
        "it": "Torna alla home",
        "sl": "Nazaj na domačo stran",
    },
    "error_not_found_title": {
        "de": "Seite nicht gefunden",
        "en": "Page not found",
        "it": "Pagina non trovata",
        "sl": "Stran ni najdena",
    },
    "error_not_found_message": {
        "de": "Die angeforderte Seite existiert nicht oder wurde verschoben.",
        "en": "The requested page does not exist or has been moved.",
        "it": "La pagina richiesta non esiste o è stata spostata.",
        "sl": "Zahtevana stran ne obstaja ali je bila premaknjena.",
    },
    "error_generic_title": {
        "de": "Ein Fehler ist aufgetreten",
        "en": "An error occurred",
        "it": "Si è verificato un errore",
        "sl": "Prišlo je do napake",
    },
    "error_generic_message": {
        "de": "Etwas ist schiefgelaufen. Bitte versuchen Sie es später erneut.",
        "en": "Something went wrong. Please try again later.",
        "it": "Qualcosa è andato storto. Riprova più tardi.",
        "sl": "Nekaj je šlo narobe. Poskusite znova pozneje.",
    },
}


def get_translation(key: str, lang: str, *args) -> str:
    """
    Get translation for a key in the specified language.
    Falls back to German if translation not found.
    Supports {0}, {1}, etc. placeholders for formatting.
    """
    if lang not in SUPPORTED_LANGUAGES:
        lang = DEFAULT_LANGUAGE

    translation_dict = TRANSLATIONS.get(key)
    if not translation_dict:
        return key

    text = translation_dict.get(lang) or translation_dict.get(DEFAULT_LANGUAGE) or key

    # Replace placeholders {0}, {1}, etc.
    if args:
        for i, arg in enumerate(args):
            text = text.replace(f"{{{i}}}", str(arg))

    return text


def t(key: str, lang: str, *args) -> str:
    """Shorthand for get_translation."""
    return get_translation(key, lang, *args)


class Translator:
    """Helper class for templates - provides translation with bound language."""

    def __init__(self, lang: str):
        self.lang = lang if lang in SUPPORTED_LANGUAGES else DEFAULT_LANGUAGE

    def __call__(self, key: str, *args) -> str:
        return get_translation(key, self.lang, *args)

    @property
    def current_lang(self) -> str:
        return self.lang

    @property
    def languages(self) -> list:
        return SUPPORTED_LANGUAGES
