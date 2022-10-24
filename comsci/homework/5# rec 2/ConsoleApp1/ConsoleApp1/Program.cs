using System;

namespace ConsoleApp1
{
    class Program
    {
        static void Main(string[] args)
        {
            int[] arr = { 0, 1, 3, 2, 0 };
            Console.WriteLine(Q1(arr));
        }


        static bool Q1(int[] arr)
        {
            return Q1_help(arr, 0);
        }
        static bool Q1_help(int[] arr, int index)
        {
            if(index >= arr.Length/2)
            {
                if(arr.Length%2 == 0)
                {
                    return arr[index] == arr[(arr.Length-1) - index];
                }
                else
                {
                    return true;
                }
            }
            return arr[index] == arr[(arr.Length-1) - index] && Q1_help(arr, index+1);
        }
    }
}
