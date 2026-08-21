"""
OpenCV 基础练习
包括读图、显示、灰度化、resize、ROI 裁剪、保存
运行前：在同目录放一张名为 test.jpg 的图片
"""

import cv2
import os


def main():
    #1. 读取图片
    img_path = "test.jpg"
    if not os.path.exists(img_path):
        print(f"错误: 找不到 {img_path}")
        print("请在同目录放一张名为 test.jpg 的图片后重新运行")
        return

    img = cv2.imread(img_path)
    if img is None:
        print(f"错误: cv2.imread 读取失败，请检查 {img_path} 是否为有效图片")
        return

    print(f"图片读取成功，原始形状: {img.shape}")  # (H, W, C), BGR 格式

    #2. 转为 RGB 显示（OpenCV 默认 BGR，matplotlib 用 RGB） 
    img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    print("（已转为 RGB 格式，如需用 matplotlib 显示可用 img_rgb）")

    #3. 灰度化
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    print(f"灰度图形状: {gray.shape}")  # (H, W)

    #4. Resize
    resized = cv2.resize(gray, (224, 224), interpolation=cv2.INTER_CUBIC)
    print(f"Resize 后形状: {resized.shape}")  # (224, 224)

    #5. ROI 裁剪（取中心 112x112）
    h, w = resized.shape
    roi = resized[h//4:h//4+h//2, w//4:w//4+w//2]
    print(f"ROI 裁剪后形状: {roi.shape}")  # (112, 112)

    #6. 保存结果
    cv2.imwrite("gray_224.jpg", resized)
    cv2.imwrite("roi_112.jpg", roi)
    print("已保存 gray_224.jpg 和 roi_112.jpg")

    #7. 用 OpenCV 窗口显示（可选，按任意键关闭）
    cv2.imshow("Original (BGR)", img)
    cv2.imshow("Gray 224x224", resized)
    cv2.imshow("ROI 112x112", roi)
    print("\n按任意键关闭所有窗口...")
    cv2.waitKey(0)
    cv2.destroyAllWindows()

    print("\n03_opencv_demo.py 全部运行完成！")


if __name__ == "__main__":
    main()