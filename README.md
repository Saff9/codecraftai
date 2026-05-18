# Code Craft – Unified AI Generation Platform

Generate text, images, and videos with **10+ providers**, chat memory, web scraping, cost analytics, and encrypted storage. Deploy instantly on Vercel.

## Features
- **Multi‑provider support**: Groq, Cerebras, NVIDIA, OpenRouter, Gemini, Hugging Face, DeepSeek, custom.
- **Text, image, video generation**: Advanced multi-modal AI capabilities.
- **Separate chat threads**: Persistent local memory with AES-GCM encryption.
- **Real‑time cost tracking dashboard**: Budget alerts and usage charts.
- **Web scraping**: Convert any URL directly to clean Markdown.
- **Video playback & Gallery**: Integrated React Player, download, copy, and export.
- **Passphrase protected**: Encrypted local history.
- **Modern UI/UX**: Claude / OpenWebUI / Agentix inspired design, dark/light mode, keyboard shortcuts, PWA.

## Quick Deploy to Vercel
1. Fork / clone this repository.
2. Connect your Vercel account and import the repo.
3. Add environment variables for the providers you want to use (or configure them directly in the frontend Settings UI!):
   - `GROQ_API_KEY`
   - `CEREBRAS_API_KEY`
   - `NVIDIA_API_KEY`
   - `OPENROUTER_API_KEY`
   - `GEMINI_API_KEY`
   - `HUGGINGFACE_API_KEY`
   - `DEEPSEEK_API_KEY`
   (Optional: `CUSTOM_PROVIDERS` – JSON array of custom endpoints)
4. Deploy! The frontend will build automatically.

## Local Development

### Backend
```bash
cd api
pip install -r requirements.txt
uvicorn main:app --reload
```

### Frontend
```bash
cd frontend
npm install
npm run dev
```

## Encryption
All chat history is encrypted using AES‑GCM before storage. You choose a passphrase on first launch. Without it, data is unreadable.

## License
MIT
