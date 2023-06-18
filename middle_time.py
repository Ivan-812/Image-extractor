def extract_middle_times(file_path):
    """
    Extracts the middle time of each subtitle in the given .srt file.
    Returns a list of middle times, one for each subtitle.
    """
    # Read the .srt file into a string.
    with open(file_path, 'r', encoding='utf-8') as input_file:
        srt_string = input_file.read()

    # Split the string into individual subtitles.
    subtitles = srt_string.split('\n\n')

    # Extract the middle time of each subtitle.
    middle_times = []
    mid_time_sec_array = []
    for subtitle in subtitles:
        # Split the subtitle into its component parts.
        subtitle_parts = subtitle.split('\n')

        # Skip over any subtitle that doesn't have at least three lines.
        if len(subtitle_parts) < 3:
            continue

        # Extract the start and end times from the subtitle.
        start_time_parts = subtitle_parts[1].split(' --> ')
        start_time = start_time_parts[0]
        end_time = start_time_parts[1]

        # Compute the middle time of the subtitle.
        start_time_secs = time_to_seconds(start_time)
        end_time_secs = time_to_seconds(end_time)
        middle_time_secs = (start_time_secs + end_time_secs) / 2
        middle_time = seconds_to_time(middle_time_secs)

        # Add the middle time to the list of middle times.
        middle_times.append(middle_time)

        mid_time_sec_array.append(middle_time_secs)

    return mid_time_sec_array


def time_to_seconds(time_str):
    """
    Converts a time string in the format HH:MM:SS,mmm to seconds.
    """
    parts = time_str.split(':')
    seconds_parts = parts[2].split(',')
    hours = int(parts[0])
    minutes = int(parts[1])
    seconds = int(seconds_parts[0])
    milliseconds = int(seconds_parts[1])
    total_seconds = (hours * 3600) + (minutes * 60) + seconds + (milliseconds / 1000)
    return total_seconds


def seconds_to_time(seconds):
    """
    Converts a time in seconds to a time string in the format HH:MM:SS,mmm.
    """
    hours = int(seconds // 3600)
    minutes = int((seconds // 60) % 60)
    seconds = int(seconds % 60)
    milliseconds = int((seconds % 1) * 1000)
    time_str = '{:02d}:{:02d}:{:02d},{:03d}'.format(hours, minutes, seconds, milliseconds)
    return time_str


def convert_to_frame_numbers(times, fps):
    frame_numbers = [int(time * fps) for time in times]
    return frame_numbers


if __name__ == '__main__':
    mid_time = extract_middle_times('./radio.srt')
    print(mid_time)
    frames = convert_to_frame_numbers(mid_time, 5)
    print(frames)
