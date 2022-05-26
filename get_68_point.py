# 直接运行这个文件即可
# 修改第29行和第64行来改变输出和读取文件的名称
# 需要按照README中的人脸位置依次点击68个点
# 点击完68个点后自动退出并保存
# 如果点错或想中途退出按q
import string
import cv2

count = 68
point_set = []


def getMousePos(imgName):
    def onmouse(event, x, y, flags, param):
        cv2.imshow("img", img)
        # if event==cv2.EVENT_MOUSEMOVE:
        # print(img[y,x], " pos: ", x, " x ", y)
        # 双击左键，显示鼠标位置
        global count
        global point_set
        if event == cv2.EVENT_LBUTTONUP:
            remain_num = str(68 - count)
            strtext = "(%s,%s)" % (x, y)
            point_set.append((x, y))
            cv2.circle(img, (x, y), 2, (0, 0, 255), -1)
            cv2.putText(img, remain_num, (x + 2, y + 15),
                        cv2.FONT_HERSHEY_SIMPLEX,
                        0.3, (0, 0, 200), 1)
            count -= 1
            if count == 0:
                cv2.destroyAllWindows()
                with open("sswap/pointsjpg.txt", 'w') as f:  # 输出所有点集
                    for i in point_set:
                        f.write(str(i[0]) + ' ' + str(i[1]) + '\n')
                return

    cv2.namedWindow("img", cv2.WINDOW_NORMAL)
    img = cv2.imread(imgName)
    print(img.shape)

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


def start(file: string):
    getMousePos(file)


start('sswap/1.jpg')  # 读取图片开始获取所有点
