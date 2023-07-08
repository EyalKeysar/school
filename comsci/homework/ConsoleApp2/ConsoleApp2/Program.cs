using System;

namespace MyApp // Note: actual namespace depends on the project name.
{
    internal class Program
    {
        static void Main(string[] args)
        {
        }
        public static void PrintPyramid(int num)
        {
            /*
             * Prints a star pyramid by length num.
             */
            for(int i = 0; i < num; i++)
            {
                for(int j = 0; j < (int) (num) - i; j++)
                {
                    Console.Write(" ");
                }
                for(int j = 0; j < i + 1; j++)
                {
                    Console.Write("* ");
                }
                Console.WriteLine();
            }
        }
        public static bool AllExists(int[] arr, int num)
        {
            bool[] boolArr = new bool[num + 1];
            for (int i = 0; i < num + 1; i++)
            {
                boolArr[i] = false;
            }

            for(int i=0; i < arr.Length; i++)
            {
                if (arr[i] < num + 1 && arr[i] > 0)
                {
                    boolArr[arr[i]] = true;
                }
            }
            for (int i = 1; i < num + 1; i++)
            {
                if (boolArr[i] == false)
                {
                    return false;
                }
            }
            return true;
        }
        public static int HowManySubStrings(string mainString, string secondString)
        {
            int sum = 0;
            for(int i = 0; i < mainString.Length;i++)
            {
                if(i + secondString.Length < mainString.Length + 1)
                {

                    bool isTrue = true;
                    for (int j = 0; j < secondString.Length; j++)
                    {
                        if (mainString[i + j] != secondString[j])
                        {
                            isTrue = false;
                        }
                    }
                    if (isTrue)
                    {
                        sum++;
                    }
                }
            }
            return sum;
        }
    }
}