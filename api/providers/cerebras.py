import httpx
from typing import List, Optional
from api.providers.base import BaseProvider
from api.models_cache import ModelInfo
from api.config import CEREBRAS_API_KEY

class CerebrasProvider(BaseProvider):
    def __init__(self, api_key: Optional[str] = None):
        key = api_key or CEREBRAS_API_KEY
        self.client = httpx.AsyncClient(base_url="https://api.cerebras.ai/v1",
                                        headers={"Authorization": f"Bearer {key}"} if key else {})

    async def list_models(self) -> List[ModelInfo]:
        return [
            ModelInfo(provider="cerebras", model_id="llama3.1-8b", display_name="Llama 3.1 8B (Cerebras)",
                      type="text", logo_url="/logos/cerebras.svg", context_length=8192, cost_per_1k_tokens=0.0001),
            ModelInfo(provider="cerebras", model_id="llama3.1-70b", display_name="Llama 3.1 70B (Cerebras)",
                      type="text", logo_url="/logos/cerebras.svg", context_length=8192, cost_per_1k_tokens=0.0005),
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
