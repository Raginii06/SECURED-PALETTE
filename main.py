import cv2

# Clear Memory & Command Window
cv2.destroyAllWindows()

# Read Input Binary Secret Image
inImg = cv2.imread('athi.bmp')
cv2.imshow('Secret Image', inImg)
cv2.waitKey(0)
cv2.destroyAllWindows()

# Visual Cryptography
share1, share2, share12 = VisCrypt4(inImg)

# Outputs
cv2.imshow('Share 1', share1)
cv2.waitKey(0)
cv2.destroyAllWindows()

cv2.imshow('Share 2', share2)
cv2.waitKey(0)
cv2.destroyAllWindows()

cv2.imshow('Overlapping Share 1 & 2', share12)
cv2.waitKey(0)
cv2.destroyAllWindows()

cv2.imwrite('Share1.bmp', share1)
cv2.imwrite('Share2.bmp', share2)
cv2.imwrite('Overlapped.bmp', share12)

