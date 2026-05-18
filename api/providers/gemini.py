import httpx
from typing import List, Optional
from api.providers.base import BaseProvider
from api.models_cache import ModelInfo
from api.config import GEMINI_API_KEY

class GeminiProvider(BaseProvider):
    def __init__(self, api_key: Optional[str] = None):
        self.api_key = api_key or GEMINI_API_KEY
        self.client = httpx.AsyncClient(base_url="https://generativelanguage.googleapis.com/v1beta/models")

    async def list_models(self) -> List[ModelInfo]:
        return [
            ModelInfo(provider="gemini", model_id="gemini-1.5-flash-latest", display_name="Gemini 1.5 Flash",
                      type="text", logo_url="/logos/gemini.svg", context_length=1048576, cost_per_1k_tokens=0.00035),
            ModelInfo(provider="gemini", model_id="gemini-1.5-pro-latest", display_name="Gemini 1.5 Pro",
                      type="text", logo_url="/logos/gemini.svg", context_length=2097152, cost_per_1k_tokens=0.00125),
        ]

    async def generate(self, model: str, prompt: str,
                       image_base64: Optional[str] = None,
                       generation_type: str = "text") -> dict:
        if not self.api_key:
            raise Exception("Gemini API key is missing")

        contents = []
        if image_base64:
            # strip data:image/...;base64, prefix if present
            b64_data = image_base64.split(",")[-1] if "," in image_base64 else image_base64
            contents.append({
                "parts": [
                    {"text": prompt},
                    {"inline_data": {"mime_type": "image/jpeg", "data": b64_data}}
                ]
            })
        else:
            contents.append({"parts": [{"text": prompt}]})

        url = f"/{model}:generateContent?key={self.api_key}"
        response = await self.client.post(url, json={"contents": contents}, timeout=60.0)
        data = response.json()
        if "error" in data:
            raise Exception(data["error"].get("message", str(data["error"])))
        
        try:
            content = data["candidates"][0]["content"]["parts"][0]["text"]
            # Mock usage for cost calculation
            usage = {
                "prompt_tokens": data.get("usageMetadata", {}).get("promptTokenCount", len(prompt) // 4),
                "completion_tokens": data.get("usageMetadata", {}).get("candidatesTokenCount", len(content) // 4)
            }
            return {"type": "text", "content": content, "usage": usage}
        except Exception as e:
            raise Exception(f"Failed to parse Gemini response: {str(data)}")
