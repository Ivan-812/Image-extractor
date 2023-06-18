import imageio
from PIL import Image
import numpy as np


def extract_images(frame_numbers, video_path, output_path, fps):

    # Create a reader object for the video file
    reader = imageio.get_reader(video_path, fps=fps)

    counter = 0

    for frame_num in frame_numbers:
        frame = reader.get_data(frame_num)

        # Assume 'frame' is a numpy array representing an image extracted from a video
        image = Image.fromarray(frame)

        # Calculate new dimensions while preserving aspect ratio
        max_size = 300
        scale = max_size / max(image.size)
        new_width, new_height = [int(dim * scale) for dim in image.size]

        # Resize the image
        resized_image = image.resize((new_width, new_height))

        # Convert the resized image back to a numpy array
        resized_frame = np.array(resized_image)

        imageio.imwrite(output_path + f'sub_{counter}.png', resized_image)
        counter = counter + 1
