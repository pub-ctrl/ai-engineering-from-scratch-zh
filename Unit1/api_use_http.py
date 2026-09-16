from dotenv import load_dotenv
load_dotenv()

import os, json, urllib.request

url = "https://api.deepseek.com/chat/completions"
headers = {
    "Content-Type": "application/json",
    "Authorization": f"Bearer {os.environ['ANTHROPIC_API_KEY']}",
}
body = json.dumps({
    "model": os.environ.get("LLM_MODEL", "deepseek-flash"),
    "max_tokens": 256,
    "messages": [{"role": "user", "content": "What is a neural network in one sentence?"}],
}).encode()

req = urllib.request.Request(url, data=body, headers=headers, method="POST")
with urllib.request.urlopen(req) as resp:
    result = json.loads(resp.read())
print(result["choices"][0]["message"]["content"])
