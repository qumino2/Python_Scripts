# -*- coding: utf-8 -*-
import os

# 需求：将文件夹中中英对照的文本文件(中英之间有一个空行)里的中英文分离开来输出单独的文件（此处仅输出中文）

sourcePath = "/Users/alan/Downloads/Alan/Scott_WeChat/商业合作/扇贝合作/听力产品内容/中英分离待处理"

allItems = os.listdir(sourcePath)

for item in allItems:
    itemPath = os.path.join(sourcePath, item)
    with open(itemPath, 'r', encoding='utf-8', errors='ignore') as f:
        allLines = f.readlines()
        blankLine_Number = 0
        for line in allLines:
            if line == "\n" and blankLine_Number % 2 == 0:
                blankLine_Number = blankLine_Number + 1
            elif line == "\n" and blankLine_Number % 2 == 1:
                blankLine_Number = blankLine_Number + 1
                f2 = open(os.path.splitext(itemPath)[0] + "_翻译.txt", 'a')
                f2.write(line)
                f2.close()
            elif blankLine_Number % 2 == 1:
                f2 = open(os.path.splitext(itemPath)[0] + "_翻译.txt", 'a')
                # f2 = open(itemPath + "output.txt", 'a')
                f2.write(line)
                f2.close()
                    



            

            