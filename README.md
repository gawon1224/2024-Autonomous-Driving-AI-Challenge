# 2024 Autonomous Driving AI Challenge
## Project Overview
Task : 2D Semantic Segmentation on Road Scene Dataset

Project Period : 2024년 7월 26일 ~ 2024년 8월 19일

Project Wrap Up Report :

[![KRoad AI competition](/pngs/banner.jpg)](https://challenge.gcontest.co.kr/template/m/16335)

## Content
1. [Data Preprocessing](#Data-Preprocessing)
2. [Model Selection](#Model-Selection)
3. [Result](#Result)

**Challenges**

- 객체 간 우선순위를 고려하여 road scene에서의 2D semantic segmentation 진행

**Solution**

- Image 전처리 단계에서 우선순위 고려
- Data Augmentation을 통한 Class Imbalance 문제 해소
- 유사한 dataset의 SOTA 모델 활용


## Dataset
- Train dataset: 12,000장
- Validation dataset: 1,500장
- Test dataset: 1,500장
- image size = (1920,1200)
- 총 24개 class

## Data Preprocessing
https://github.com/gawon1224/2024-Autonomous-Driving-AI-Challenge/tree/main/Data-Preprocessing
## Model Selection
![image](https://github.com/user-attachments/assets/8aea3393-913c-416f-8035-bd84040c9f4f)
src: 


## Result
### UperNet + InternImage
Pretrained with Cityscapes(fine)
|Backbone|Batchsize|Iter|mIoU(val)|mIoU(test)|Inference time(test)|# params|
|-----|-----|-----|---|---|---|---|
|T(Tiny)|8|160k|76.06|76.29|100s|59M|
|S(Small)|8|80k|77.01|77.08|113s|80M|
|B(Base)|8|80k|79.17|80.68|125s|128M|
|B(Base)|12|80k|79.15|81.66|151s|128M|
|**B(Base)-use load_from**|**12**|**320k**|**82.25**|**<span style="color:red">84.78</span>**|**221s**|**128M**|
### UperNet + InternImage(Pretrained with additional data)
Pretrained with Mapillary 80k + Cityscapes(coarse) 160k
|Backbone|Batchsize|Iter|mIoU(val)|mIoU(test)|Inference time(test)|# params|
|-----|-----|-----|---|---|---|---|
|L(Large)|8|36k|73.17|74.74|149s|256M|
### UperNet + InternImage with Augmented data
Pretrained with Cityscapes(fine)

We augmented motorcycle and personal mobility classes by cropping images to 960x600 and resize images to 1920x1200.
|Backbone|Batchsize|Iter|mIoU(val)|mIoU(test)|Inference time(test)|# params|
|-----|-----|-----|---|---|---|---|
|S(Small)|8|36k|80.78|80.09|113s|80M|
|B(Base)|12|160k|79.78|80.19|122s|128M|

## Reference
* https://github.com/OpenGVLab/InternImage
* https://github.com/open-mmlab/mmsegmentation
