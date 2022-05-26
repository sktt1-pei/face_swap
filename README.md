可以直接运行face_swap.py或get_68_point.py，作用分别是换脸和手动选取人脸68个特征点。
光流程序optical_flow.py还有bug，需要修改。

文件夹结构：
--------
        face_swap
        |-sample_data   //optical_flow.py需要读取的文件
        |-sswap         //face_swap.py和get_68_point.py需要读取的文件
            |-1.jpg & 1.png //两个需要换脸的源文件
            |-pointsjpg.txt & pointspng.jpg //两张图片的68个点的信息
            |-..
        |-get_68_point.py //获取68个点的程序，需按照下方人脸标定规则去点
        |-face_swap.py    //线性几何变换换脸
        |-optical_flow.py //(有bug)光流，在读取一个视频后可以输出光流信息

[光流源代码](https://opencv24-python-tutorials.readthedocs.io/en/latest/py_tutorials/py_video/py_lucas_kanade/py_lucas_kanade.html)

[人脸几何变换github](https://github.com/Largefreedom/Opencv_pra/tree/master/Face%20Swap)

[获取鼠标位置源代码](https://blog.csdn.net/weixin_45331269/article/details/122447532)


#人脸标定

![ava 图标](https://ewr1.vultrobjects.com/imgur1/000/003/484/999_2b4_f18.jpg)

// 鼻尖 30  
// 鼻根 27  
// 下巴 8  
// 左眼外角 36  
// 左眼内角 39  
// 右眼外角 45  
// 右眼内角 42  
// 嘴中心   66  
// 嘴左角   48  
// 嘴右角   54  
// 左脸最外 0  
// 右脸最外 16  