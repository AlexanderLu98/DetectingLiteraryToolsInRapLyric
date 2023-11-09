import cv2
import pytesseract

def process_video(video_path):
    # Load the video
    cap = cv2.VideoCapture(video_path)

    while(cap.isOpened()):
        ret, frame = cap.read()

        if ret:
            # Use OCR to extract text
            pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
            text = pytesseract.image_to_string(frame)

            # Print the transcribed text
            print(text)

        else:
            break

    cap.release()
    cv2.destroyAllWindows()

# Test the function
process_video('videosYoutube\Big L on The Enemy - Lyrics, Rhymes Highlighted (034).mp4')
