1. 01_dcm2bmp_shoulder.ipynb
- dcm ct, dcm mr 쌍을 bmp로 만들어준 후 두 bmp 이미지를 좌우로 붙여 하나의 이미지로 생성하는 코드

2. 02_imgProc_and_trainGAN.ipynb
- histogram equalization, train 수행
- train은 region1,2,3을 따로 진행

3. 03_psnr_ssim.ipynb
- 생성된 gan 이미지 평가 및 boxplot 저장