using System;
using System.Diagnostics;
using System.IO;


namespace Run
{
    public class ScriptRunner
    {
        public static string RunFromCmd(string rCodeFilePath, string args,string root)
        {
           
            string file = rCodeFilePath;
            string result = string.Empty;
            string userName = Environment.UserName;
            string path = root + "python\\python.exe";
            try
            {

                var info = new ProcessStartInfo(@path);
                info.Arguments = rCodeFilePath + " " + args;

                info.RedirectStandardInput = false;
                info.RedirectStandardOutput = true;
                info.UseShellExecute = false;
                info.CreateNoWindow = true;

                using (var proc = new Process())
                {
                    proc.StartInfo = info;
                    proc.Start();
                    proc.WaitForExit();
                    if (proc.ExitCode == 0)
                    {
                        result = proc.StandardOutput.ReadToEnd();
                    }
                }
                return result;
            }
            catch (Exception ex)
            {
                throw new Exception("R Script failed: " + result, ex);
            }
        }
        public static void Main()
        {
            string root = Path.GetPathRoot(System.Reflection.Assembly.GetEntryAssembly().Location);
            string path2 = root + "CrazyPy\\Run\\Run\\bin\\Debug\\netcoreapp3.1\\Carlos.py";
            string args = "";
            string res = ScriptRunner.RunFromCmd(path2, args,root);


        }
    }
}
