import middle_time
import compile_image


# Set the desired frame rate
fps = 5
mid_time = middle_time.extract_middle_times('./radio.srt')
print(mid_time)
frame_nums = middle_time.convert_to_frame_numbers(mid_time, fps)
print(frame_nums)

# Set the path to the video file
video_path = '/content/drive/MyDrive/video-subtitle-extractor-main/test/radio_finished.mp4'
output_path = '/content/drive/MyDrive/video-subtitle-extractor-main/test/'

compile_image.extract_images(frame_nums, video_path, output_path, fps)