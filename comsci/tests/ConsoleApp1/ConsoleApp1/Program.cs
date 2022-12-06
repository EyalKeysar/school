using System;

namespace ConsoleApp1
{
    class Program
    {
        static void Main(string[] args){
            int num = 10; int[] arr = new int[10];
            string word = "word"; string[] wordArr = { "word1", "word2" };
            bool isTrue = true; bool isFalse = false;
            
            int[,] arr2D = { { 1, 2}, 
                             { 3, 4}, 
                             { 5, 6} }; int[,] arr2D2 = new int[10, 10];
            arr2D.GetLength(0); // 3 Divs/Rows
            arr2D.GetLength(1); // 2 Spans/Cols
            arr2D[2, 1] = 6;// arr2D[Row, Col]
            Console.WriteLine(arr2D[2, 1]);

        }
        public static void someFunc(int num, int[] arr)
        {

        }
    }
}
