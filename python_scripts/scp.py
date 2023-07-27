import time
import cv2
import pyautogui
import numpy as np

def find_image_on_screen(template_path, confidence=0.8):
    screenshot = pyautogui.screenshot()
    screenshot = cv2.cvtColor(np.array(screenshot), cv2.COLOR_RGB2GRAY)
    
    template = cv2.imread(template_path, cv2.IMREAD_GRAYSCALE)
    w, h = template.shape[::-1]
    res = cv2.matchTemplate(screenshot, template, cv2.TM_CCOEFF_NORMED)
    min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(res)
    top_left = max_loc
    bottom_right = (top_left[0] + w, top_left[1] + h)
    location=top_left,bottom_right
    if max_val >= confidence:
        print(max_val)
        return location
    return None

def find_image_on_window(template_path, sub_path,confidence=0.8):    
    template = cv2.imread(template_path, cv2.IMREAD_GRAYSCALE)
    sub_template=cv2.imread(sub_path,cv2.IMREAD_GRAYSCALE)

    w, h = sub_template.shape[::-1]
    res = cv2.matchTemplate(template, sub_template, cv2.TM_CCOEFF_NORMED)
    min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(res)
    top_left = max_loc
    bottom_right = (top_left[0] + w, top_left[1] + h)
    location=top_left,bottom_right
    if max_val >= confidence:
        print(max_val)
        return location
    return None

def click_on_image2(template_path2, confidence=0.95, interval=1):
    while True:
        location = find_image_on_screen(template_path2, confidence)
        if location is not None:
            tr, br = location
            x=(tr[0]+br[0])/2
            y=(tr[1]+br[1])/2
            pyautogui.click(x, y)
            print("click",x,y)
            time.sleep(interval)
            break

def click_on_image3(template_path1,sub_path3, confidence=0.95, interval=1):
    while True:
        location1 = find_image_on_screen(template_path1, confidence)
        print("location1",location1)
        if location1 is not None:
            tl1, br1 = location1
            location3 = find_image_on_window(template_path1,sub_path3)
            print("location3",location3)
            if location3 is not None:
                _tl,_br=location3
                tl3 = (tl1[0] + _tl[0], tl1[1] + _tl[1])
                br3 = (tl1[0] + _br[0], tl1[1] + _br[1])
                print("tl3,br3",tl3,br3)
                x=(tl3[0]+br3[0])/2
                y=(tl3[1]+br3[1])/2
                pyautogui.click(x, y)
                print("click",x,y)
                time.sleep(interval)
                break
            else :continue
        else: continue

if __name__ == "__main__":
    # 在这里指定您要查找并点击的图像的路径
    image_template_path1 = "1.png"
    sub_path3 = "3.png"
    image_template_path4 = "4.png"
    image_template_path5 = "5.png"
    image_template_path6 = "6.png"
    n = 3
    for i in range(n):
        # 开始自动点击
        click_on_image3(image_template_path1,sub_path3)
        print("click success",sub_path3)
        click_on_image2(image_template_path4)
        print("click success",image_template_path4)
        click_on_image2(image_template_path5)
        print("click success",image_template_path5)
        click_on_image2(image_template_path6)
        print("click success",image_template_path6)
