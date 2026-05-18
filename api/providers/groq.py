import httpx
from typing import List, Optional
from api.providers.base import BaseProvider
from api.models_cache import ModelInfo
from api.config import GROQ_API_KEY

class GroqProvider(BaseProvider):
    def __init__(self, api_key: Optional[str] = None):
        key = api_key or GROQ_API_KEY
        self.client = httpx.AsyncClient(base_url="https://api.groq.com/openai/v1",
                                        headers={"Authorization": f"Bearer {key}"} if key else {})

    async def list_models(self) -> List[ModelInfo]:
        return [
            ModelInfo(provider="groq", model_id="llama3-8b-8192", display_name="Llama 3 8B",
                      type="text", logo_url="/logos/groq.svg", context_length=8192, cost_per_1k_tokens=0.0005),
            ModelInfo(provider="groq", model_id="mixtral-8x7b-32768", display_name="Mixtral 8x7B",
                      type="text", logo_url="/logos/groq.svg", context_length=32768, cost_per_1k_tokens=0.0007),
            ModelInfo(provider="groq", model_id="llama3-70b-8192", display_name="Llama 3 70B",
                      type="text", logo_url="/logos/groq.svg", context_length=8192, cost_per_1k_tokens=0.0008),
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
