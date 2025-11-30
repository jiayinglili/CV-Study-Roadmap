list1 = ["img1.jpg","img2.png","data.txt"]
list1.append("img3.jpg")
for item in list1:
    if item.endswith(".jpg"):
        print(item)

dic1 = {"img1":"1080","img2":720}
print(len(dic1))
