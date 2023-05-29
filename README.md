# 使用TexturePacker打包UI图集

## TexturePacker注册

选择`TexturePacker.exe`，点击`agree`

## 安装python

安装python3，注册环境变量， python如果无法执行，重启下电脑就生效

## 导入插件

![github](https://github.com/xieliujian/UnityDemo_TexturePacker/blob/main/video/1.png?raw=true)

把图片格式从`Default`修改为`Sprite (2D and UI)`

![github](https://github.com/xieliujian/UnityDemo_TexturePacker/blob/main/video/2.png?raw=true)

## python导出工具

```python

# 执行导出语句
def exeCommand(srcfulldir, subdirnoext, dstdir):
    dstfulldir = dstdir + subdirnoext

    srcabspath = os.path.abspath(srcfulldir)
    dstabspath = os.path.abspath(dstfulldir)

    exeabspath = "/win/TexturePacker.exe "
    exeabspath = os.getcwd() + exeabspath

    cmd = exeabspath
    cmd += srcabspath + " --multipack "
    cmd += "--sheet " + dstabspath + "{n}.png "
    cmd += "--data " + dstabspath + "{n}.tpsheet "
    cmd += "--format unity-texture2d "
    cmd += "--max-size " + str(TP_MAX_SIZE) + " "
    cmd += "--size-constraints POT "
    cmd += "--trim-mode None"

    print(cmd)

    os.system(cmd)

```

