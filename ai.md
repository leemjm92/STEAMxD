# :robot: AI Object Detection :robot:


# Table of Contents
* [Overview](#chapter1)
* [Dataset](#chapter2)
* [Labeling](#chapter3)
* [Training the custom object detection model](#chapter4)
* [Tips](#chapter5)
* [Further Learning Resources](#chapter6)

## Overview <a id="chapter1"></a>

<p align="center">
    <img src="/.github/images/ai-overview.jpg" width="90%" title='testing1' />
</p>

The diagram shows the iteration process when training a custom object detection model. Teams will be required to use two online platforms mainly [makesense.ai](https://www.makesense.ai/) for labelling of new images and [google colab notebook](custom-yolov5-object-detection.ipynb) for augmentation, training and evaluation of models. 

Supervised learning is used for the iteraction process. Please proceed to [Introduction to Machine Learning](https://developers.google.com/machine-learning/intro-to-ml) for a short overview on machine learning and explanation on supervised learning. 

Specifically for the competition sake we will not be delving deeply into the various concepts but would instead aim to enable you all to train and use your own custom object detection model with minimal knowledge. However, if you're interested in advancing your knowledge specifically within the machine learning field you can head on to the [Further Learning](#chapter7) section.

## Dataset <a id="chapter2"></a>

<!--- dataset needs to be collected after I've the figurines a good enough sample will do --->
<!--- 
- ipynb to git clone the yolov5 repo that I've edit to remove the settings for the augmentation (this is to allow students to thinking about the type of augmentations they will want to input for training
- tedious labelling will be cut down after more fine-tuning
- need to workout the model monitoring with tensorboard then include it in the ipynb
- some of the suggestion provided is that there could be X different composition of dataset that the students can choose from (however, how do you ensure that the students do not share the different compostion of dataset around (this idea should be discussed on friday) 
--->
A baseline dataset that is labelled has been included and can be found [here](/data). This baseline dataset includes a total of 90 images, 30 from each category. Teams are required to collect more images and label them accordingly for training of the custom object detection model for the competition. 

There are 2 main categories, humans and pets. Pets is broken down into 3 sub-categories; rabbits, dogs and cats. <!---Each category can then be subdivided into subcategories.---> Below are the list of objects that will be present in the terrain of the competition. 

<p align="center">
    <img src="/.github/images/adult0001.jpg" width="20%" title='testing1' />
    &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
    <img src="/.github/images/adult0002.jpg" width="20%" title='testing2' />
    &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
    <img src="/.github/images/child0001.jpg" width="20%" title='testing3' />
    &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
    <img src="/.github/images/child0002.jpg" width="20%" title='testing3' />
</p>

<p align="center">
    <hx>Humans</hx>
</p>

<p align="center">   
    <img src="/.github/images/rabbit0001.jpg" width="20%" title='placeholder' />
    &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
    <img src="/.github/images/rabbit0002.jpg" width="20%" title='placeholder' />
    &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
    <img src="/.github/images/rabbit0003.jpg" width="20%" title='placeholder' />
</p>

<p align="center">
    <font size="3">Animals (Rabbits)</font>
</p>

<p align="center">
    <img src="/.github/images/dog0001.jpg" width="20%" title='placeholder' />
    &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
    <img src="/.github/images/dog0002.jpg" width="20%" title='placeholder' />
    &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
    <img src="/.github/images/dog0003.jpg" width="20%" title='placeholder' />
</p>

<p align="center">
    <font size="5">Animals (Dogs)</font>
</p>

<p align="center">
    <img src="/.github/images/cat0001.jpg" width="20%" title='placeholder' />
    &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
    <img src="/.github/images/cat0002.jpg" width="20%" title='placeholder' />
    &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
    <img src="/.github/images/cat0003.jpg" width="20%" title='placeholder' />
</p>

<p align="center">
    <font size="5">Animals (Cats)</font>
</p>

## Labeling <a id="chapter3"></a>

Before teams can proceed to train the model labelling of the new images will be required. Below is a guided tutorial on how to label the images. Teams can obtain the labels-list.txt file [here](/data/labels-list.txt) and the labelling website [here](https://www.makesense.ai/). 

https://user-images.githubusercontent.com/65292018/188316871-39b920eb-b4fd-414b-91b9-2ad2c7e74e38.mov


## Training the custom object detection model <a id="chapter4"></a>

The Google Colab notebook with the relevant instructions can be obtained [here](custom-yolov5-object-detection.ipynb). The notebook contains step by step instructions on how to do data augmentation on your labelled custom dataset, train your custom model with your custom dataset and evaluate your custom model.

## Tips <a id="chapter5"></a>

Some tips for best training results can be found in the [original repository](https://github.com/ultralytics/yolov5/wiki/Tips-for-Best-Training-Results). 
<!---
- include some tips on how to ensure that you're labeling correctly
    Label consistency. All instances of all classes in all images must be labelled. Partial labelling will not work.
    Label accuracy. Labels must closely enclose each object. No space should exist between an object and it's bounding box. No objects should be missing a label.
- background images to reduce false positives (this might be part of their data collection so as to reduce the labeling efforts)

-->


## Further Learning Resources <a id="chapter6"></a>

https://github.com/aladdinpersson/Machine-Learning-Collection \
https://github.com/zwang4/awesome-machine-learning-in-compilers \
https://github.com/exajobs/machine-learning-collection \
https://github.com/microsoft/machine-learning-collection \
https://github.com/ZuzooVn/machine-learning-for-software-engineers \
https://github.com/eugeneyan/applied-ml \
https://github.com/ChristosChristofidis/awesome-deep-learning \
https://github.com/academic/awesome-datascience 

Books: \
https://www.deeplearningbook.org/ \
https://d2l.ai/ \
https://madewithml.com/