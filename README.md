

# 🌿 EcoScan-AI — Intelligent Waste Detection (Open Source)

EcoScan è unAI locale, gratuita, open-source per analizzare rifiuti, degrado urbano e aiutare l’ambiente.
Works 100% offline, powered by LLaVA models via Ollama.

⸻

🇮🇹 (Italiano)

EcoScan-AI è un sistema di intelligenza artificiale che analizza immagini contenenti rifiuti e ne valuta la gravità.
Tutto gira localmente sul tuo PC, senza API, senza costi e senza inviare dati online.

🔍 Cosa può fare:
	•	Riconoscere rifiuti in una foto
	•	Valutare quantità, tipo e gravità
	•	Generare spiegazioni dettagliate
	•	Analizzare anche testo + immagine
	•	Funzionare tramite bot Telegram
	•	(Opzionale) Chiedere il comune e preparare una segnalazione automatica
	•	Completamente open-source e modificabile

Perfetto per progetti ambientali, civic-tech, scuole, enti locali o analisi urbane.

⸻

🇬🇧 (English)

EcoScan-AI is a local AI system designed to analyze waste in photos and determine pollution severity.
Runs fully offline, using LLaVA models through Ollama.

🔍 Features:
	•	Waste detection in images
	•	Severity and category classification
	•	Text + image reasoning
	•	Optional Telegram bot integration
	•	Optional municipality lookup for automated reporting
	•	Fully open-source, no external API required

Ideal for environmental monitoring, civic-tech solutions, schools, and open AI research.

⸻

📁 Project Structure

EcoScan-AI/
│── main.py
│── analyzer.py
│── telegram_bot.py        (opzionale)
│── comuni.json            (email dei comuni)
│── requirements.txt
│── README.md
│── /images
│── /utils


⸻

⚙️ Installazione

1️⃣ Clona il progetto

git clone https://github.com/tuonome/EcoScan-AI.git
cd EcoScan-AI


⸻

2️⃣ Crea l’ambiente Python

python3 -m venv env
source env/bin/activate


⸻

3️⃣ Installa dipendenze

pip install -r requirements.txt


⸻

4️⃣ Installa Ollama

macOS / Linux

curl -fsSL https://ollama.com/install.sh | sh

Windows

Scarica da https://ollama.com/download

⸻

5️⃣ Scarica il modello AI

Per usare LLaVA versione 7B:

ollama pull llava

Alternative:

ollama pull llava:13b
ollama pull llava-phi
ollama pull llava-llama3


⸻

6️⃣ Avvia Ollama in background

ollama serve


⸻

7️⃣ Avvia EcoScan-AI

python3 main.py


⸻

🧪 Modalità di utilizzo

➤ Analisi di testo

Scrivi un messaggio e l’AI risponde.

➤ Analisi di immagini

Inserisci il percorso di un’immagine locale:

/images/scatto.jpg

Oppure, con il bot Telegram, invia semplicemente una foto.

➤ Modalità ambiente

L’AI riconosce:
	•	presenza di rifiuti
	•	quantità
	•	gravità
	•	suggerimenti di intervento

Se trova un accumulo grave, allora:
	1.	chiede il comune dello scatto
	2.	cerca l’email nel file comuni.json
	3.	prepara automaticamente la segnalazione ambientale (opzionale da attivare)

⸻

📧 Automated Reporting (Optional)

Il file comuni.json contiene le email dei comuni.
Può essere esteso manualmente o automaticamente.

Esempio:

{
  "Catania": "urp@comune.catania.it",
  "Milano": "ambiente@comune.milano.it",
  "Roma": "segnalazioni.ambiente@comune.roma.it"
}


⸻

👨‍💻 Crediti

Creato da Andrea (17 anni)
✔ Appassionato di AI, cybersecurity e sviluppo open-source
✔ Focus su progetti etici e utili alla società

⸻

📜 Licenza — MIT

MIT License  
Copyright (...)

Permission is hereby granted, free of charge, to any person obtaining a copy...


⸻

🤝 Contribuire

Pull request e miglioramenti sono ben accetti!

Puoi contribuire con:
	•	nuovi modelli AI
	•	dataset di addestramento
	•	aggiunta comuni
	•	miglioramento logica ambientale
	•	integrazioni API open-data

⸻

🌱 Perché esiste EcoScan-AI?

Per dimostrare che l’AI non deve essere costosa né centralizzata:
può anche essere libera, locale e al servizio dell’ambiente.

⸻
