# AI Face Swap App

An AI-powered face swapping web application built using InsightFace and Gradio. Upload a source face and a target image — the model detects faces and blends them seamlessly using a deep learning ONNX model.

## Live Demo
 **[Hugging Face Spaces](https://huggingface.co/spaces/Tanvi308/face-swap-app)**

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
| <table>
<tr>
<th>Source</th>
<th>Target</th>
<th>Result</th>
</tr>

<tr>
<td><img src="<img width="960" height="1280" alt="WhatsApp Image 2026-05-05 at 12 11 22 PM" src="https://github.com/user-attachments/assets/7c284a96-9e81-4349-b449-3634c4e87636" />" width="250"></td>
<td><img src="<img width="960" height="1280" alt="WhatsApp Image 2026-05-05 at 12 47 01 PM" src="https://github.com/user-attachments/assets/b9a8d1f5-9133-4cf9-ab90-1b61a52dc505" />" width="250"></td>
<td><img src="<img width="960" height="1280" alt="result (1)" src="https://github.com/user-attachments/assets/72030b94-2fca-4bdc-859e-3a05841fedd8" />" width="250"></td>
</tr>
</table> |

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
