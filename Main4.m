%Clear Memory & Command Window
clc;
clear all;
close all;

%Read Input Binary Secret Image
inImg = imread('athi.bmp');
figure;imshow(inImg);title('Secret Image');

%Visual Cryptography
[share1, share2, share12] = VisCrypt4(inImg);

%Outputs
figure;imshow(share1);title('Share 1');
figure;imshow(share2);title('Share 2');

figure;imshow(share12);title('Overlapping Share 1 & 2');

imwrite(share1,'Share1.bmp');
imwrite(share2,'Share2.bmp');
imwrite(share12,'Overlapped.bmp');
