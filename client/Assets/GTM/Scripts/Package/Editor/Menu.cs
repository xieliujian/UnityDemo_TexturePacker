using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using UnityEditor;
using System.IO;

namespace gtm.Editor
{
    public class Menu : UnityEditor.Editor
    {
        static void RunBat(string batFile, string workingDir)
        {
            var path = EditorUtil.FormatPath(workingDir);

            if (!Directory.Exists(path))
            {
                Debug.LogError(string.Format("bat文件[%s]不存在：", path));
            }
            else
            {
                EditorUtil.RunBat(batFile, "", path);
            }
        }

        [MenuItem("GTM/图集打包")]
        static void Run_TexturePacker()
        {
#if UNITY_EDITOR_OSX
        
#else
            RunBat("texturepacker.bat", Application.dataPath + "/../../tools/texturepacker/");
#endif
        }
    }
}

