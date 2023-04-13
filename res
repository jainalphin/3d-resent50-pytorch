python -m util_scripts.kinetics_json data/frame_list3 2 data/video/jpg jpg out/label.json


python3 main.py --root_path modules --video_path data --annotation_path labels/label.json \
--result_path results --dataset kinetics --model resnet \
--model_depth 50 --n_classes 2 --batch_size 8 --checkpoint 10  --n_epochs 20




python3 -m util_scripts.kinetics_json modules/frame_list 2 modules/data/kinetics_videos/jpg jpg modules/data/kinetics.json

python3 main.py --root_path "/notebooks/3D-ResNets-PyTorch/modules" --video_path data --annotation_path labels/label.json --result_path results --dataset kinetics --model resnet --model_depth 50 --n_classes 2 --batch_size 128 --checkpoint 10  --n_epochs 20


python3 main.py --root_path "/notebooks/3D-ResNets-PyTorch/modules/data" --video_path kinetics_videos/jpg  --annotation_path kinetics.json --result_path results --dataset kinetics --model resnet --model_depth 50 --n_classes 2 --batch_size 128 --checkpoint 10  --n_epochs 20




python3 main.py --root_path "/notebooks/3D-ResNets-PyTorch/modules/data" --video_path kinetics_videos/jpg  --annotation_path kinetics.json --result_path results --dataset kinetics --model resnet --model_depth 50 --n_classes 2 --batch_size 16 --checkpoint 10  --n_epochs 20

!python3 main.py --root_path "/content/drive/MyDrive/Skylark/resent/3D-ResNets-PyTorch/data"\
           --video_path kinetics_videos/jpg \
           --annotation_path kinetics.json \
           --result_path results --dataset kinetics \
          --model resnet --model_depth 50 \
          --n_classes 2 --batch_size 16 \
          --checkpoint 10  --n_epochs 20 --no_cuda



python3 -m util_scripts.kinetics_json modules/frame_list 2 modules/data/kinetics_videos/jpg jpg modules/data/kinetics.json
