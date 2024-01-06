from detect_modul import video_cap_detect

# Example usage
model_path = "model/model.tflite"
labels = ["100", "200", "500", "500_2", "1000"]  # Replace with your own class labels
video_cap_detect(model_path, labels)
