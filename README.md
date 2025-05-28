# MCQ Solver AI (Image Input)
🎓 This is a web-based MCQ solver that uses OpenAI GPT to answer multiple choice questions from images.

## 🔍 Features
- Upload an image of a printed or handwritten MCQ
- OCR (Optical Character Recognition) extracts the text using Tesseract.js
- Sends the question to a secure backend connected to OpenAI's GPT model
- Displays the AI-generated answer on the page

## 🚀 How It Works
1. User uploads an image
2. Tesseract.js scans and extracts question text
3. Text is sent to a backend proxy (`/ask`) which talks to OpenAI GPT
4. GPT returns the best answer based on the MCQ

## 🌐 Demo
Visit: [https://guui68.github.io/mcq-ai-web/](https://guui68.github.io/mcq-ai-web/)

## 🛠️ Tech Stack
- HTML, JavaScript, CSS (Frontend)
- Tesseract.js (OCR)
- OpenAI GPT (via backend proxy)

## 📦 Backend Proxy Required
This site uses a backend hosted at `https://mcq-proxy.vercel.app/ask` to keep the OpenAI API key secure.

You can deploy your own backend by cloning [this template](https://vercel.com) and setting the `OPENAI_API_KEY` in `.env`.

---
© 2025 guui68 | AI MCQ Solver with ❤️ by ChatGPT
