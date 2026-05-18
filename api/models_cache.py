from pydantic import BaseModel
from typing import List, Optional

class ModelInfo(BaseModel):
    provider: str
    model_id: str
    display_name: str
    type: str  # text, image, video
    description: Optional[str] = None
    logo_url: Optional[str] = None
    context_length: Optional[int] = 8192
    cost_per_1k_tokens: Optional[float] = 0.0
    is_free: Optional[bool] = False
    capabilities: Optional[List[str]] = []
    tier: Optional[str] = "Professional"

MODELS_CACHE: List[ModelInfo] = [
    # OpenRouter Free Tier
    ModelInfo(
        provider="openrouter",
        model_id="deepseek/deepseek-r1:free",
        display_name="DeepSeek R1 (Free)",
        type="text",
        description="DeepSeek state-of-the-art reasoning model available on OpenRouter free tier.",
        logo_url="/logos/openrouter.svg",
        context_length=65536,
        cost_per_1k_tokens=0.0,
        is_free=True,
        capabilities=["Advanced Reasoning", "Math/Code"],
        tier="Free Tier"
    ),
    ModelInfo(
        provider="openrouter",
        model_id="qwen/qwen-2.5-72b-instruct:free",
        display_name="Qwen 2.5 72B (Free)",
        type="text",
        description="Alibaba Cloud flagship open model on OpenRouter free tier.",
        logo_url="/logos/openrouter.svg",
        context_length=32768,
        cost_per_1k_tokens=0.0,
        is_free=True,
        capabilities=["Tool Use", "Multilingual"],
        tier="Free Tier"
    ),
    ModelInfo(
        provider="openrouter",
        model_id="google/gemma-2-9b-it:free",
        display_name="Gemma 2 9B (Free)",
        type="text",
        description="Google lightweight state-of-the-art open model.",
        logo_url="/logos/openrouter.svg",
        context_length=8192,
        cost_per_1k_tokens=0.0,
        is_free=True,
        capabilities=["General AI"],
        tier="Free Tier"
    ),
    ModelInfo(
        provider="openrouter",
        model_id="meta-llama/llama-3-8b-instruct:free",
        display_name="Llama 3 8B (Free)",
        type="text",
        description="Meta Llama 3 open instruct model.",
        logo_url="/logos/openrouter.svg",
        context_length=8192,
        cost_per_1k_tokens=0.0,
        is_free=True,
        capabilities=["General AI"],
        tier="Free Tier"
    ),
    ModelInfo(
        provider="openrouter",
        model_id="mistralai/mistral-7b-instruct:free",
        display_name="Mistral 7B (Free)",
        type="text",
        description="Mistral AI open weight instruct model.",
        logo_url="/logos/openrouter.svg",
        context_length=8192,
        cost_per_1k_tokens=0.0,
        is_free=True,
        capabilities=["Fast Inference"],
        tier="Free Tier"
    ),
    # Groq Free Tier
    ModelInfo(
        provider="groq",
        model_id="llama-3.3-70b-versatile",
        display_name="Groq Llama 3.3 70B",
        type="text",
        description="Ultra-fast Llama 3.3 70B inference powered by Groq LPU.",
        logo_url="/logos/groq.svg",
        context_length=131072,
        cost_per_1k_tokens=0.0,
        is_free=True,
        capabilities=["Ultra Fast Inference", "Tool Use"],
        tier="Free Tier / LPU"
    ),
    ModelInfo(
        provider="groq",
        model_id="mixtral-8x7b-32768",
        display_name="Groq Mixtral 8x7B",
        type="text",
        description="Mixtral MoE model on Groq LPU.",
        logo_url="/logos/groq.svg",
        context_length=32768,
        cost_per_1k_tokens=0.0,
        is_free=True,
        capabilities=["Ultra Fast Inference"],
        tier="Free Tier / LPU"
    ),
    # Cerebras Free Tier
    ModelInfo(
        provider="cerebras",
        model_id="llama3.1-70b",
        display_name="Cerebras Llama 3.1 70B",
        type="text",
        description="Blazing fast Llama 3.1 70B powered by Cerebras CS-3 wafer-scale engine.",
        logo_url="/logos/cerebras.svg",
        context_length=8192,
        cost_per_1k_tokens=0.0,
        is_free=True,
        capabilities=["Wafer Scale Speed", "Tool Use"],
        tier="Free Tier / CS-3"
    ),
    # Gemini Free Tier
    ModelInfo(
        provider="gemini",
        model_id="gemini-1.5-flash",
        display_name="Gemini 1.5 Flash (Free)",
        type="text",
        description="Google multimodal fast model with 1M context.",
        logo_url="/logos/gemini.svg",
        context_length=1048576,
        cost_per_1k_tokens=0.0,
        is_free=True,
        capabilities=["1M Long Context", "Multimodal Vision"],
        tier="Free Tier"
    ),
    # NVIDIA NIM
    ModelInfo(
        provider="nvidia",
        model_id="meta/llama-3.1-405b-instruct",
        display_name="NVIDIA Llama 3.1 405B",
        type="text",
        description="Meta flagship 405B model hosted on NVIDIA NIM microservices.",
        logo_url="/logos/nvidia.svg",
        context_length=128000,
        cost_per_1k_tokens=0.005,
        is_free=False,
        capabilities=["Flagship 405B", "Senior Code Agent"],
        tier="Enterprise Flagship"
    ),
    ModelInfo(
        provider="nvidia",
        model_id="nvidia/neva-22b",
        display_name="NVIDIA NeVA 22B (Vision)",
        type="image",
        description="NVIDIA NIM multimodal vision model.",
        logo_url="/logos/nvidia.svg",
        context_length=4096,
        cost_per_1k_tokens=0.005,
        is_free=False,
        capabilities=["Multimodal Vision"],
        tier="Professional"
    ),
    # DeepSeek
    ModelInfo(
        provider="deepseek",
        model_id="deepseek-reasoner",
        display_name="DeepSeek R1 (Official)",
        type="text",
        description="Official DeepSeek R1 reasoning model API.",
        logo_url="/logos/deepseek.svg",
        context_length=64000,
        cost_per_1k_tokens=0.002,
        is_free=False,
        capabilities=["Advanced Reasoning", "Math/Code"],
        tier="Expert Reasoning"
    ),
    ModelInfo(
        provider="deepseek",
        model_id="deepseek-chat",
        display_name="DeepSeek V3 (Official)",
        type="text",
        description="Official DeepSeek V3 general chat model API.",
        logo_url="/logos/deepseek.svg",
        context_length=64000,
        cost_per_1k_tokens=0.001,
        is_free=False,
        capabilities=["General AI", "Fast Inference"],
        tier="Professional"
    ),
    # Hugging Face
    ModelInfo(
        provider="huggingface",
        model_id="Qwen/Qwen2.5-Coder-32B-Instruct",
        display_name="HF Qwen 2.5 Coder 32B",
        type="text",
        description="Hugging Face serverless inference for Qwen Coder.",
        logo_url="/logos/huggingface.svg",
        context_length=32768,
        cost_per_1k_tokens=0.001,
        is_free=False,
        capabilities=["Senior Code Agent"],
        tier="Developer Specialized"
    ),
    ModelInfo(
        provider="huggingface",
        model_id="black-forest-labs/FLUX.1-schnell",
        display_name="FLUX.1 Schnell (Image)",
        type="image",
        description="High-speed text-to-image generation model.",
        logo_url="/logos/huggingface.svg",
        context_length=1024,
        cost_per_1k_tokens=0.03,
        is_free=False,
        capabilities=["High Res Image Gen"],
        tier="Flagship Image Gen"
    ),
    ModelInfo(
        provider="huggingface",
        model_id="damo-vilab/text-to-video-ms-1.7b",
        display_name="ModelScope Text-to-Video",
        type="video",
        description="Text-to-video generation animation model.",
        logo_url="/logos/huggingface.svg",
        context_length=1024,
        cost_per_1k_tokens=0.05,
        is_free=False,
        capabilities=["Video Animation Gen"],
        tier="Flagship Video Gen"
    ),
]
