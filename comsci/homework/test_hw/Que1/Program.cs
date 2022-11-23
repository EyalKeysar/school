using System;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using Unit4.CollectionsLib;
using Unit4.BinTreeUtilsLib;
using Unit4.BinTreeCanvasLib;

namespace Que1
{
    internal class Program
    {
        static void Main(string[] args)
        {
            
        }

        static bool IsContained(Queue<int> q1, int n) 
        {
            Queue<int> q2 = new Queue<int>();
            bool[] boolArr = new bool[n +1];
            resBool(boolArr);
            while (!q1.IsEmpty())
            {
                int curVal = q1.Remove();
                if(curVal <= n && curVal >= 1)
                {
                    boolArr[curVal] = true;
                }
                q2.Insert(curVal);
            }
            while (!q2.IsEmpty())
            {
                q1.Insert(q2.Remove());
            }
            for(int i = 1; i < n+1; i++)
            {
                if (!boolArr[i])
                {
                    return false;
                }
            }
            return true;

        }
        static void resBool(bool[] arr)
        {
            for (int i = 0; i < arr.Length; i++)
            {
                arr[i] = false;
            }
        }

        public static bool IsAll(Queue<int>[] arr, int n)
        {

        }
        public static bool IsAll_help(Queue<int>[] arr, int n, int index) {
            if (index > arr.Length)
            {
                return true;
            }
            else
            {
                if (!(arr[index] == null))
                {
                    return IsContained(arr[index], n) && IsAll_help(arr, n, index + 1);
                }
                else
                {
                    return IsAll_help(arr, n, index + 1);
                }
            }
        }
    }
}
