from roboflow import Roboflow
rf = Roboflow(api_key="bfMj5TPAyBW7PEA9r6xL")
project = rf.workspace("sayed-gamall").project("fire-smoke-detection-yolov11")
version = project.version(2)
dataset = version.download("yolov8")
                