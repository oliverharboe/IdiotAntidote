from openai import OpenAI
from mistralai import Mistral
import os
from dotenv import load_dotenv

# gets apikeys from .env file


load_dotenv()
MISTRAL_KEY = os.getenv("MISTRAL_KEY")


### PROMPT STUFF ###

SYSTEM_CONTENT = """
Du er ekspert i undervisning.

Generér 1 flashcard (spørgsmål og svar) baseret på et givet tekststykke.

Krav:
- Stil kun ét spørgsmål, som tester vigtig viden fra teksten.
- Spørgsmålet må ikke referere til billeder, tabeller eller eksternt materiale.
- Spørgsmålet skal kunne besvares uden at have teksten foran sig.
- Svaret må højst være 4 sætninger langt.
- Omskriv teksten til pædagogisk og letforståeligt sprog – undgå at gentage ordlyden direkte.
- Giv kun ét flashcard (ét spørgsmål og ét svar).
- Returnér intet andet end dette: `"Question: [spørgsmål] #||# Answer: [svar]"` (inkluder citationstegn og nøjagtig formatering).

Svarformat:
"Question: Hvad er fotosyntese? #||# Answer: Fotosyntese er den proces, hvor planter omdanner sollys til energi."

Svar altid i én linje som vist. INGEN forklaringer, mellemrum eller ekstra tekst, og skriv kun Question og Answer en gang.
"""



def deepseek_model(chunk):
    """
    uses deepseek model to generate flashcards 
    """
    client = OpenAI(
        api_key = 'DEEPSEEK_KEY',
        base_url = "https://api.deepseek.com"
    )
    response = client.chat.completions.create(
        model = "deepseek-chat",
        messages=[
            {"role": "system", "content": SYSTEM_CONTENT},
            {"role": "user", "content": f"TEMATEKST:\n{chunk}"}
        ]
    )
    return response.choices[0].message.content
    
def openai_model(chunk):
    """
    uses openai model to generate flashcards
    """
    client = OpenAI(api_key = 'OPENAI_KEY',)
    response = client.chat.completions.create(
        model = "gpt-4o-mini",
        messages=[
            {"role": "system", "content": SYSTEM_CONTENT},
            {"role": "user", "content": f"TEMATEKST:\n{chunk}"}
        ]
    )
    return response.choices[0].message.content


def mistral_model(chunk):
    # uses mistral model free tier 
    model = "mistral-small-latest"
    client = Mistral(api_key=MISTRAL_KEY)
    chat_response = client.chat.complete(
        model=model,
        messages = [
            {"role": "system", "content": SYSTEM_CONTENT},
            {"role": "user", "content": f"TEMATEKST:\n{chunk}"}
        ]
    )
    return chat_response.choices[0].message.content