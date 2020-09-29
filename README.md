# Spacial Intensity Transformations

*CSE4019 Image Processing - Fall 2020 - Digital Assignment - 18BCE0715*

## Environment and Dependencies

1. MacOS 10.15.6
2. Python 3.7.7
3. Pillow (only for input and output display)
4. argparse (for parsing commandline arguments)
5. Numpy (pixel data manipulation)

## How to Run

Set up all dependencies

```
pip install -r requirements.txt
```

Run main.py with picture path

```
python main.py --input=./img/myPicture.png
```

Select the operation/transformation by entering the correct *number*.

![sample-terminal](./img/sample-input.png)

Enter Parameters (and Constants) As Required By the selected transformation

![sample-par](./img/sample-para.png)

## Tranforamtions Functions Implemeted

1. Image Negetive
2. Log Transform
3. Power-Law Transform
4. Contrast Stretching
5. Graylevel Slicing
6. Bit Plane Splicing

All input paramenters should be entered by the user as required by the corresponding transformation

## Sample input

![scenic-walk](./img/pic.png)

## Sample output

Output for each method contains the formua followed by the output image. Here are a few processed images for the sample input image.

### 1. Image Negetive
![](./img/output-readme/image-negetive-1.png)

### 2. Log Transform with c=50
![](./img/output-readme/image-log-1.png)

### 3. Power-Law Tranform with c=1 and $\gamma$	= 3

![](./img/output-readme/gamma-1.png)

### 4. Contrast Stretching

#### with  r1=50, s1=60, r2=150, s2=180

![](./img/output-readme/contrast-stretching-1.png)

#### with r1=50, s1=1, r2=50, s2=255 (Thresholding i.e it gives Binary Image )

![](./img/output-readme/conrast-stretching-2.png)

### 5. Graylevel Slicing

#### without Background Slicing and limits = 80 to 130 and S=70 and background-clipped to 50

![](./img/output-readme/graylevel-withoutbg.png)

#### with Background Slicing and with limits = 80 to 130 and S=70

![](./img/output-readme/graylevel-slicing-withbg.png)

### 6. BitPlane Splicing (from plane 1 to 8 - LSB to MSB)

![](./img/output-readme/bl1.png)
![](./img/output-readme/bl2.png)
![](./img/output-readme/bl3.png)
![](./img/output-readme/bl4.png)
![](./img/output-readme/bl5.png)
![](./img/output-readme/bl6.png)
![](./img/output-readme/bl7.png)
![](./img/output-readme/bl8.png)