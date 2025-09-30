import os

# 计数器
exec_count = 0

script_src = os.getcwd()
os.chdir("../_posts")
base_src = os.getcwd()
filename_list = os.listdir("../_posts")

# 待处理的数据
file_src_list = []

# 寻找所有待处理的数据
for filename in filename_list:
    if filename == ".DS_Store":
        continue
    # 获取文件绝对路径
    file_src = f"{base_src}/{filename}"
    # 读取文件
    with open(file_src) as f:
        content = f.read()
        # 判定文件是否以存在lang标签
        if content.find("lang: ") == -1:
            # 记录这个文件的绝对路径
            file_src_list.append(file_src)


# 将所有待处理的文件添加lang标签
for file_src in file_src_list:
    # 读取到的文件内容
    with open(file_src) as f:
        content = f.read()
    # 将文件添加lang标签，插入在date标签之前
    content = content.replace("\ndate: ", "\nlang: zh-CN\ndate: ")
    # 重新写入文件
    with open(file_src, mode="w") as f:
        f.write(content)
        exec_count += 1
    # DEBUG
    print(f"== 添加lang标签完成 {file_src} ==")
    print(f"== 完成进度 {exec_count}/{len(file_src_list)} ==")
