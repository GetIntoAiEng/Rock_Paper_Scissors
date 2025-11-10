
import cv2
from pathlib import Path

# Function to extract video segment between start_time and end_time
def extract_video_segment(input_path, output_path, start_time, end_time):
    # Open the input video
    cap = cv2.VideoCapture(input_path)

    # Get video properties
    fps = cap.get(cv2.CAP_PROP_FPS)
    width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
    height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
    fourcc = cv2.VideoWriter_fourcc(*'mp4v')

    # Calculate start and end frame numbers
    start_frame = int(start_time * fps)
    end_frame = int(end_time * fps)

    # Set the starting frame
    cap.set(cv2.CAP_PROP_POS_FRAMES, start_frame)

    # Create VideoWriter object
    out = cv2.VideoWriter(output_path, fourcc, fps, (width, height))

    current_frame = start_frame
    while cap.isOpened() and current_frame <= end_frame:
        ret, frame = cap.read()
        if not ret:
            break
        out.write(frame)
        current_frame += 1

    # Release resources
    cap.release()
    out.release()
    print(f"Video segment saved to {output_path}")

# define were to find the files and what to cut
if __name__ == '__main__':
    input_path = r'..\videos\Screen Recording 2025-11-10 081021.mp4'
    output_path = r'..\videos\uie68285\Videos\RockPaperScissors.mp4'
    start_time = 105   # seconds
    end_time = 140    # seconds

    
if Path(input_path).is_file():
    extract_video_segment(input_path, output_path, start_time, end_time)
else:
    print("Can't find input file")


    
