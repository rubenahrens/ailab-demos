# AI Impact Lab — demo scripts (sessie 4)

De voorbeeldscripts uit het mini-college **"AI in je app"**. Ze laten in drie stappen
de bouwstenen van een AI-app zien: **interface · sleutel · LLM-call**.

1. **`0_curl-command.txt`** — de kleinst mogelijke AI-call, recht vanuit je terminal (geen app).
   Gebruik je Windows PowerShell? Neem dan **`0_curl-command-powershell.txt`**.
2. **`1_chat-openai.py`** — dezelfde call in Python, met streaming.
3. **`2_chat.py`** — een minimale chat-app in Streamlit.

> Het KNVB-voorbeeld staat in een aparte repo: `ailab-llm-poc-knvb`.

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

## Draaien

### 1. curl

Zet eerst je key in de terminal (alleen voor deze sessie):

| | Key zetten | Daarna plakken |
|---|---|---|
| **macOS / Linux** | `export OPENAI_API_KEY="sk-..."` | inhoud van `0_curl-command.txt` |
| **Windows PowerShell** | `$env:OPENAI_API_KEY = "sk-..."` | inhoud van `0_curl-command-powershell.txt` |

Waarom een aparte PowerShell-versie? In Windows PowerShell:
- is `curl` een alias voor `Invoke-WebRequest` — je hebt `curl.exe` nodig;
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

Werkt op alle platforms. De key plak je in de zijbalk, of zet je in `.env`.

## Veiligheid

Zet **nooit** een echte API key in je code, in de curl-bestanden, of in git.
`.env` staat in `.gitignore`; gebruik `.env.example` als sjabloon. Lekt een key toch? Trek hem direct in.
