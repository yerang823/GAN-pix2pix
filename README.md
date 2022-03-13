# Result
### Bar plot of RMSE by part
![image](https://user-images.githubusercontent.com/97432613/158047011-a57c32f4-9f72-46a9-a899-36e76cf43a0f.png)

### Original CT image / synthetic GAN image
![image](https://user-images.githubusercontent.com/97432613/158047018-a5a710f3-b987-45ef-8d73-9c1b57fae5e1.png)
![image](https://user-images.githubusercontent.com/97432613/158047022-1949f081-54ed-4c41-a7f4-08debeea488b.png)
![image](https://user-images.githubusercontent.com/97432613/158047024-b18100a2-c396-4c5c-b470-c11edd184c0f.png)
![image](https://user-images.githubusercontent.com/97432613/158047025-1e0042f1-8581-43c7-8e9c-6f5fbc37d775.png)


# Usage

```python 01_img_precess.py```
- dcm ct, dcm mr 쌍을 bmp로 만들어준 후 두 bmp 이미지를 좌우로 붙여 하나의 이미지로 생성

```python 02_train.py```
- train GAN

```python 03_eval_similarity.py```
- 생성된 gan 이미지 평가 및 boxplot 저장
