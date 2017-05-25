# OpenCV特征匹配

引用自[博客](http://www.jianshu.com/p/1f6195352b26)

## 特征获取（Feature extraction）

很多的低级特征，例如边，角，团，脊会比一个像素的灰度值所带有的信息多的多。在不同的应用，一些特征会比其它特征更加的有用。一旦想好我们想要的特征的构成，我们就要想办法在图片里找到我们想要的特征。

## 特征检测（Feature detection）

在图片里找到我们感兴趣的区域的过程就叫做特征检测。OpenCV中提供了多个特征检测算法：

Harris corner detection: 角点时在所有方向像素变化剧烈的点，Harris和Stephens提出了检测这样区域的快速的方法。opencv:cv2.cornerHarris
Shi-Tomasi corner detection:通常比Harris方法更优，他们查找N个最强的角点。opencv:cv2.goodFeaturesToTrack
Scale-Invariant Feature Transform(SIFT):在图像大小改变时角点检测的效果就不好了，Lowe提出了一个描述图像里与角度大小无关的关键点的方法。在opencv3中，SIFT在contrib模块里，ubuntu环境安装opencv_contrib的方法见我写的教程。windows的话，opencv3.2中集成了contrib，可以在这里找到对应的whl文件通过pip安装即可。opencv2:cv2.SIFT，opencv3:cv2.xfeatures2d.SIFT_create()
Speeded-Up Robust Features(SURF):SIFT是一个很好的方法，但是对于大部分应用来说，它不够快。SURF将SIFT中的Laplacian of a Gaussian（LOG）用一个方框滤波（box filter）代替。opencv2:cv2.SURF，opencv3:cv2.xfeatures2d.SURF_create()
OpenCV支持很多的特征描述，包括Features fromAccelerated Segment Test (FAST), Binary Robust IndependentElementary Features (BRIEF), Oriented FAST，Rotated BRIEF(ORB)。
