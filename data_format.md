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

2) whole-body keypoints: `foot_kpts`, `face_kpts`, `lefthand_kpts`, `righthand_kpts` and

3) validity: `face_valid`, `lefthand_valid`, `righthand_valid`, `foot_valid`.

We provide boxes for face/hands. The box is a length 4 array (x, y, w, h), indicating 
its top left corner and the width and the height. The box coordinates are measured from the top left image corner and are 0-indexed.

The whole-body keypoint annotation has similar format as "keypoints" in COCO. 
In addition to 17 body keypoints, we have 68 face keypoints, 21 lefthand keypoints, 21 righthand keypoints, 6 foot keypoints.
Note that some keypoints may have `float` keypoint visibility. In such cases, `v>0` means that the keypoint is reliable.

The validity of the face/hand/foot are used to minimize the labelling uncertainty. 
Only if the face/hand images are clear enough for keypoint labeling (for annotators), the validity is True, otherwise False.
Invalid cases may include severely blur or occlusion. We only label keypoints/boxes for valid cases. 
Invalid boxes/keypoints are simply set as all-zero arrays.

```
annotation{

"face_box": list([x, y, w, h]),
"lefthand_box": list([x, y, w, h]),
"righthand_box": list([x, y, w, h]),

"foot_kpts": list([x, y, v] * 6),
"face_kpts": list([x, y, v] * 68),
"lefthand_kpts": list([x, y, v] * 21),
"righthand_kpts": list([x, y, v] * 21),

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
Note that the visibility flags `vi` indicate the confidence of the corresponding keypoints. 
We recommend setting `vi=1` for visible and confident predictions, and `vi=0` for invisible or uncertain ones. 
As we evaluate keypoints of different whole-body parts (body, foot, face, lefthand, righthand and wholebody) individually, 
we require a score for each part.
Note that, we do not change the existing fields in the COCO keypoint dataset, 
and use the "score" field to indicate the body score.

 ```
[{
"image_id": int,
"category_id": int,
"keypoints": list([x, y, v] * 17),
"foot_kpts": list([x, y, v] * 6),
"face_kpts": list([x, y, v] * 68),
"lefthand_kpts": list([x, y, v] * 21),
"righthand_kpts": list([x, y, v] * 21),
"score": float,
"foot_score": float,
"face_score": float,
"lefthand_score": float,
"righthand_score": float,
"wholebody_score": float,
}]
```
