import cv2
import numpy as np
from tensorflow.lite.python.interpreter import Interpreter


def video_cap_detect(model_path, labels, min_confidence=0.5):
    # Load the TFLite model and set up the interpreter
    interpreter = Interpreter(model_path=model_path)
    interpreter.allocate_tensors()

    # Get input and output details
    input_details = interpreter.get_input_details()
    output_details = interpreter.get_output_details()
    height, width = input_details[0]["shape"][1], input_details[0]["shape"][2]

    # Open a connection to the webcam (use 0 for the default camera)
    cap = cv2.VideoCapture(0)

    while True:
        # Read a frame from the webcam
        ret, frame = cap.read()
        if not ret:
            break

        # Preprocess the input frame
        image_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        image_resized = cv2.resize(image_rgb, (width, height))
        input_data = np.expand_dims(image_resized, axis=0)

        # Normalize pixel values if using a floating model
        if input_details[0]["dtype"] == np.float32:
            input_data = (np.float32(input_data) - 127.5) / 127.5

        # Set input tensor
        interpreter.set_tensor(input_details[0]["index"], input_data)

        # Run inference
        interpreter.invoke()

        # Get output tensors
        boxes = interpreter.get_tensor(output_details[1]["index"])[0]
        classes = interpreter.get_tensor(output_details[3]["index"])[0]
        scores = interpreter.get_tensor(output_details[0]["index"])[0]

        # Process and display results
        for i in range(len(scores)):
            if scores[i] > min_confidence:
                ymin, xmin, ymax, xmax = boxes[i]
                xmin = int(max(1, xmin * frame.shape[1]))
                ymin = int(max(1, ymin * frame.shape[0]))
                xmax = int(min(frame.shape[1], xmax * frame.shape[1]))
                ymax = int(min(frame.shape[0], ymax * frame.shape[0]))

                # Draw bounding box and label
                cv2.rectangle(frame, (xmin, ymin), (xmax, ymax), (0, 255, 0), 2)
                label = f"{labels[int(classes[i])]}: {int(scores[i] * 100)}%"
                cv2.putText(
                    frame,
                    label,
                    (xmin, ymin),
                    cv2.FONT_HERSHEY_SIMPLEX,
                    0.6,
                    (0, 255, 0),
                    2,
                )

        # Display the frame
        cv2.imshow("Object Detection", frame)

        # Break the loop if 'q' key is pressed
        if cv2.waitKey(1) & 0xFF == ord("q"):
            break

    # Release the webcam and close the OpenCV window
    cap.release()
    cv2.destroyAllWindows()
