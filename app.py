import gradio as gr
import cv2
import insightface
from insightface.app import FaceAnalysis
from insightface.model_zoo import get_model
import numpy as np
import os
import urllib.request

# Load models at startup
app_face = FaceAnalysis(name='buffalo_l', providers=['CPUExecutionProvider'])
app_face.prepare(ctx_id=0, det_size=(640, 640))

model_path = "inswapper_128.onnx"
if not os.path.exists(model_path):
    print("Downloading model...")
    url = "https://github.com/deepinsight/insightface/releases/download/v0.7/inswapper_128.onnx"
    urllib.request.urlretrieve(url, model_path)
    print("Downloaded!")

swapper = get_model(model_path, download=False)

def face_swap(source_img, target_img):
    if source_img is None or target_img is None:
        return None, "Please upload both images."
    
    src = cv2.cvtColor(np.array(source_img), cv2.COLOR_RGB2BGR)
    dst = cv2.cvtColor(np.array(target_img), cv2.COLOR_RGB2BGR)

    src_faces = app_face.get(src)
    dst_faces = app_face.get(dst)

    if len(src_faces) == 0:
        return None, "No face detected in source image!"
    if len(dst_faces) == 0:
        return None, "No face detected in target image!"

    result = dst.copy()
    for face in dst_faces:
        result = swapper.get(result, face, src_faces[0], paste_back=True)

    result_rgb = cv2.cvtColor(result, cv2.COLOR_BGR2RGB)
    return result_rgb, "✅ Face swap successful!"

demo = gr.Interface(
    fn=face_swap,
    inputs=[
        gr.Image(type="pil", label="Source Face (whose face to use)"),
        gr.Image(type="pil", label="Target Image (where to place the face)")
    ],
    outputs=[
        gr.Image(label="Result"),
        gr.Text(label="Status")
    ],
    title="AI Face Swap",
    description="Upload a source face and a target image. The source face will be swapped onto the target."
)

demo.launch()