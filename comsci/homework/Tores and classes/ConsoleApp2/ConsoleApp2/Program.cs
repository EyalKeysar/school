using System;
//using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using Unit4.CollectionsLib;

namespace ConsoleApp2
{
    class Program
    {
        static void PrintQ(Queue<int> q1)
        {
            Queue<int> q2 = new Queue<int>();
            while (!q1.IsEmpty())
            {
                int curVal = q1.Remove();
                Console.Write(" >> " + curVal);
                q2.Insert(curVal);
            }
            while (!q2.IsEmpty())
            {
                q1.Insert(q2.Remove());
            }

        }
        static void Main(string[] args)
        {
            Queue<int> q1 = new Queue<int>();
            q1.Insert(2);
            q1.Insert(5);
            q1.Insert(1);
            q1.Insert(3);
            q1.Insert(4);
            q1.Insert(-3);
            PrintQ(sortQ(q1));
            Console.ReadLine();

        }
        public static int findMinQ(Queue<int> q1)
        {
            int minVal = int.MaxValue;
            Queue<int> q2 = new Queue<int>();
            while (!q1.IsEmpty())
            {
                int curVal = q1.Remove();
                if(curVal < minVal) { minVal = curVal; }
                q2.Insert(curVal);
            }
            while (!q2.IsEmpty())
            {
                q1.Insert(q2.Remove());
            }
            return minVal;
        }
        public static Queue<int> sortQ(Queue<int> q1)
        {
            Queue<int> qSorted = new Queue<int>();
            while (!q1.IsEmpty())
            {
                int curMin = findMinQ(q1);
                Queue<int> q2 = new Queue<int>();
                while (!q1.IsEmpty())
                {
                    int curVal = q1.Remove();
                    if(curVal == curMin)
                    {
                        qSorted.Insert(curVal);
                    }
                    else
                    {
                        q2.Insert(curVal);
                    }
                }
                while (!q2.IsEmpty())
                {
                    q1.Insert(q2.Remove());
                }
            }
            return qSorted;
        }
    }
}
