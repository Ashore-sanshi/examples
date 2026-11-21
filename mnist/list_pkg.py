import subprocess
result = subprocess.run(['pip','list'], capture_output=True, text=True)
print(result.stdout)
# 也可以直接保存成txt
with open("pkg_list_DL.txt","w",encoding="utf-8") as f:
    f.write(result.stdout)
print("DL环境包清单已保存 pkg_list_DL.txt")
