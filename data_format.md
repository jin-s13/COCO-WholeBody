### COCO-WholeBody Annotation File Format

COCO-WholeBody annotation contains all the data of [COCO keypoint annotation](https://cocodataset.org/#format-data)
(including keypoints, num_keypoints, etc.) and additional fields.

Note that, we do not change the existing fields in the COCO keypoint dataset, such as 
"keypoints" and "num_keypoints". 

"keypoints" is a length 3*17 array (x, y, v) for `body` keypoints. 
Each keypoint has a 0-indexed location x,y and a visibility flag v defined as 
v=0: not labeled (in which case x=y=0), 
v=1: labeled but not visible, and 
v=2: labeled and visible. 
A keypoint is considered visible if it falls inside the object segment. 

"num_keypoints" indicates the number of labeled `body` keypoints (v>0), (e.g. crowds and small objects, will have num_keypoints=0). 

Additional fields include:

1) bboxes: `face_box`, `lefthand_box`, `righthand_box` and 

2) whole-body keypoints: `face_kpts`, `lefthand_kpts`, `righthand_kpts`, `foot_kpts` and

3) validity: `face_valid`, `lefthand_valid`, `righthand_valid`, `foot_valid`.

We provide boxes for face/hands. The box is a length 4 array (x, y, w, h), indicating 
its left corner and the width and the height. The box coordinates are measured from the top left image corner and are 0-indexed.

The whole-body keypoint annotation has similar format as "keypoints" in COCO. 
In addition to 17 body keypoints, we have 68 face keypoints, 21 lefthand keypoints, 21 righthand keypoints, 6 foot keypoints.

The validity of the face/hand/foot are used to minimize the labelling uncertainty. 
Only if the face/hand images are clear enough for keypoint labeling (for annotators), the validity is True, otherwise False.
Invalid cases may include severely blur or occlusion. We only label keypoints/boxes for valid cases. 
Invalid boxes/keypoints are simply set as all-zero arrays.


```
annotation{

"face_box": list([x, y, w, h]),
"lefthand_box": list([x, y, w, h]),
"righthand_box": list([x, y, w, h]),

"face_kpts": list([x, y, v] * 68),
"lefthand_kpts": list([x, y, v] * 21),
"righthand_kpts": list([x, y, v] * 21),
"foot_kpts": list([x, y, v] * 6),

"face_valid": bool,
"lefthand_valid": bool,
"righthand_valid": bool,
"foot_valid": bool,

"[cloned]": ...,
}

categories[{
"[cloned]": ...,
}]
```


### Result File Format


Note: keypoint coordinates are floats measured from the top left image corner (and are 0-indexed). 
We recommend rounding coordinates to the nearest pixel to reduce file size. 
Note also that the visibility flags vi are not currently used (except for controlling visualization), 
we recommend simply setting vi=1.

 ```
[{
"image_id": int,
"category_id": int,
"keypoints": list([x, y, v] * 17),
"lefthand_kpts": list([x, y, v] * 21),
"righthand_kpts": list([x, y, v] * 21),
"foot_kpts": list([x, y, v] * 6),
"face_kpts": list([x, y, v] * 68),
"score": float,
}]
```
