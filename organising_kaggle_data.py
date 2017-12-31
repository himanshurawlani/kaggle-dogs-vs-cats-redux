import os
from shutil import copyfile

base='/home/ubuntu/Desktop/Anaconda/my_course_practice/kaggle_comp/'

# Splitting the training data into different classes(folders) as required by keras
os.chdir(base+'train/')
os.makedirs('dogs/',exist_ok=True)
os.makedirs('cats/',exist_ok=True)

os.chdir(base)
filename=base+'train/'
for i in os.scandir(filename):
    if i.is_file():
        if 'cat' in i.name:
            os.rename('train/'+i.name,'train/cats/'+i.name)
        elif 'dog' in i.name:
            os.rename('train/'+i.name,'train/dogs/'+i.name)

# Moving 1000 images from each class in training set to validation set
os.makedirs('valid/dogs/',exist_ok=True)
os.makedirs('valid/cats/',exist_ok=True)
filename=base+'train/cats/'
for i in os.scandir(filename):
    if len(os.listdir('valid/cats/'))>=1000:
        break
    os.rename('train/cats/'+i.name,base+'valid/cats/'+i.name)
filename=base+'train/dogs/'
for i in os.scandir(filename):
    if len(os.listdir('valid/dogs/'))>=1000:
        break
    os.rename('train/dogs/' + i.name, base+'valid/dogs/' + i.name)

# Creating sample training set from training set
# Sample training set has same directory structure as training set
os.makedirs('sample/train/dogs/',exist_ok=True)
os.makedirs('sample/train/cats/',exist_ok=True)
filename=base+'train/cats/'
for i in os.scandir(filename):
    if len(os.listdir('sample/train/cats/'))>=80:
        break
    copyfile('train/cats/'+i.name,base+'sample/train/cats/'+i.name)
filename=base+'train/dogs/'
for i in os.scandir(filename):
    if len(os.listdir('sample/train/dogs/'))>=80:
        break
    copyfile('train/dogs/' + i.name, base+'sample/train/dogs/' + i.name)

os.makedirs('sample/valid/dogs/',exist_ok=True)
os.makedirs('sample/valid/cats/',exist_ok=True)
filename=base+'valid/cats/'
for i in os.scandir(filename):
    if len(os.listdir('sample/valid/cats/'))>=20:
        break
    copyfile('valid/cats/'+i.name,base+'sample/valid/cats/'+i.name)
filename=base+'valid/dogs/'
for i in os.scandir(filename):
    if len(os.listdir('sample/valid/dogs/'))>=20:
        break
    copyfile('valid/dogs/' + i.name, base+'sample/valid/dogs/' + i.name)
