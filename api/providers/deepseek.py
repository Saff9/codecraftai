import httpx
from typing import List, Optional
from api.providers.base import BaseProvider
from api.models_cache import ModelInfo
from api.config import DEEPSEEK_API_KEY

class DeepSeekProvider(BaseProvider):
    def __init__(self, api_key: Optional[str] = None):
        key = api_key or DEEPSEEK_API_KEY
        self.client = httpx.AsyncClient(base_url="https://api.deepseek.com/v1",
                                        headers={"Authorization": f"Bearer {key}"} if key else {})

    async def list_models(self) -> List[ModelInfo]:
        return [
            ModelInfo(provider="deepseek", model_id="deepseek-chat", display_name="DeepSeek V3 (Chat)",
                      type="text", logo_url="/logos/deepseek.svg", context_length=65536, cost_per_1k_tokens=0.00014),
            ModelInfo(provider="deepseek", model_id="deepseek-coder", display_name="DeepSeek Coder",
                      type="text", logo_url="/logos/deepseek.svg", context_length=65536, cost_per_1k_tokens=0.00028),
        ]

    async def generate(self, model: str, prompt: str,
                       image_base64: Optional[str] = None,
                       generation_type: str = "text") -> dict:
        response = await self.client.post("/chat/completions", json={
            "model": model,
            "messages": [{"role": "user", "content": prompt}]
        }, timeout=60.0)
        data = response.json()
        if "error" in data:
            raise Exception(data["error"].get("message", str(data["error"])))
        content = data["choices"][0]["message"]["content"]
        return {"type": "text", "content": content, "usage": data.get("usage", {})}
