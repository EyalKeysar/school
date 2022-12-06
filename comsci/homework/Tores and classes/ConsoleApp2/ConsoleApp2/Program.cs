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
            q1.Insert(1);
            q1.Insert(4);
            q1.Insert(-3);
            q1.Insert(1);
            q1.Insert(1);
            q1.Insert(4);
            q1.Insert(-8);
            q1.Insert(1);
            q1.Insert(4);
            PrintQ(sortByCommoness(q1));
            Queue<int> q2 = new Queue<int>();
            q2.Insert(12);
            q2.Insert(13);
            q2.Insert(14);
            q2.Insert(4);
            q2.Insert(8);
            q2.Insert(-4);

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
        public static int findMaxQ(Queue<int> q1)
        {
            int minVal = int.MinValue;
            Queue<int> q2 = new Queue<int>();
            while (!q1.IsEmpty())
            {
                int curVal = q1.Remove();
                if (curVal > minVal) { minVal = curVal; }
                q2.Insert(curVal);
            }
            while (!q2.IsEmpty())
            {
                q1.Insert(q2.Remove());
            }
            return minVal;
        }
        public static int findLastQ(Queue<int> q1)
        {
            int curVal = 0;
            Queue<int> q2 = new Queue<int>();
            while (!q1.IsEmpty())
            {
                curVal = q1.Remove();
                q2.Insert(curVal);
            }
            while (!q2.IsEmpty())
            {
                q1.Insert(q2.Remove());
            }
            return curVal;
        }

        public static int findMinWithLimit(Queue<int> q1, int lim)
        {
            int minVal = int.MaxValue;
            Queue<int> q2 = new Queue<int>();
            while (!q1.IsEmpty())
            {
                int curVal = q1.Remove();
                if (curVal < minVal && curVal > lim) { minVal = curVal; }
                q2.Insert(curVal);
            }
            while (!q2.IsEmpty())
            {
                q1.Insert(q2.Remove());
            }
            return minVal;
        }
        public static Queue<int> SortQueue(Queue<int> q1)
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

        public static int distQueue(Queue<int> q1, int x, int y)
        {
            Queue<int> q2 = new Queue<int>();
            int sum = 0;
            bool afterXBeforeY = false;
            bool afterY = false;
            while (!q1.IsEmpty())
            {
                int curVal = q1.Remove(); q2.Insert(curVal);
                if (afterXBeforeY)
                {
                    if(curVal == y)
                    {
                        afterY = true;
                    }
                    else if(afterY == false)
                    {
                        sum++;
                    }
                }
                if(curVal == x && !afterY)
                {
                    afterXBeforeY = true;
                }
            }
            while (!q2.IsEmpty())
            {
                q1.Insert(q2.Remove());
            }
            return sum;
        }

        public static int smallestBoth(Queue<int> q1, Queue<int> q2)
        {
            Queue<int> q12 = new Queue<int>();
            Queue<int> q22 = new Queue<int>();
            int maxQ1 = findMaxQ(q1);
            int maxQ2 = findMaxQ(q2);
            int curQ1 = q1.Remove();
            int curQ2 = q2.Remove();
            bool end = false;
            int num = int.MaxValue;
            while ((!q1.IsEmpty()) && (!q2.IsEmpty()) && (!end))
            {
                if (curQ1 == curQ2)
                {
                    q12.Insert(curQ1); q22.Insert(curQ2);
                    num = curQ1;
                    end = true;
                }
                else if(curQ1 > curQ2)
                {
                    Console.WriteLine(curQ1 + " > " + curQ2);
                    q22.Insert(curQ2);
                    curQ2 = q2.Remove();
                }
                else
                {
                    Console.WriteLine(curQ1 + " < " + curQ2);
                    q12.Insert(curQ2);
                    curQ1 = q1.Remove();
                }
            }

            while (!q1.IsEmpty())
            {
                q12.Insert(q1.Remove());
            }
            while (!q12.IsEmpty())
            {
                q1.Insert(q12.Remove());
            }
            while (!q2.IsEmpty())
            {
                q22.Insert(q2.Remove());
            }
            while (!q22.IsEmpty())
            {
                q2.Insert(q22.Remove());
            }
            return num;
        }
        public static Queue<int> sortByEven(Queue<int> q1)
        {
            Queue<int> q2 = new Queue<int>();
            Queue<int> q3 = new Queue<int>();
            while (!q1.IsEmpty())
            {
                int cur = q1.Remove(); q2.Insert(cur);
                if(cur%2 == 0)
                {
                    q3.Insert(cur);
                }
            }
            while (!q2.IsEmpty())
            {
                int cur = q2.Remove(); q1.Insert(cur);
                if (cur % 2 == 1)
                {
                    q3.Insert(cur);
                }
            }
            return q3;
        }

        public static int countByNum(Queue<int> q1, int num)
        {
            Queue<int> q2 = new Queue<int>();
            int sum = 0;
            while (!q1.IsEmpty())
            {
                int cur = q1.Remove(); q2.Insert(cur);
                if(cur == num) { sum++; }
            }
            while (!q2.IsEmpty()) { q1.Insert(q2.Remove()); }
            return sum;
        }


        // O(n^2)
        public static Queue<int> sortByCommoness(Queue<int> q1)
        {
            Queue<int> q2 = new Queue<int>();
            Queue<int> q3 = new Queue<int>();
            while (!q1.IsEmpty())
            {
                int cur = q1.Remove(); q2.Insert(cur); q3.Insert(cur);
                q3.Insert(countByNum(q1, cur) + countByNum(q2, cur));
            }
            while (!q2.IsEmpty())
            {
                q1.Insert(q2.Remove());
            }
            return q3;
        }

    }
}
