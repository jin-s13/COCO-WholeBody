# COCO-WholeBody

This is the official repo for ECCV2020 paper ["Whole-Body Human Pose Estimation in the Wild"]. 
The repo contains COCO-WholeBody annotations proposed in this paper.

### What is COCO-WholeBody? 

COCO-WholeBody is the first large-scale benchmark for whole-body pose estimation. 
It has manual annotations on the entire human body, including 133 dense landmarks with 68 on the face, 42 on hands and 23 on the body and feet.
The COCO-WholeBody dataset is an extension of ["COCO 2017 dataset"](https://cocodataset.org/#keypoints-2017). We use the same train/val split as COCO.

Here is an example of one annotated image.
<img src="imgs/Fig1_example.png">

<img src="imgs/Fig3_anno.png">

To measure the annotation quality, we also had 3 annotators to label the same batch of 500 images for face/hand/foot keypoints. 
The standard deviation of the human annotation is calculated for each keypoint, which is used to calculate the normalized factor of whole-body keypoint for evaluation. 
For ``17 body keypoints'', we directly use the standard deviation of COCO.

<img src="imgs/Fig4_dev.png">

### Compare with other popular datasets.

Overview of some popular public datasets for 2D keypoint estimation in RGB images. 
Kpt stands for keypoints, and \#Kpt means the annotated number. 
``Wild'' denotes whether the dataset is collected in-the-wild. * means head box.

|DataSet | Images | \#Kpt | Wild |  Body Box  |    Hand Box   |    Face Box  |   Body Kpt  |    Hand  Kpt  |   Face Kpt | Total|
|-------- | -------- | -------- | -------- | --------  |  --------  |  -------- | -------- | --------  | -------- | --------|
| MPII      | 25K | 16 | ✔️ |  ✔️ |   | * | ✔️|    | | 40K |
| PoseTrack | 23K | 15 | ✔️ | ✔️|   | | ✔️ | |   | 150K  |
|AI Challenger          |  300K | 14 | ✔️ | ✔️  |   |  | ✔️ |    |  | 700K  |
|COCO    | 200K | 17  | ✔️ | ✔️  |   | * | ✔️ |    |  | 250K |
|OneHand10K  | 10K | 21 |✔️  |    | ✔️ | |  | ✔️ | | - |
|SynthHand | 63K |  21 |  |    | ✔️ | |  | ✔️ | | - |
|RHD | 41K |  21 |  |    | ✔️ | |  | ✔️ | | -|
|FreiHand   | 130K | 21 |  |    |  | |  | ✔️ | | - |
|MHP  | 80K | 21  |  |    | ✔️ | |  | ✔️ | | - |
|GANerated | 330K | 21 |   |   |    | |  | ✔️ | | -|
|Panoptic | 15K | 21 |  |   |  ✔️ | |  | ✔️ | | - |
|WFLW | 10K  |  98 | ✔️  |   |   | ✔️ | |    | ✔️ | - |
|AFLW  | 25K  | 19 | ✔️  |   |   | ✔️ | |    | ✔️ | - |
|COFW | 1852 | 29 | ✔️  |   |   | ✔️ | |    | ✔️ | - |
|300W  | 3837 | 68 | ✔️ |   |   | ✔️ | | | ✔️ | -     |
COCO-WholeBody | 200K | 133 | ✔️  | ✔️ | ✔️   |✔️  |  ✔️ | ✔️ | ✔️ | 250K  |


### COCO-WholeBody Benchmark

Whole-body pose estimation results on our WholeBody benchmark.

|Method    |  body |       | foot  |       | face  |       |  hand |       | whole |       |
|----------| ------| ----- | ----- | ----- | ----- | ----- | ----- | ----- | ----- | ----- | 
|          |  AP   | AR    | AP    | AR    |  AP   | AR    | AP    | AR    | AP    | AR    |
|OpenPose  | 0.563 | 0.612 | 0.532 | 0.645 | 0.482 | 0.626 | 0.198 | 0.342 | 0.338 | 0.449 |
|SN        | 0.280 | 0.336 | 0.121 | 0.277 | 0.382 | 0.440 | 0.138 | 0.336 | 0.161 | 0.209 |
|PAF       | 0.266 | 0.328 | 0.100 | 0.257 | 0.309 | 0.362 | 0.133 | 0.321 | 0.141 | 0.185 |
|PAF-body  | 0.409 | 0.470 |   -   |   -   |   -   |   -   |   -   |   -   |   -   |   -   |
|AE        | 0.405 | 0.464 | 0.077 | 0.160 | 0.477 | 0.580 | 0.341 | 0.435 | 0.274 | 0.350 |
|AE-body   | 0.582 | 0.634 |   -   |   -   |   -   |   -   |   -   |   -   |   -   |   -   |
|HRNet     | 0.659 | 0.709 | 0.314 | 0.424 | 0.523 | 0.582 | 0.300 | 0.363 | 0.432 | 0.520 |
|HRNet-body| 0.758 | 0.809 |   -   |   -   |   -   |   -   |   -   |   -   |   -   |   -   |
|ZoomNet   | 0.743 | 0.802 | 0.798 | 0.869 | 0.623 | 0.701 | 0.401 | 0.498 | 0.541 | 0.658 |


### Pre-training on COCO-WholeBody for face/hand keypoint estimation



|Train-set | Test-set | EPE ↓| NME ↓ |
|--------| ------| ----- | ----- |
|CMU Panoptic | CMU Panoptic | 7.49 | 0.68 |
|COCO-WholeBody → CMU Panoptic | CMU Panoptic | 7.00 |  0.63  |
|COCO-WholeBody | COCO-WholeBody  | 2.76 | 6.66 |
| CMU Panoptic → COCO-WholeBody | COCO-WholeBody  | 2.70 | 6.49 |


## Citation

If you find this dataset in your research, please cite this project.

```
@inproceedings{jin2020whole,
  title={Whole-Body Human Pose Estimation in the Wild},
  author={Jin, Sheng and Xu, Lumin and Xu, Jin and Wang, Can and Liu, Wentao and Qian, Chen and Ouyang, Wanli and Luo, Ping},
  booktitle={Proceedings of the European Conference on Computer Vision (ECCV)},    
  year={2020}
}
```

## License

This project is released under the [Apache 2.0 license](LICENSE).



