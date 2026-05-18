import httpx
from typing import List, Optional
from api.providers.base import BaseProvider
from api.models_cache import ModelInfo
from api.config import OPENROUTER_API_KEY

class OpenRouterProvider(BaseProvider):
    def __init__(self, api_key: Optional[str] = None):
        key = api_key or OPENROUTER_API_KEY
        self.client = httpx.AsyncClient(base_url="https://openrouter.ai/api/v1",
                                        headers={
                                            "Authorization": f"Bearer {key}",
                                            "HTTP-Referer": "https://codecraft.ai",
                                            "X-Title": "Code Craft"
                                        } if key else {})

    async def list_models(self) -> List[ModelInfo]:
        return [
            ModelInfo(provider="openrouter", model_id="anthropic/claude-3.5-sonnet", display_name="Claude 3.5 Sonnet",
                      type="text", logo_url="/logos/openrouter.svg", context_length=200000, cost_per_1k_tokens=0.003),
            ModelInfo(provider="openrouter", model_id="openai/gpt-4o", display_name="GPT-4o",
                      type="text", logo_url="/logos/openrouter.svg", context_length=128000, cost_per_1k_tokens=0.0025),
            ModelInfo(provider="openrouter", model_id="google/gemini-pro-1.5", display_name="Gemini 1.5 Pro",
                      type="text", logo_url="/logos/openrouter.svg", context_length=2000000, cost_per_1k_tokens=0.0025),
        ]

    async def generate(self, model: str, prompt: str,
                       image_base64: Optional[str] = None,
                       generation_type: str = "text") -> dict:
        messages = []
        if image_base64:
            messages.append({
                "role": "user",
                "content": [
                    {"type": "text", "text": prompt},
                    {"type": "image_url", "image_url": {"url": image_base64}}
                ]
            })
        else:
            messages.append({"role": "user", "content": prompt})

        response = await self.client.post("/chat/completions", json={
            "model": model,
            "messages": messages
        }, timeout=60.0)
        data = response.json()
        if "error" in data:
            raise Exception(data["error"].get("message", str(data["error"])))
        content = data["choices"][0]["message"]["content"]
        return {"type": "text", "content": content, "usage": data.get("usage", {})}
