from ultralytics import YOLO


# model = YOLO('yolov8s.pt')  

# model.train(
#     data=r"F:\fire_smoke_detection\Fire-Smoke-Detection-Yolov11-2\data.yaml",        
#     epochs=5,             
#     imgsz=416,              
#     batch=8,               
#     name='fire_smoke_yolov8s1',  
#     device="cpu",              
# )


model = YOLO(r"F:\fire_smoke_detection\runs\detect\fire_smoke_yolov8s_12\weights\best.pt")


model.train(
    data=r"F:\fire_smoke_detection\Fire-Smoke-Detection-Yolov11-2\data.yaml",        
    epochs=8,                         
    resume=False,                     
    imgsz=416,
    batch=8,
    device="cpu",
    name='fire_smoke_yolov8s_1',       
    save=True,                       
    save_period=1,   
    project="runs/detect"                  
)
