# **ML Model**

### Dataset

[Kaggle](https://www.kaggle.com/raghavrpotdar/fresh-and-stale-images-of-fruits-and-vegetables)

### Dataset Collection

Initially For the purpose of data collection we were taking images of fruits and vegetables on a daily basis by letting them rot for days. This approach was impractical as the dataset generated was a small dataset and had very little variety. This led to a trained model with less accuracy.

### Revised Approach

As a result of small size of dataset, we employed a revised approach for dataset collection. The approach can be described in the following steps:

1. First, instead of photos, videos of the fruits and vegetables were taken.
2. Then, each and every frame of video containing the particular fruit was extracted.
3. These extracted frames were augmented further to in various angles for increasing the variety of images.
4. For images containing stale fruits/vegetables, datasets from online source [Kaggle](https://www.kaggle.com/sriramr/fruits-fresh-and-rotten-for-classification) were used.

In the end we had over 15,000 images across 12 classes and 6 different fruits, providing considerable variety.

This approach led to increase in the accuracy of the Machine Learning Model.

# **VGG16 Model**

Transfer learning is a process in which a pre-trained model is used on another dataset to solve a similar problem. We have used transfer learning to train the VGG 16 model on our food images dataset. The VGG 16 model has 16 pre-trained layers trained on the ImageNet dataset. It can work on RGB images of size 224x224. The convolutional layers in the VGG 16 model have filters of size 3x3, with stride=1, while the max-pooling layers have filters of size 2x2 with stride=2. We have used the pre-trained layers of the VGG 16 model for feature extraction. The dataset of food images is used, along with the classes (fresh and stale). The weights of the last layer have been modified in order to train the model on this dataset.

# InceptionV3 Model

The Inception V3 model has been trained on a dataset of 1000 classes from the original ImageNet dataset, which consisted of over a million images. It uses 7x7 factorized convolution. Similar to using transfer learning on the VGG 16 model, we have implemented transfer learning to train the Inception V3 model on our dataset.

# **MobileNet Architecture**

It is a lightweight architecture that is suitable for mobile applications. It uses depth-wise separable convolutions. Each depth-wise separable convolution layer consists of a depth-wise convolution and a pointwise convolution. Counting depth-wise and pointwise convolutions as separate layers, a MobileNet has 28 layers.A standard MobileNet has 4.2 million parameters which can be further reduced by tuning the width multiplier hyperparameter appropriately. The size of the input image is 224 × 224 × 3. We used this model for prototyping the freshness classification feature.

For prototyping purposes Teachable Machine with MobileNet Architecture  was used.

[https://teachablemachine.withgoogle.com/](https://teachablemachine.withgoogle.com/)

Following Link was reffered for VGG16 and InceptionV3 models

[https://www.analyticsvidhya.com/blog/2020/08/top-4-pre-trained-models-for-image-classification-with-python-code/](https://www.analyticsvidhya.com/blog/2020/08/top-4-pre-trained-models-for-image-classification-with-python-code/)

The current deployed InceptionV3 model provides 89% value accuracy in ideal conditions.

