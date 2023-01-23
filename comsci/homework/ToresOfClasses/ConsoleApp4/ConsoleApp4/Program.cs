using System;

namespace ConsoleApp4
{
    class Program
    {
        static void Main(string[] args)
        {

            int[,] arr = {
            {20, 23, 35},
            {40, 42, 60},
            {70, 77, 99},
            {100, 101, 110}
            };
            theFunc(arr, 2, 1);
        }
        public static void printArr(int[,] arr)
        {
            for (int i = 0; i < arr.GetLength(0); i++)
            {
                for (int j = 0; j < arr.GetLength(1); j++)
                {
                    Console.Write($"|{arr[i, j]}| ");
                }
                Console.WriteLine();
            }
        }

        public static void theFunc(int[,] arr, int i, int j)
        {
            int[,] newArr = new int[arr.GetLength(0) - i, arr.GetLength(1) - j];
            //printArr(newArr);
            func(arr, newArr, i, j, i, j);
            printArr(newArr);
        }
        public static void func(int[,] arr, int[,] resArr, int i, int j, int curI, int curJ)
        {
            resArr[curI - i, curJ - j] = arr[curI, curJ];
            if (curI == arr.GetLength(0) - 1 && curJ == arr.GetLength(1) - 1)
            {
                return;
            }
            if (curJ == arr.GetLength(1) - 1)
            {
                curI++;
                curJ = j;
                func(arr, resArr, i, j, curI, curJ);
                return;
            }
            curJ++;
            func(arr, resArr, i, j, curI, curJ);
            return;
        }
    }
}
