from dotenv import load_dotenv
load_dotenv()

import os, json, urllib.request

# 说明：变量名沿用 ANTHROPIC_API_KEY，因为同一个 .env 还要服务 SDK 那条路
# （api_use_sdk.py 里的 anthropic.Anthropic() 空参构造只认 ANTHROPIC_API_KEY
# 和 ANTHROPIC_BASE_URL）。这里的值实际是 DeepSeek 的 key，走 OpenAI 格式端点。
api_key = os.environ.get("ANTHROPIC_API_KEY")
if not api_key:
    raise SystemExit("未找到 ANTHROPIC_API_KEY，请检查项目根目录的 .env 文件")

url = "https://api.deepseek.com/chat/completions"
headers = {
    "Content-Type": "application/json",
    "Authorization": f"Bearer {api_key}",
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
