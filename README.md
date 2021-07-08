# croplands_segmentation

This project is built under the Project development division at Spartificial. https://spartificial.com

Crop lands segmentation in four categories, cultivated, non-cultivated, building, water-body.

For this task the dataset was build from scratch in these following steps:
1. Screenshots from google earth in almost 200x200 meters surface resolution.
2. Labeling and annotation of all the images using labelme annotation tool.
3. Converting all annotated json files to image masks in batch using json_to_mask_batch.py

In total we generated dataset of almost 1100 images and their masks. The dataset is not in public domain, you can contact us via our website for further info.

After that we used different models for the desired results.



