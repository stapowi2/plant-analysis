from fastapi import FastAPI, UploadFile, File
from ultralytics import YOLO
import cv2
import numpy as np
import io

app = FastAPI(title="Plant Analysis API")

MODEL_PATH = 'best.pt'
PX_TO_MM = 0.1090


model = YOLO(MODEL_PATH)

@app.post("/analyze")
async def analyze_image(file: UploadFile = File(...)):
    request_object_content = await file.read()
    nparr = np.frombuffer(request_object_content, np.uint8)
    img = cv2.imdecode(nparr, cv2.IMREAD_COLOR)


    results = model.predict(img, conf=0.25)
    
    predictions = []
    
    for r in results:
        if r.masks is not None:
            for i, mask in enumerate(r.masks.data):

                cls_id = int(r.boxes.cls[i])
                label = model.names[cls_id]
            
                area_px = float(mask.sum())
                area_mm2 = area_px * (PX_TO_MM ** 2)
                
                predictions.append({
                    "object": label,
                    "area_mm2": round(area_mm2, 2)
                })

    return {"filename": file.filename, "analysis": predictions}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)