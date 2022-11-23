using System;
using System.Diagnostics.SymbolStore;

namespace twst_homework // Note: actual namespace depends on the project name.
{
    internal class Program
    {
        static void Main(string[] args)
        {

        }

        static void CheckAll(Wizard[,] arr, string mat, int lvl) {
            int bestSum = 0;
            int bestIndex = -1;
            for (int i = 0; i < 4; i++)
            {
                int curSum = 0;
                for (int k = 0; k < arr.GetLength(0); k++)
                {
                    if (arr[i, k].CheckWizard(mat, lvl))
                    {
                        bestSum++;
                    }
                }
                if(curSum <= bestSum) { bestSum = curSum; bestIndex = i; }
                
            }
            if(bestIndex >= 0)
            {
                if(bestIndex == 0)
                {
                    Console.WriteLine("Ravenclaw");
                }
                else if(bestIndex == 1)
                {
                    Console.WriteLine("Hufflepuff");
                }
                else if(bestIndex == 2)
                {
                    Console.WriteLine("Gryffindor");
                }
                else if(bestIndex == 3)
                {
                    Console.WriteLine("Slytherin");
                }
                else
                {
                    Console.WriteLine("none");
                }
            }
            else { Console.WriteLine("none"); }
        }
    }
}