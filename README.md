# AI Face Swap App

An AI-powered face swapping web application built using InsightFace and Gradio. Upload a source face and a target image — the model detects faces and blends them seamlessly using a deep learning ONNX model.

## Live Demo
🔗 Hugging Face Deployment: [https://huggingface.co/spaces/Tanvi308/face-swap-app](https://huggingface.co/spaces/Tanvi308/face-swap-app)

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
| <img src="<img width="960" height="1280" alt="Source" src="https://github.com/user-attachments/assets/1ae2a0b8-a60a-47e9-ba02-49cd2c2d0270" />" width="200"> | <img src="<img width="960" height="1280" alt="Target" src="https://github.com/user-attachments/assets/1f45da4a-fde0-41a6-b7d9-678824ba7232" />" width="200"> | <img src="<img width="960" height="1280" alt="Result" src="https://github.com/user-attachments/assets/542d94fa-8fe9-418d-9d0b-7f51cbf3e37a" />" width="200"> |

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
