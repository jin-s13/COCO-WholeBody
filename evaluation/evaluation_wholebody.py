from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import argparse
import warnings
from pycocotools.coco import COCO

from myeval_body import MYeval_body
from myeval_foot import MYeval_foot
from myeval_face import MYeval_face
from myeval_lefthand import MYeval_lefthand
from myeval_righthand import MYeval_righthand
from myeval_wholebody import MYeval_wholebody

def parse_args():
    parser = argparse.ArgumentParser(description='COCO-WholeBody mAP Evaluation')
    parser.add_argument('--res_file',
                        help='tha path to result file',
                        required=True,
                        type=str)
    parser.add_argument('--gt_file',
                        help='tha path to gt file',
                        required=True,
                        type=str)
    args = parser.parse_args()
    return args

def test_body(coco,coco_dt):
    print('body mAP ----------------------------------')
    check_part_score(coco_dt, 'body')
    coco_eval = MYeval_body(coco, coco_dt, 'keypoints')
    coco_eval.params.useSegm = None
    coco_eval.evaluate()
    coco_eval.accumulate()
    coco_eval.summarize()
    return 0

def test_foot(coco,coco_dt):
    print('foot mAP ----------------------------------')
    check_part_score(coco_dt, 'foot')
    coco_eval = MYeval_foot(coco, coco_dt, 'keypoints')
    coco_eval.params.useSegm = None
    coco_eval.evaluate()
    coco_eval.accumulate()
    coco_eval.summarize()
    return 0

def test_face(coco,coco_dt):
    print('face mAP ----------------------------------')
    check_part_score(coco_dt, 'face')
    coco_eval = MYeval_face(coco, coco_dt, 'keypoints')
    coco_eval.params.useSegm = None
    coco_eval.evaluate()
    coco_eval.accumulate()
    coco_eval.summarize()
    return 0

def test_lefthand(coco,coco_dt):
    print('lefthand mAP ----------------------------------')
    check_part_score(coco_dt, 'lefthand')
    coco_eval = MYeval_lefthand(coco, coco_dt, 'keypoints')
    coco_eval.params.useSegm = None
    coco_eval.evaluate()
    coco_eval.accumulate()
    coco_eval.summarize()
    return 0

def test_righthand(coco,coco_dt):
    print('righthand mAP ----------------------------------')
    check_part_score(coco_dt, 'righthand')
    coco_eval = MYeval_righthand(coco, coco_dt, 'keypoints')
    coco_eval.params.useSegm = None
    coco_eval.evaluate()
    coco_eval.accumulate()
    coco_eval.summarize()
    return 0

def test_wholebody(coco,coco_dt):
    print('wholebody mAP ----------------------------------')
    coco_eval = MYeval_wholebody(coco, coco_dt, 'keypoints')
    coco_eval.params.useSegm = None
    coco_eval.evaluate()
    coco_eval.accumulate()
    coco_eval.summarize()
    return 0

def check_part_score(coco_dt, part):
    flag_no_part_score = False
    for k in coco_dt.anns.keys():
        if '{}_score'.format(part) not in coco_dt.anns[k]:
            flag_no_part_score = True
            coco_dt.anns[k]['{}_score'.format(part)] = coco_dt.anns[k]['score']
    if flag_no_part_score:
        warnings.warn("'{}_score' not found, use 'score' instead.".format(part))

def main():
    args = parse_args()
    coco = COCO(args.gt_file)

    coco_dt = coco.loadRes(args.res_file)
    print('Testing: {}'.format(args.res_file), flush=True)

    test_body(coco, coco_dt)
    test_foot(coco, coco_dt)
    test_face(coco, coco_dt)
    test_lefthand(coco, coco_dt)
    test_righthand(coco, coco_dt)
    test_wholebody(coco, coco_dt)

if  __name__ == '__main__':
   main()
