# 软件著作权申请代码整理提取
## 本程序的功能
- 自动从文件或者文件夹中整理提取代码
- 删除代码中的空行
- 删除代码中的注释
- 按照要求输出成软件著作权申请所需的docx文件（60页，每页50行）

## 使用方法
```python
# 【源代码所在文件夹路径】或者【zip压缩包路径】或者【txt文件路径】
file = './files/text2vec-master.zip'  
# 输出的docx文件路径
doc_path = './files/code.docx'    
from copyright_helper import write_cleaned_code_to_doc
write_cleaned_code_to_doc(code_src=file, doc_path=doc_path)
```

## Supported annotations
- \#
- """  """
- //
- \<!--  -->
- /*  */
## Supported programming language
理论上符合上述注释分隔符的都可以添加，也可以自己修改分隔符，以便符合自己的程序语言
- python
- html
- js
- css
- java
...

## supported file format
- tar\zip\txt format;
- directory;

## TODO
- web页面
- 显示行号   
目前输出的文件没有显示行号，需要用wps或者word打开后，选择 页面>行号>连续  ，即可显示行号，保存文件即可   
- 更精确的页数   
目前输出页数可能略多于60页，需要手动删除   
- 队列任务
- 上传文件的安全性和大小验证