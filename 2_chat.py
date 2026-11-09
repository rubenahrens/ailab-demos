"""
2_chat.py - je eerste AI-app (AI Impact Lab, sessie 4)

Een minimale chatbot in ~50 regels. Hij laat de DRIE BOUWSTENEN van een AI-app zien:
  1. De interface - wat de gebruiker ziet en doet (Streamlit)
  2. De sleutel   - je toegangspas tot het model (uit het bestand .env)
  3. De LLM-call  - je bericht heen, het antwoord terug (OpenAI)

Starten:
  pip install -r requirements.txt      # streamlit, openai, python-dotenv
  cp .env.example .env                 # zet je key achter OPENAI_API_KEY=
  streamlit run 2_chat.py
"""

import os
import streamlit as st
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()  # leest OPENAI_API_KEY uit het bestand .env in deze map

# Welke modellen mag de gebruiker kiezen (klein en goedkoop voor de workshop)
ALLOWED_MODELS = ["gpt-6-luna"]
# Max. aantal tokens dat het model mag teruggeven (houdt kosten in toom)
MAX_OUTPUT_TOKENS = 8000

# Zo praat de assistent. Pas deze tekst aan en zie het verschil! (stap 3)
SYSTEEM_PROMPT = (
    "Je bent een vriendelijke sport-assistent. Je geeft korte, duidelijke antwoorden. "
    "Je mag ook een beetje humor gebruiken, maar blijf beleefd. "
    "Als je het antwoord niet weet, zeg dat dan eerlijk."
)

# ---- BOUWSTEEN 1: de interface ----------------------------------------------
st.title("Sport-assistent")

with st.sidebar:
    # ---- BOUWSTEEN 2: de sleutel --------------------------------------------
    # De key staat in .env, niet in de code en niet in de app.
    api_key = os.environ.get("OPENAI_API_KEY", "")
    if api_key:
        st.success("Key gevonden in .env")
    else:
        st.warning("Geen key gevonden. Zet OPENAI_API_KEY=... in het bestand .env en herstart de app.")
    model = st.selectbox("Model", ALLOWED_MODELS)  # standaard het eerste: gpt-6-luna

# Bewaar de gespreksgeschiedenis tussen berichten door
if "messages" not in st.session_state:
    st.session_state.messages = []

# Toon de berichten tot nu toe
for bericht in st.session_state.messages:
    with st.chat_message(bericht["role"]):
        st.markdown(bericht["content"])

# Wacht op een nieuwe vraag van de gebruiker
if vraag := st.chat_input("Typ je vraag..."):
    if not api_key:
        st.warning("Geen key gevonden. Zet OPENAI_API_KEY=... in het bestand .env en herstart de app.")
        st.stop()

    st.session_state.messages.append({"role": "user", "content": vraag})
    with st.chat_message("user"):
        st.markdown(vraag)

    # ---- BOUWSTEEN 3: de LLM-call -------------------------------------------
    client = OpenAI(api_key=api_key)
    try:
        antwoord = client.chat.completions.create(
            model=model,
            messages=[{"role": "system", "content": SYSTEEM_PROMPT}, *st.session_state.messages],
            max_completion_tokens=MAX_OUTPUT_TOKENS,
        ).choices[0].message.content
    except Exception as fout:
        st.error(f"Er ging iets mis bij de LLM-call: {fout}")
        st.stop()

    # Redenerende modellen (gpt-6-luna) geven soms None terug als het
    # token-budget op is. Vang dat af zodat de app niet crasht.
    if not antwoord:
        antwoord = "(Geen antwoord ontvangen - probeer het opnieuw of verhoog MAX_OUTPUT_TOKENS.)"

    with st.chat_message("assistant"):
        st.markdown(antwoord)
    st.session_state.messages.append({"role": "assistant", "content": antwoord})
