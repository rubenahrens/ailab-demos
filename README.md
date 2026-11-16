# AI Impact Lab: demo scripts (sessie 4)

De voorbeeldscripts uit het mini-college **"AI in je app"**. Ze laten in drie stappen
de bouwstenen van een AI-app zien: **interface · sleutel · LLM-call**.

1. **`0_curl-command.txt`**: de kleinst mogelijke AI-call, recht vanuit je terminal (geen app).
   Gebruik je Windows PowerShell? Neem dan **`0_curl-command-powershell.txt`**.
2. **`1_chat-openai.py`**: dezelfde call in Python, met streaming.
3. **`2_chat.py`**: een minimale chat-app in Streamlit.

Alle drie gebruiken de **Chat Completions API** van OpenAI, net als de apps die je in de workshop bouwt.

**Moet ik hier iets mee?** Nee. Voor de workshop-checklist heb je deze repo niet nodig:
Claude bouwt je app in je eigen projectmap. Kijk hier als je wilt zien hoe een AI-call er
onder de motorkap uitziet, of als je de demo's uit het mini-college zelf wilt nadoen.

Het KNVB-voorbeeld uit het mini-college is niet openbaar en staat dus niet in deze repo.

## Aan de slag

### macOS / Linux (bash, zsh)

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
cp .env.example .env        # zet je eigen OPENAI_API_KEY in .env
```

### Windows (PowerShell)

```powershell
python -m venv .venv
.venv\Scripts\Activate.ps1
pip install -r requirements.txt
Copy-Item .env.example .env   # zet je eigen OPENAI_API_KEY in .env
```

> Krijg je bij `Activate.ps1` de melding dat scripts geblokkeerd zijn? Voer eenmalig
> `Set-ExecutionPolicy -Scope CurrentUser RemoteSigned` uit en probeer opnieuw.
>
> Gebruik je Anaconda/conda? Dan kun je de venv-stappen overslaan en direct
> `pip install -r requirements.txt` doen in je conda-omgeving.

## Je key in `.env`

De scripts lezen je key uit het bestand `.env`. Dat bestand maak je zelf:

1. Kopieer `.env.example` naar `.env` (de `cp`- of `Copy-Item`-regel hierboven doet dat).
2. Open `.env` en zet de groeps-key achter `OPENAI_API_KEY=`, zonder aanhalingstekens of spaties.
3. Sla op. `.env` staat in `.gitignore`, dus hij komt nooit in git.

## Welk model?

Alle scripts gebruiken **`gpt-6-luna`**. Met de groeps-key van de workshop werken alleen:

| Model | Waarvoor |
|---|---|
| `gpt-6-luna` | standaard voor alles (tekst en beeld), het goedkoopst |
| `gpt-6-sol` | zwaarder en 20× zo duur; alleen na overleg met de begeleiders |
| `text-embedding-3-small` | embeddings, bijvoorbeeld voor RAG |
| `whisper-1`, `gpt-4o-transcribe` | spraak naar tekst |

Realtime-, tekst-naar-spraak- en beeldgeneratiemodellen werken niet met deze key.

## Draaien

### 1. curl

Zet eerst je key in de terminal (alleen voor deze sessie):

| | Key zetten | Daarna plakken |
|---|---|---|
| **macOS / Linux** | `export OPENAI_API_KEY="sk-..."` | inhoud van `0_curl-command.txt` |
| **Windows PowerShell** | `$env:OPENAI_API_KEY = "sk-..."` | inhoud van `0_curl-command-powershell.txt` |

Waarom een aparte PowerShell-versie? In Windows PowerShell:
- is `curl` een alias voor `Invoke-WebRequest`, dus je hebt `curl.exe` nodig;
- schrijf je omgevingsvariabelen als `$env:OPENAI_API_KEY` in plaats van `$OPENAI_API_KEY`;
- moeten de aanhalingstekens binnen de JSON ge-escaped worden (`\"`).

Tip: op Windows kun je ook **Git Bash** gebruiken; dan werken de macOS/Linux-commando's ongewijzigd.

### 2. Python

| macOS / Linux | Windows PowerShell |
|---|---|
| `python3 1_chat-openai.py` | `python 1_chat-openai.py` |

### 3. Streamlit

```
streamlit run 2_chat.py
```

Werkt op alle platforms. De app leest de key uit `.env`; in de zijbalk zie je of hij gevonden is.

## Veiligheid

Zet **nooit** een echte API key in je code, in de curl-bestanden, of in git.
`.env` staat in `.gitignore`; gebruik `.env.example` als sjabloon. Lekt een key toch? Trek hem direct in.
