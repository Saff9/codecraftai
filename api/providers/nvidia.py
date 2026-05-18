import httpx
from typing import List, Optional
from api.providers.base import BaseProvider
from api.models_cache import ModelInfo
from api.config import NVIDIA_API_KEY

class NvidiaProvider(BaseProvider):
    def __init__(self, api_key: Optional[str] = None):
        key = api_key or NVIDIA_API_KEY
        self.client = httpx.AsyncClient(base_url="https://integrate.api.nvidia.com/v1",
                                        headers={"Authorization": f"Bearer {key}"} if key else {})

    async def list_models(self) -> List[ModelInfo]:
        return [
            ModelInfo(provider="nvidia", model_id="meta/llama-3.1-70b-instruct", display_name="Llama 3.1 70B (NVIDIA)",
                      type="text", logo_url="/logos/nvidia.svg", context_length=128000, cost_per_1k_tokens=0.0008),
            ModelInfo(provider="nvidia", model_id="nvidia/neva-22b", display_name="NeVA 22B Vision",
                      type="text", logo_url="/logos/nvidia.svg", context_length=4096, cost_per_1k_tokens=0.0015),
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
            "messages": messages,
            "max_tokens": 1024
        }, timeout=60.0)
        data = response.json()
        if "error" in data:
            raise Exception(data["error"].get("message", str(data["error"])))
        content = data["choices"][0]["message"]["content"]
        return {"type": "text", "content": content, "usage": data.get("usage", {})}
