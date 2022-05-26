import numpy as np
import cv2
import json
import os

count = 68
point_set = []
point_array = np.zeros((68,1,2),dtype='float32')

def getMousePos(image):
    def onmouse(event, x, y, flags, param):
        cv2.imshow("img", img)
        # if event==cv2.EVENT_MOUSEMOVE:
        # print(img[y,x], " pos: ", x, " x ", y)
        # 双击左键，显示鼠标位置
        global count
        global point_set
        if event == cv2.EVENT_LBUTTONUP:
            remain_num = str(68 - count)
            # strtext = "(%s,%s)" % (x, y)
            point_set.append((x, y))
            cv2.circle(img, (x, y), 2, (0, 0, 255), -1)
            cv2.putText(img, remain_num, (x + 2, y + 15),
                        cv2.FONT_HERSHEY_SIMPLEX,
                        0.3, (0, 0, 200), 1)
            count -= 1
            if count == 0:
                cv2.destroyAllWindows()
                with open("sample_data/trump.json", 'w') as f:  # 储存
                    json.dump(point_set,f)
                for i in range(len(point_set)):
                    point_array[i][0][0] = point_set[i][0]
                    point_array[i][0][1] = point_set[i][1]
                return point_array

    cv2.namedWindow("img", cv2.WINDOW_NORMAL)
    img = image
    print(img.shape)
    if os.path.exists('sample_data/trump.json'):
        with open('sample_data/trump.json','r') as f:
            point_set = json.load(f)
        for i in range(len(point_set)):
            point_array[i][0][0] = point_set[i][0]
            point_array[i][0][1] = point_set[i][1]
        return point_array
    cv2.setMouseCallback("img", onmouse)

    if cv2.waitKey() & 0xFF == 27:  # 按下‘q'键，退出
        cv2.destroyAllWindows()

        return


def showPixelValue(imgName):
    img = cv2.imread(imgName)

    def onmouse(event, x, y, flags, param):
        if event == cv2.EVENT_MOUSEMOVE:
            print(img[y, x])

    cv2.namedWindow("img")
    cv2.setMouseCallback("img", onmouse)
    cv2.imshow("img", img)
    if cv2.waitKey() == ord('q'):  # 按下‘q'键，退出
        cv2.destroyAllWindows()
