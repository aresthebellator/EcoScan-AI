# 🌿 EcoScan-AI — Intelligent Waste Detection (Open Source)

EcoScan è un'AI locale, gratuita, open-source per analizzare rifiuti, degrado urbano e aiutare l’ambiente.  
Works 100% offline, powered by LLaVA models via Ollama.

---

# 🇮🇹 (ITA)

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

# 🇬🇧 (ENG)

EcoScan-AI is a local AI system that analyzes images containing waste and determines environmental severity.

Runs **fully offline**:  
✔ No API  
✔ No cloud  
✔ No data sent online  

### 🔍 Features:

• Waste detection in images  
• Severity classification  
• Text + image multimodal analysis  
• Optional Telegram bot  
• Optional municipality auto-reporting  
• Fully open-source & customizable  

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
Windows:
```bash
env\Scripts\activate
```

⸻

3️⃣ Installa le dipendenze Python
```bash
pip install -r requirements.txt
```

⸻

4️⃣ Installa Ollama

macOS / Linux
```bash
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

6️⃣ Avvia Ollama
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

Scrivi un messaggio nel terminale per ricevere una risposta dall’AI.

➤ Analisi di immagini

Specifica il percorso dell’immagine:

images/scatto.jpg

Oppure usa il bot Telegram per inviare direttamente una foto.

➤ Analisi ambientale

L’AI identifica:
	•	presenza di rifiuti
	•	quantità
	•	gravità
	•	suggerimenti per l’intervento

Se rileva accumulo grave, attiva la procedura:
	1.	Chiede il comune
	2.	Cerca email in comuni.json
	3.	Prepara una segnalazione (opzionale)

⸻

📧 Automated Reporting (Optional)

Il file comuni.json contiene email dei comuni italiani.
Esempio:

{
  "Catania": "urp@comune.catania.it",
  "Milano": "ambiente@comune.milano.it",
  "Roma": "segnalazioni.ambiente@comune.roma.it"
}

You can expand this list anytime.
(Puoi ampliarlo quando vuoi.)

⸻

👨‍💻 Crediti / Credits

Creato da Ares (17 anni)
Created by Ares (17 y/o)

✔ Appassionato di AI, cybersecurity e open-source
✔ Focus su progetti etici e utili
✔ Basato su LLaVA + Ollama

⸻

📜 Licenza — MIT License

Open-source. Free to use, modify and distribute.

MIT License
Copyright (...)
Permission is hereby granted, free of charge, to any person obtaining a copy...


⸻

🤝 Contribuire / Contribute

💡 Pull requests are welcome.
Puoi contribuire con / You can contribute by:

• Miglioramenti all’AI
• Aggiunta email dei comuni
• Nuovi modelli supportati
• Ottimizzazione codice
• Documentazione

⸻

🌱 Perché EcoScan-AI?

** 🇮🇹 Perché l’AI non deve essere costosa o centralizzata.
Può essere locale, libera e al servizio dell’ambiente.**

** 🇬🇧 Because AI shouldn’t be expensive or locked behind cloud services.
It can be local, open, and built to protect the environment.**

⸻

✨ EcoScan-AI è un piccolo progetto con un grande obiettivo: usare l’AI per migliorare il mondo, non per complicarlo.
✨ EcoScan-AI is a small project with a big goal: using AI to help the world, not harm it.

---

