from dotenv import load_dotenv
load_dotenv()                                  # 自动读取最近的 .env

import os
import anthropic

client = anthropic.Anthropic()   # 靠 ANTHROPIC_BASE_URL / ANTHROPIC_API_KEY 两个环境变量

MODEL = os.environ.get("LLM_MODEL", "deepseek-flash")
response = client.messages.create(
    model=MODEL,
    max_tokens=256,
    messages=[{"role": "user", "content": "What is a neural network in one sentence?"}],
)

"""
for block in response.content:
    if block.type == "thinking":
        print("[思维链]", block.thinking)      # 可选：看模型的推理过程
    elif block.type == "text":
        print(block.text)
"""

print("".join(b.text for b in response.content if b.type == "text"))
