#### 새로 생성
# from mmseg.registry import DATASETS
# from .basesegdataset import BaseSegDataset
from mmseg.datasets.builder import DATASETS
from mmseg.datasets.custom import CustomDataset

@DATASETS.register_module()
class KroadDataset(CustomDataset):
        
        CLASSES = ('road', 'sidewalk', 'road roughness', 'road boundaries', 
                'crosswalks', 'lane', 'road color guide', 'road marking', 
                'parking', 'traffic sign', 'traffic light', 'pole/structural object',
                'building', 'tunnel', 'bridge', 'pedestrian', 'vehicle', 
                'bicycle', 'motorcycle', 'personal mobility', 'dynamic', 
                'vegetation', 'sky', 'static')
                
        PALETTE = [[120, 120, 120], [180, 120, 120], [6, 230, 230], [80, 50, 50],
                [4, 200, 3], [120, 120, 80], [140, 140, 140], [204, 5, 255],
                [230, 230, 230], [4, 250, 7], [224, 5, 255], [235, 255, 7],
                [150, 5, 61], [120, 120, 70], [8, 255, 51], [255, 6, 82],
                [143, 255, 140], [204, 255, 4], [255, 51, 7], [204, 70, 3],
                [0, 102, 200], [61, 230, 250], [255, 6, 51], [11, 102, 255]]

        def __init__(self, **kwargs):
                super(KroadDataset, self).__init__(
                img_suffix='.jpg',
                seg_map_suffix='.png',
                reduce_zero_label=False,
                **kwargs)

# @DATASETS.register_module()
# class KroadDataset(BaseSegDataset):

#     METAINFO = dict(
#         classes=('road', 'sidewalk', 'road roughness', 'road boundaries', 
#                 'crosswalks', 'lane', 'road color guide', 'road marking', 
#                 'parking', 'traffic sign', 'traffic light', 'pole/structural object',
#                 'building', 'tunnel', 'bridge', 'pedestrian', 'vehicle', 
#                 'bicycle', 'motorcycle', 'personal mobility', 'dynamic', 
#                 'vegetation', 'sky', 'static'),
#         palette=[[120, 120, 120], [180, 120, 120], [6, 230, 230], [80, 50, 50],
#                  [4, 200, 3], [120, 120, 80], [140, 140, 140], [204, 5, 255],
#                  [230, 230, 230], [4, 250, 7], [224, 5, 255], [235, 255, 7],
#                  [150, 5, 61], [120, 120, 70], [8, 255, 51], [255, 6, 82],
#                  [143, 255, 140], [204, 255, 4], [255, 51, 7], [204, 70, 3],
#                  [0, 102, 200], [61, 230, 250], [255, 6, 51], [11, 102, 255]])

#     def __init__(self,
#                  img_suffix='.jpg',
#                  seg_map_suffix='.png',
#                  **kwargs) -> None:
#         super().__init__(
#             img_suffix=img_suffix,
#             seg_map_suffix=seg_map_suffix,
#             **kwargs)