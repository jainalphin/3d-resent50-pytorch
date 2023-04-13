import argparse
import json
import os.path
from pathlib import Path

import cv2

dictData = {0: 'nonviolence', 1: 'violence'}


def get_n_frames(video_path):
    return len([
        x for x in video_path.iterdir()
        if 'image' in x.name and x.name[0] != '.'
    ])


def convert_video_jpg(video_path, jpg_path):
    path = video_path
    print(f"[INFO] Old Path: ", path)

    # new_path = path.replace(data_path, resize_path)
    new_path = jpg_path
    # folder = "/".join(new_path.split("/")[:-1])
    if not os.path.isdir(new_path):
        os.makedirs(new_path)

    print(f"[INFO] New Path : ", new_path)

    cap = cv2.VideoCapture(path)

    if not cap.isOpened():
        print(f"{path} is not opened")
    i = 0
    while cap.isOpened():
        i += 1
        ret, frame = cap.read()
        if not ret:
            print(f"[INFO] : Video : {path} is Finished With I : {i}....\n")
            break
        rescaled_frame = cv2.resize(frame, (256, 256), interpolation=cv2.INTER_AREA)
        path_to_save = new_path + '/' + 'image_' + format(i, '05') + ".jpg"
        cv2.imwrite(path_to_save, rescaled_frame)

    cv2.destroyAllWindows()
    cap.release()

def convert_kinetics_csv_to_json(test_video_path, dst_json_path= Path("data/kinetics.json")):
    path_id = test_video_path.split("/")[-1].split(".")[0]
    jpg_path = f"data/test/{path_id}"
    convert_video_jpg(test_video_path, jpg_path=jpg_path)

    if os.path.exists(test_video_path):
        n_frames = get_n_frames(Path(jpg_path))
        database = {path_id: {"subset": "testing", "annotations": {"segment": (1, n_frames + 1)}}}

        dst_data = {}
        dst_data['labels'] = {"Violence": 1, "NonViolence": 0}
        dst_data['database'] = {}
        dst_data['database'].update(database)

        with dst_json_path.open('w') as dst_file:
            json.dump(dst_data, dst_file)
    else:
        print("Test video path not exists")


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('video_path',
                        default=None,
                        type=str,
                        help=('Path of video directory '
                              'Using to get n_frames of each video.'))

    args = parser.parse_args()
    convert_kinetics_csv_to_json(args.video_path)
