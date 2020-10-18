# CRAFT-Reimplementation
# Note：This is a reimplement from backtime92

## Reimplementation：Character Region Awareness for Text Detection Reimplementation based on Pytorch

## Character Region Awareness for Text Detection
Youngmin Baek, Bado Lee, Dongyoon Han, Sangdoo Yun, Hwalsuk Lee (Submitted on 3 Apr 2019)

The full paper is available at: https://arxiv.org/pdf/1904.01941.pdf                                                         

## Install Requirements:                                                                                                        
1、PyTroch>=0.4.1                                                                                                                       
2、torchvision>=0.2.1 			                                                    																			                             
3、opencv-python>=3.4.2                                                                                                       
4、check requiremtns.txt                                                                                                      
5、4 nvidia GPUs(we use 4 nvidia titanX)                                                                                      

## Pre-trained model:
`NOTE: There are old pre-trained models, I will upload the new results pre-trained models' link.`

Syndata+IC15:[Syndata+IC15 for baidu drive](https://pan.baidu.com/s/19lJRM6YWZXVkZ_aytsYSiQ) ||      [Syndata+IC15 for google
 drive](https://drive.google.com/file/d/1k17GuBG_omT91tJoIMSlLrorYbLXkq4z/view?usp=sharing)                                   

## Train for your own data:
- Put the training img and its ground truth in the "icdar2015" folder
- Put the testing img and its ground truth ing the "test" folder
- Change the path in basenet/vgg16_bn.py file: 
-> `(/data/CRAFT-pytorch/vgg16_bn-6c64b313.pth -> /your_path/vgg16_bn-6c64b313.pth).You can download the model here.`[baidu](https://pan.baidu.com/s/1_h5qdwYQAToDi_BB5Eg3vg)||[google](https://drive.google.com/open?id=1ZtvGpFQrbmEisB_GhmZb8UQOtvqY_-tW)

- change the path in trainic15data.py file: 
->` (1、/data/CRAFT-pytorch/SynthText -> /your_path/SynthText)`
->` (2、/data/CRAFT-pytorch/real_weights -> /your_path/real_weights)`
-> `(3、/data/CRAFT-pytorch/1-7.pth -> /your_path/your_pre-trained_model_name)`
-> `(4、/data/CRAFT-pytorch/icdar1317 -> /your_ic15data_path/)`
- Run **`python trainic15data.py`**

## We have released the latest code with new gaussian map and random crop algorithm. 
**`Note:new gaussian map method can split the inference gaussian region score map`**                                                                                                                         
`Sample:`                                                                                           
<img src="https://github.com/backtime92/CRAFT-Reimplementation/blob/master/image/test3_score.jpg" width="384" height="512" /><img src="https://github.com/backtime92/CRAFT-Reimplementation/blob/master/image/test3_affinity.jpg" width="384" height="256" />             

# Acknowledgement
Thanks for Youngmin Baek, Bado Lee, Dongyoon Han, Sangdoo Yun, Hwalsuk Lee excellent work and [code](https://github.com/clovaai/CRAFT-pytorch) for test. In this repo, we use the author repo's basenet and test code.

# License
For commercial use, please contact us.
