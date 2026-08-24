import json
from urllib.request import Request, urlopen

SCHEMA = {
    "type": "object", "additionalProperties": False,
    "properties": {"analyses": {"type": "array", "items": {
        "type": "object", "additionalProperties": False,
        "properties": {
            "symbol": {"type": "string"}, "thesis": {"type": "string"},
            "catalysts": {"type": "array", "items": {"type": "string"}},
            "risks": {"type": "array", "items": {"type": "string"}},
            "confidence": {"type": "number"}, "recommendation": {"type": "string"}
        }, "required": ["symbol", "thesis", "catalysts", "risks", "confidence", "recommendation"]
    }}}
}

def analyze_top_candidates(api_key: str, candidates: list[dict], model: str = "gpt-5-mini") -> dict[str, dict]:
    if not api_key or not candidates:
        return {}
    prompt = "Analyze these top paper-trading candidates. Explain signals and risks; do not invent facts, do not place orders, and treat the numeric Python score as authoritative. Return only the requested JSON.\n" + json.dumps(candidates, separators=(",", ":"))
    body = {"model": model, "store": False, "input": [
        {"role": "system", "content": [{"type": "input_text", "text": "You are a cautious market-research assistant. This is research, not financial advice."}]},
        {"role": "user", "content": [{"type": "input_text", "text": prompt}]}
    ], "text": {"format": {"type": "json_schema", "name": "candidate_analysis", "strict": True, "schema": SCHEMA}}}
    request = Request("https://api.openai.com/v1/responses", data=json.dumps(body).encode(),
                      headers={"Authorization": f"Bearer {api_key}", "Content-Type": "application/json"}, method="POST")
    with urlopen(request, timeout=30) as response:
        payload = json.loads(response.read().decode())
    text = payload.get("output_text")
    if not text:
        text = next(part["text"] for item in payload.get("output", []) for part in item.get("content", []) if part.get("type") == "output_text")
    return {item["symbol"].upper(): item for item in json.loads(text).get("analyses", [])}
