import whisper
import argparse
import os

def generate_srt(video_path):
    """
    Generates an SRT subtitle file from a video file.

    Args:
        video_path (str): The path to the video file.
    """
    print(f"Loading Whisper model...")
    model = whisper.load_model("base")

    print(f"Transcribing video: {video_path}")
    result = model.transcribe(video_path, verbose=True)

    srt_path = os.path.splitext(video_path)[0] + ".srt"
    
    with open(srt_path, "w", encoding="utf-8") as srt_file:
        for i, segment in enumerate(result['segments']):
            start, end, text = segment['start'], segment['end'], segment['text']
            srt_file.write(f"{i + 1}\n")
            srt_file.write(f"{int(start // 3600):02}:{int(start % 3600 // 60):02}:{int(start % 60):02},{int(start * 1000 % 1000):03} --> {int(end // 3600):02}:{int(end % 3600 // 60):02}:{int(end % 60):02},{int(end * 1000 % 1000):03}\n")
            srt_file.write(f"{text.strip()}\n\n")

    print(f"SRT file generated at: {srt_path}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Generate SRT subtitles from a video file.")
    parser.add_argument("video_path", help="The path to the video file.")
    args = parser.parse_args()

    if not os.path.exists(args.video_path):
        print(f"Error: Video file not found at: {args.video_path}")
    else:
        generate_srt(args.video_path)
