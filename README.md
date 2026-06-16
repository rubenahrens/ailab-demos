# AI Impact Lab — demo scripts (sessie 4)

De voorbeeldscripts uit het mini-college **"AI in je app"**. Ze laten in drie stappen
de bouwstenen van een AI-app zien: **interface · sleutel · LLM-call**.

1. **`0_curl-command.txt`** — de kleinst mogelijke AI-call, recht vanuit je terminal (geen app).
2. **`1_chat-openai.py`** — dezelfde call in Python, met streaming.
3. **`2_chat.py`** — een minimale chat-app in Streamlit.

> Het KNVB-voorbeeld staat in een aparte repo: `ailab-llm-poc-knvb`.

## Aan de slag

```bash
python -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt
cp .env.example .env        # zet je eigen OPENAI_API_KEY in .env
```

Draaien:
- **curl:** `export OPENAI_API_KEY=...`, plak daarna de inhoud van `0_curl-command.txt` in je terminal.
- **python:** `python 1_chat-openai.py`
- **streamlit:** `streamlit run 2_chat.py` (key plak je in de zijbalk, of zet hem in `.env`)

## Veiligheid

Zet **nooit** een echte API key in je code, in `0_curl-command.txt`, of in git.
`.env` staat in `.gitignore`; gebruik `.env.example` als sjabloon. Lekt een key toch? Trek hem direct in.
