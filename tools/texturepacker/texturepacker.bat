

echo off & color 0A

::指定起始文件夹

set SrcDir1="../../client/Assets/Arts/ui/icon/"
set DstDir1="../../client/Assets/Package/ui/icon/"

set SrcDir2="../../client/Assets/Arts/ui/image/"
set DstDir2="../../client/Assets/Package/ui/image/"

set DstDir1_To_DstDir2="../image/"

set PYTHON_MAIN_FILE="texturepacker_export/main.py"

echo "--------------------------------------------------------------------------"

python %PYTHON_MAIN_FILE% %SrcDir1% %DstDir1%
python %PYTHON_MAIN_FILE% %SrcDir2% %DstDir2%

echo "--------------------------------------------------------------------------"

echo "svn add DstDir"
cd %DstDir1%
svn add . --no-ignore --force

cd %DstDir1_To_DstDir2%
svn add . --no-ignore --force

pause

