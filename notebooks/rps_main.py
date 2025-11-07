import cv2
import mediapipe as mp
import time

mp_hands = mp.solutions.hands
mp_drawing = mp.solutions.drawing_utils

def live_hand_tracking():
    cap = cv2.VideoCapture(0)
    if not cap.isOpened():
        print("Fehler: Kamera konnte nicht geöffnet werden.")
        return

    countdown_texts = ["ONE", "TWO", "THREE"]
    countdown_index = 0
    countdown_start = time.time()

    with mp_hands.Hands(max_num_hands=1, min_detection_confidence=0.7, min_tracking_confidence=0.7) as hands:
        print("Handtracking gestartet. Drücke ESC zum Beenden.")
        while True:
            ret, frame = cap.read()
            if not ret:
                break

            # MediaPipe Verarbeitung
            image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            image.flags.writeable = False
            results = hands.process(image)

            image.flags.writeable = True
            image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)

            # Hand-Landmarks zeichnen
            if results.multi_hand_landmarks:
                for hand_landmarks in results.multi_hand_landmarks:
                    mp_drawing.draw_landmarks(image, hand_landmarks, mp_hands.HAND_CONNECTIONS)

            # Countdown-Text einfügen (für die ersten 3 Sekunden)
            if countdown_index < len(countdown_texts):
                if time.time() - countdown_start >= countdown_index + 1:
                    countdown_index += 1
                if countdown_index < len(countdown_texts):
                    text = countdown_texts[countdown_index]
                    h, w, _ = image.shape
                    font = cv2.FONT_HERSHEY_SIMPLEX
                    font_scale = 3
                    thickness = 6
                    color = (255, 255, 255)
                    (text_width, text_height), _ = cv2.getTextSize(text, font, font_scale, thickness)
                    x = (w - text_width) // 2
                    y = (h + text_height) // 2
                    cv2.putText(image, text, (x, y), font, font_scale, color, thickness, cv2.LINE_AA)

            cv2.imshow("Rock-Paper-Scissors", image)

            if cv2.waitKey(1) & 0xFF == 27:
                break

    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    live_hand_tracking()