#AI Face Swap

A real-time face swapping web app built using InsightFace and Gradio.

## Live Demo
🔗 Hugging Face Deployment: https://huggingface.co/spaces/Tanvi308/face-swap-app

## 🛠️ Tech Stack
- **InsightFace** (buffalo_l) — Face detection & analysis
- **inswapper_128.onnx** — Neural face swap model
- **ONNX Runtime** — Model inference
- **OpenCV** — Image processing
- **Gradio** — Web interface
- **Hugging Face Spaces** — Deployment

## ⚙️ How It Works
1. Upload a **source** image (whose face to use)
2. Upload a **target** image (where to place the face)
3. Model detects faces using InsightFace
4. inswapper_128 blends the face seamlessly
5. Result is displayed instantly
