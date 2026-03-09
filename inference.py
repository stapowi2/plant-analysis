import sys
import cv2
import numpy as np
from ultralytics import YOLO

def run_inference(image_path):
    model = YOLO('best.pt')
    PX_TO_MM = 0.1090
    
    results = model.predict(image_path, save=True, conf=0.5)
    
    print(f"\n--- Отчет: {image_path} ---")
    for r in results:
        if r.masks:
            for i, mask in enumerate(r.masks.data):
                label = model.names[int(r.boxes.cls[i])]
                

                area_px = float(mask.sum())
                area_mm2 = area_px * (PX_TO_MM ** 2)
                

                mask_np = (mask.cpu().numpy() * 255).astype(np.uint8)
                skeleton = cv2.ximgproc.thinning(mask_np) if hasattr(cv2, 'ximgproc') else mask_np
                length_mm = np.sum(skeleton > 0) * PX_TO_MM
                
                print(f"Объект: {label:10} | Площадь: {area_mm2:8.2f} мм2 | Длина: {length_mm:8.2f} мм")

if __name__ == "__main__":
    if len(sys.argv) > 1:
        run_inference(sys.argv[1])