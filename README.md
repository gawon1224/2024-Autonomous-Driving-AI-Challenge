# 2024 Autonomous Driving AI Challenge | 2D Semantic Segmentation
2024년 7월 26일 ~ 2024년 8월 19일

[![KRoad AI competition](/pngs/banner.jpg)](https://challenge.gcontest.co.kr/template/m/16335)


## Content
1. [Data Preprocessing](#Data-Preprocessing)
2. [Model Selection](#Model-Selection)
3. [Result](#Result)

## Data Preprocessing
https://github.com/gawon1224/2024-Autonomous-Driving-AI-Challenge/tree/main/Data-Preprocessing
## Model Selection
### UperNet+InternImage
Pretrained with Cityscapes(fine)
|Backbone|Batchsize|Iter|mIoU(val)|mIoU(test)|Inference time(test)|# params|
|-----|-----|-----|---|---|---|---|
|B(Base)-load_from 사용|12|320k|82.25|**<span style="color:red">84.78</span>**|221s|128M|
|T(Tiny)|8|160k|76.06|76.29|100s|59M|
|S(Small)|8|80k|77.01|77.08|113s|80M|
|B(Base)|8|80k|79.17|80.68|125s|128M|
|B(Base)|12|80k|79.15|81.66|151s|128M|
### UperNet+InternImage(Pretrained with additional data)
Pretrained with Mapillary 80k + Cityscapes(coarse) 160k
|Backbone|Batchsize|Iter|mIoU(val)|mIoU(test)|Inference time(test)|# params|Train speed|
|-----|-----|-----|---|---|---|---|---|
|L(Large)|8|36k|73.17|74.74|149s|256M|0.78s/iter|
## Result

## Reference
* https://github.com/OpenGVLab/InternImage
* https://github.com/open-mmlab/mmsegmentation
