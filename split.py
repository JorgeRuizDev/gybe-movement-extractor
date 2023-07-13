import json
import string
import subprocess

alphabet = string.ascii_lowercase

def split_flac_track(album_path: str, track_path: str, subtracks: dict[str, str], track_idx: str):
    start_time = "00:00:00"
    
    for i, (subtrack_name, subtrack_length) in enumerate(subtracks.items()):
        letter = alphabet[i]
        
        output_file = f'{album_path}/{track_idx}.{letter} {subtrack_name}.flac'
        end_time = calculate_end_time(start_time, subtrack_length)

        print(["ffmpeg", "-i", track_path, "-ss", start_time, "-to", end_time, "-c", "copy", output_file])
        subprocess.run(["ffmpeg", "-i", track_path, "-ss", start_time, "-to", end_time, output_file])
        start_time = end_time  # Update the start time for the next subtrack

def calculate_end_time(start_time: str, subtrack_length: str) -> str:
    start_time_parts = start_time.split(":")
    subtrack_length_parts = subtrack_length.split(":")

    start_time_parts = [int(part) for part in start_time_parts]
    subtrack_length_parts = [int(part) for part in subtrack_length_parts]

    total_time = []
    carry = 0

    for i in range(max(len(start_time_parts), len(subtrack_length_parts))):
        start_part = start_time_parts[-(i+1)] if i < len(start_time_parts) else 0
        length_part = subtrack_length_parts[-(i+1)] if i < len(subtrack_length_parts) else 0

        total_part = start_part + length_part + carry
        carry = total_part // 60
        total_time.insert(0, total_part % 60)

    end_time = ":".join([str(part).zfill(2) for part in total_time])
    return end_time

def split_flac_tracks(json_data: dict, lp_path: str):
    for album, tracks in json_data.items():
        for i, (track, subtracks) in enumerate(tracks.items()):
            album_path = f"{lp_path}/{album}"
            track_path = album_path + "/" + track
            split_flac_track(album_path, track_path, subtracks, str(i+1))
            

def main():
    with open("lps.json", "r", encoding="utf-8") as f:
        json_data = json.load(f)
        split_flac_tracks(json_data, "lps")

if __name__ == "__main__":
    main()