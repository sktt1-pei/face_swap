from time import sleep

import numpy as np
import cv2
import get_point
import face_swap

# 所有有效的点
valid = [i for i in range(68)]
# 对所有点的标记 1 - 有效 0 - 无效
flg = [1 for i in range(68)]

cap = cv2.VideoCapture('sample_data/obama.mp4')

# params for ShiTomasi corner detection
feature_params = dict(maxCorners=100,
                      qualityLevel=0.3,
                      minDistance=7,
                      blockSize=7)

# Parameters for lucas kanade optical flow
lk_params = dict(winSize=(15, 15),
                 maxLevel=2,
                 criteria=(
                 cv2.TERM_CRITERIA_EPS | cv2.TERM_CRITERIA_COUNT, 10, 0.03))

# Create some random colors
color = np.random.randint(0, 255, (100, 3))

# Take first frame and find corners in it
ret, old_frame = cap.read()
old_gray = cv2.cvtColor(old_frame, cv2.COLOR_BGR2GRAY)
p0 = get_point.getMousePos(old_gray)
#p0 = cv2.goodFeaturesToTrack(old_gray, mask=None, **feature_params)
# Create a mask image for drawing purposes
mask = np.zeros_like(old_frame)

# 要换脸的那个人的脸的关键点集合 这个集合不会发生变化
txt_path1 = "sswap/pointspng.txt"
points1 = face_swap.readPoints(txt_path1)
points2 = [(int(c[0][0]),int(c[0][1])) for c in p0]
filename1 = "sswap/1.png"

while (1):
    # 对每一帧进行读取
    ret, frame = cap.read()
    #print(frame.shape)

    # cv2.imshow(out)
    frame_gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # calculate optical flow  p1 是所有的点
    p1, st, err = cv2.calcOpticalFlowPyrLK(old_gray, frame_gray, p0, None,
                                           **lk_params)




    # 得到有效的点的index集合 相对于68个点集合
    for i in range(len(st)):
        if st[i] == 1:
            pass
        else:
            flg[valid[i]] = 0
    for i in range(len(flg)):
        if(flg[i] == 0 and i in valid):
            valid.remove(i)
    print((valid))


    for i in range(len(valid)):
        points2[valid[i]] = (p1[i][0][0], p1[i][0][1])

    out = face_swap.face_swap_1(filename1, frame, points1, points2, flg)
    # Select good points 选择好的点
    try:
        good_new = p1[st == 1]
        good_old = p0[st == 1]
    except:
        pass

    # draw the tracks 画出轨迹 没啥用
    for i, (new, old) in enumerate(zip(good_new, good_old)):
        a, b = new.ravel()
        c, d = old.ravel()
        a = int(a)
        b = int(b)
        c = int(c)
        d = int(d)
        mask = cv2.line(mask, (a, b), (c, d), color[i].tolist(), 2)
        frame = cv2.circle(frame, (a, b), 5, color[i].tolist(), -1)
    img = cv2.add(frame, mask)

    cv2.imshow('frame', out)
    sleep(1/60)
    k = cv2.waitKey(30) & 0xff
    if k == 27:
        break

    # Now update the previous frame and previous points
    old_gray = frame_gray.copy()
    # n * 1 * 2 表示点
    p0 = good_new.reshape(-1, 1, 2)
    #print(p0)
cv2.destroyAllWindows()
cap.release()
