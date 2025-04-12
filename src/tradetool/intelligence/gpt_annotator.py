from tradetool.intelligence.tag_filter import is_tag_blocked
from tradetool.utils.safe_executor import safe_call

import openai
import os

openai.api_key = os.getenv("OPENAI_API_KEY")

def annotate_entry(entry_result):
    prompt = (
    print("Annotatie gestart door GPT")
"
        f"- Asset: {entry_result.asset}
"
        f"- Richting: {entry_result.direction}
"
        f"- RR: {entry_result.rr}
"
        f"- Confidence: {entry_result.confidence}
"
        f"- Reden: {entry_result.reason}

"
        f"Leg in het kort uit waarom deze entry goed of riskant is. Geef een tag zoals 'early sweep', 'range bias', 'strong confluence' of 'low RR'."
    )

    try:
        response = openai.ChatCompletion.create(
            model="gpt-4",
            messages=[{"role": "user", "content": prompt}],
            max_tokens=100
        )
        tag = response.choices[0].message["content"].strip()
    if is_tag_blocked(tag):
        return f'BLOCKED_TAG::{tag}'
    return tag
    except Exception as e:
        return f"Annotatie mislukt: {e}"
