## Creating Custom Object Detection Datasets


### 1. Create custom COCO datasets from scratch

https://www.youtube.com/watch?v=jftZBfMZj8k&list=PLy-L-4xQRIuNm4tN9RIufCC6sqjuw1mAj

### 2. Convert COCO dataset into KITTI format

https://www.youtube.com/watch?v=N6D9W-ytQc4&feature=youtu.be

### 3. Convert PASCAL VOC formatted datasets into a COCO dataset

https://www.youtube.com/watch?v=NPnPn-buQRM&list=PLy-L-4xQRIuOZFQ3UMFTDp8m_7ekbNiuP


### Link to voc2coco.py

[link](https://github.com/Boltuzamaki/voc2coco/blob/master/voc2coco.py)

### Coco Json format contains

“info”, “licenses”, “images”, “annotations”, “categories” (in most cases), and “segment info” (in one case)

```
"info":
    {
        "description": "COCO 2017 Dataset",
        "url": "http://cocodataset.org",
        "version": "1.0",
        "year": 2017,
        "contributor": "COCO Consortium",
        "date_created": "2017/09/01"
    }
,

"licenses": [
    {"url": "http://creativecommons.org/licenses/by/2.0/","id": 4,"name": "Attribution License"}
],
```

Copy and paste above info into test.josn, train.json and val.json
