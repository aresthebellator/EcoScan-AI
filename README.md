
# 🌿 EcoScan-AI — Intelligent Waste Detection (Open Source)

EcoScan è un'AI locale, gratuita, open-source per analizzare rifiuti, degrado urbano e aiutare l’ambiente.  
Works 100% offline, powered by LLaVA models via Ollama.

---

# 🇮🇹 Italiano

EcoScan-AI è un sistema di intelligenza artificiale che analizza immagini contenenti rifiuti, ne valuta la gravità e fornisce un’analisi ambientale completa.

Funziona **totalmente in locale**, sul tuo PC:  
✔ Nessuna API esterna  
✔ Nessun costo  
✔ Nessun invio di foto online  

### 🔍 Cosa può fare:

• Riconoscere rifiuti in una foto  
• Valutare quantità, tipo e gravità  
• Generare spiegazioni dettagliate  
• Analizzare testo + immagini insieme  
• Funzionare tramite bot Telegram  
• (Opzionale) Chiedere il comune dello scatto  
• (Opzionale) Preparare una segnalazione automatica al comune  
• Completamente open-source e modificabile  

Perfetto per progetti ambientali, civic-tech, scuole, enti locali e analisi urbane.

---

# 🇬🇧 English Version

EcoScan-AI is a local AI system that analyzes photos containing waste and determines the environmental severity.

Everything runs **fully offline** on your machine:  
✔ No API  
✔ No cloud  
✔ No data sent online  

### 🔍 Features:

• Waste detection in images  
• Severity and category classification  
• Text + image deep analysis  
• Optional Telegram bot integration  
• Optional municipality auto-reporting (email)  
• Fully open-source & customizable  

Ideal for environmental monitoring, civic-tech, schools, and AI research.

---

# 📁 Project Structure

EcoScan-AI/
│── main.py
│── analyzer.py
│── telegram_bot.py        (opzionale)
│── comuni.json            (email dei comuni)
│── requirements.txt
│── README.md
│── /images
│── /utils

---

# ⚙️ Installazione

## 1️⃣ Clona il progetto

```bash
git clone https://github.com/tuonome/EcoScan-AI.git
cd EcoScan-AI
```

⸻

2️⃣ Crea un ambiente virtuale Python

```bash
python3 -m venv env
source env/bin/activate
```
Su Windows:
```bash 
env\Scripts\activate

```
⸻

3️⃣ Installa le dipendenze Python

``` bash  
pip install -r requirements.txt
```
⸻

4️⃣ Installa Ollama

macOS / Linux
``` bash
curl -fsSL https://ollama.com/install.sh | sh
```
Windows

Scarica da:
```bash
https://ollama.com/download
```

⸻

5️⃣ Scarica il modello LLaVA

LLaVA 7B (consigliato):
```bash
ollama pull llava

Alternative:

ollama pull llava:13b
ollama pull llava-phi
ollama pull llava-llama3
```

⸻

6️⃣ Avvia Ollama in background

```bash
ollama serve
```

⸻

7️⃣ Avvia EcoScan-AI

```bash
python3 main.py
```

⸻

🧪 Modalità di utilizzo

➤ Analisi di testo

Scrivi un messaggio nel terminale e l’AI risponderà.

➤ Analisi di immagini

Inserisci il percorso dell’immagine:

images/scatto.jpg

Con bot Telegram: basta inviare una foto.

➤ Modalità “Ambiente”

L’AI riconosce:

• Presenza di rifiuti
• Quantità (bassa, media, alta)
• Gravità
• Suggerimenti reali per intervenire

Se viene rilevato un accumulo grave, l’AI:
	1.	Chiede il comune dove è stata scattata la foto
	2.	Cerca l’email nel file comuni.json
	3.	Prepara automaticamente una segnalazione ambientale (opzionale)

⸻

📧 Automated Reporting (Optional)

Il file comuni.json contiene le email dei comuni italiani.

Esempio:

{
  "Catania": "urp@comune.catania.it",
  "Milano": "ambiente@comune.milano.it",
  "Roma": "segnalazioni.ambiente@comune.roma.it"
}

Puoi estendere il file con quanti comuni vuoi.

⸻

👨‍💻 Crediti

Creato da Ares (17 anni)
✔ Appassionato di AI, cybersecurity e sviluppo open-source
✔ Focus su progetti etici, utili e accessibili
✔ Basato su LLaVA + Ollama

⸻

📜 Licenza — MIT

MIT License
Copyright (...)

Permission is hereby granted, free of charge, to any person obtaining a copy...


⸻

🤝 Contribuire

Pull request e miglioramenti sono ben accetti!

Puoi contribuire con:

• Nuovi modelli AI
• Dataset ambientali
• Aggiunta email dei comuni
• Miglioramento logica di analisi
• Integrazioni open-data
• Funzionalità nel bot Telegram

⸻

🌱 Perché EcoScan-AI?

Per dimostrare che l’AI non deve essere costosa né centralizzata:
può essere libera, locale e al servizio dell’ambiente.

---
