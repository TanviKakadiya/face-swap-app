# AI Face Swap App

An AI-powered face swapping web application built using InsightFace and Gradio. Upload a source face and a target image — the model detects faces and blends them seamlessly using a deep learning ONNX model.

## Live Demo
🔗 Hugging Face Deployment: https://huggingface.co/spaces/Tanvi308/face-swap-app
---

## 📌 Features
- 🎯 Accurate face detection using InsightFace (buffalo_l model)
- 🔁 Seamless face blending via inswapper_128.onnx neural model
- 🖼️ Supports any photo — handles lighting & angle differences
- ⚡ Real-time processing with ONNX Runtime
- 🌐 Deployed as a public web app on Hugging Face Spaces

---

## 🛠️ Tech Stack

| Tool | Purpose |
|------|---------|
| InsightFace (buffalo_l) | Face detection & landmark extraction |
| inswapper_128.onnx | Neural face swap & blending |
| ONNX Runtime | Model inference (CPU & GPU) |
| OpenCV | Image read, write & color conversion |
| NumPy | Array & image manipulation |
| Gradio | Web interface |
| Hugging Face Spaces | Cloud deployment |

---



## 📸 Screenshots

| Source | Target | Result |
|--------|--------|--------|
| <img src="<img width="960" height="1280" alt="WhatsApp Image 2026-05-05 at 12 11 22 PM" src="https://github.com/user-attachments/assets/07fac6f6-c09a-4dfe-b470-5053d186231a" />" width="200"> | <img src="<img width="960" height="1280" alt="WhatsApp Image 2026-05-05 at 12 47 01 PM" src="https://github.com/user-attachments/assets/b98dc90e-64b8-474a-8ab8-18f9e87544a0" />" width="200"> | <img src="<img width="960" height="1280" alt="result (1)" src="https://github.com/user-attachments/assets/8167af07-aed5-4cea-85eb-5457d568a315" />" width="200"> |

---

## 📂 Project Structure

```text
face-swap-app/
├── app.py                  # Main Gradio app + face swap logic
├── requirements.txt        # Python dependencies
├── packages.txt            # System dependencies
├── README.md
└── .gitattributes
```

## ⚙️ Run Locally

```bash
git clone https://github.com/TanviKakadiya/face-swap-app.git
cd face-swap-app
pip install -r requirements.txt
python app.py
```

---

## 🔍 How It Works
1. User uploads a **source** image (face to use) and a **target** image
2. InsightFace detects and extracts facial landmarks from both images
3. inswapper_128 model transfers the source face onto each detected face in the target
4. OpenCV blends the result back into the target image naturally
5. Final result is displayed and available to download

---

## 🎯 Future Improvements
- [ ] Video face swapping support
- [ ] Multiple face selection
- [ ] Face enhancement post-processing
- [ ] Mobile-friendly UI

---

## 👩‍💻 Author
**Tanvi Kakadiya**
B.Tech Computer Engineering | AI/ML Enthusiast
🔗 [Hugging Face](https://huggingface.co/Tanvi308)
