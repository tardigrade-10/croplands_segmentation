# -*- coding: utf-8 -*-
import json
import cv2
import numpy as np
import os
import shutil
import argparse
 
 
def cvt_one(json_path, img_path, save_path, label_color):
    # load img and json
    data = json.load(open(json_path,encoding='gbk'))
    img = cv2.imread(img_path)
 
    # get background data
    img_h = data['imageHeight']
    img_w = data['imageWidth']
    color_bg = (0, 0, 0)
    points_bg = [(0, 0), (0, img_h), (img_w, img_h), (img_w, 0)]
    img = cv2.fillPoly(img, [np.array(points_bg)], color_bg)
    # draw roi
    for i in range(len(data['shapes'])):
        name = data['shapes'][i]['label']
        points = data['shapes'][i]['points']
        data['shapes'][i]['fill_color'] = label_color[name] 
        color =  data['shapes'][i]['fill_color']
        # data['shapes'][i]['fill_color'] = label_color[name] # Modify the fill color in the json file to the color we set
        if data['shapes'][i]['shape_type'] == 'rectangle':
            pt1, pt2 = data['shapes'][i]['points'][0], data['shapes'][i]['points'][1]
            img = cv2.rectangle(img, (int(pt1[0]), int(pt1[1])), (int(pt2[0]), int(pt2[1])), label_color[name], -1)
        
        img = cv2.fillPoly(img, [np.array(points, dtype=int)], label_color[name])
        
    cv2.imwrite(save_path, img)
 
 
if __name__ == '__main__':
    save_dir ='masks'
    if not os.path.exists(save_dir):
        os.mkdir(save_dir)
 
    annots_dir = 'annots'
    imgs_dir = 'images'
    annots_names_list = os.listdir(annots_dir)
    img_names_list = os.listdir(imgs_dir)
    label_color = {
        'cultivated':(0,0 ,255),
        'non-cultivated':(0,255, 0),
        'building':(0, 255, 255),
        'water-body':(255,0,0)
    }

    for ann, img in zip(annots_names_list, img_names_list):
        img_path = 'images/' + img
        json_path = 'annots/' + ann
        save_path = 'masks/mask'+ img
        print('Processing {}'.format(img_path))
        cvt_one(json_path, img_path, save_path, label_color)