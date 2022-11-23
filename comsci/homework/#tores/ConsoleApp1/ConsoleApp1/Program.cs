using System;
//using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using Unit4.CollectionsLib;
using Unit4.BinTreeUtilsLib;
using Unit4.BinTreeCanvasLib;

namespace ConsoleApp1
{
    class Program
    {
        public static void PrintQueue(Queue<int> q1)
        {
            Queue<int> tempQueue = new Queue<int>();
            int currentNum = 0;

            Console.Write("[");
            while (!q1.IsEmpty())
            {
                currentNum = q1.Remove();
                Console.Write(currentNum + ", ");
                tempQueue.Insert(currentNum);
            }
            Console.WriteLine("]");

            while (!tempQueue.IsEmpty())
                q1.Insert(tempQueue.Remove());
        }

        static void Main(string[] args)
        {
            //Q2
            Queue<int> q2qu = new Queue<int>();
            q2qu.Insert(3);
            q2qu.Insert(5);
            q2qu.Insert(8);
            Q1(q2qu);
            //Q3
            q2qu.Insert(9);
            Q1(q2qu);
            //Q4
            Console.WriteLine(Q4(q2qu));
            //Q5
            Q5(q2qu, 7);
            Q5(q2qu, 8);
            //Q6
            Console.WriteLine(Q6(q2qu));
            //Q7
            Console.WriteLine(Q7(q2qu));
            //Q8
            Console.WriteLine(Q8(q2qu));
            //Q9
            Console.WriteLine(Q9(q2qu));
            //Q14
            Console.WriteLine(Q14(q2qu, 2));
            Console.WriteLine(Q14(q2qu, 8));
            //Q15
            Queue<int> q15qu = new Queue<int>();
            q15qu.Insert(4); q15qu.Insert(6); q15qu.Insert(9); q15qu.Insert(12);
            Q1(q15qu);

            //Q16
            Q16(q15qu, 7);
            Q1(q15qu);

            Q1(Q21(q2qu, q15qu));

            Console.Read();
        }

        public static void Q1(Queue<int> q1)
        {
            Queue<int> q2 = new Queue<int>();
            while (!q1.IsEmpty()) {
                int curVal = q1.Remove();
                Console.Write(" <- (" + curVal + ")");
                q2.Insert(curVal);
            }
            Console.WriteLine();
            while (!q2.IsEmpty())
            {
                q1.Insert(q2.Remove());
            }
        }
        public static int Q4(Queue<int> q1)
        {
            int sum = 0;
            Queue<int> q2 = new Queue<int>();
            while (!q1.IsEmpty())
            {
                int curVal = q1.Remove();
                sum++;
                q2.Insert(curVal);
            }
            while (!q2.IsEmpty())
            {
                q1.Insert(q2.Remove());
            }
            return sum;
        }
        public static bool Q5(Queue<int> q1, int num)
        {
            bool isExist = false;
            Queue<int> q2 = new Queue<int>();
            while (!q1.IsEmpty())
            {
                int curVal = q1.Remove();
                if(curVal == num)
                {
                    isExist = true;
                }
                q2.Insert(curVal);
            }
            while (!q2.IsEmpty())
            {
                q1.Insert(q2.Remove());
            }
            Console.Write("The num " + num);
            if (isExist)
            {
                Console.Write(" is ");
            }
            else
            {
                Console.Write(" is not ");
            }
            Console.WriteLine("in queue.");
            return isExist;
        }
        public static bool Q6(Queue<int> q1)
        {
            bool inOrder = true;
            int lastNum = int.MinValue;
            Queue<int> q2 = new Queue<int>();
            while (!q1.IsEmpty())
            {
                int curVal = q1.Remove();
                if(!(curVal >= lastNum)) { inOrder = false; }
                lastNum = curVal;
                q2.Insert(curVal);
            }
            while (!q2.IsEmpty())
            {
                q1.Insert(q2.Remove());
            }
            return inOrder;
        }
        public static bool Q7(Queue<int> q1)
        {
            bool inOrder = true;
            int lastNum = int.MinValue;
            Queue<int> q2 = new Queue<int>();
            while (!q1.IsEmpty())
            {
                int curVal = q1.Remove();
                if (!(curVal <= lastNum)) { inOrder = false; }
                lastNum = curVal;
                q2.Insert(curVal);
            }
            while (!q2.IsEmpty())
            {
                q1.Insert(q2.Remove());
            }
            return inOrder;
        }
        public static int Q8(Queue<int> q1)
        {
            int sum = 0;
            Queue<int> q2 = new Queue<int>();
            while (!q1.IsEmpty())
            {
                int curVal = q1.Remove();
                sum+=curVal;
                q2.Insert(curVal);
            }
            while (!q2.IsEmpty())
            {
                q1.Insert(q2.Remove());
            }
            return sum;
        }
        public static double Q9(Queue<int> q1)
        {
            int sum = 0;
            Queue<int> q2 = new Queue<int>();
            while (!q1.IsEmpty())
            {
                int curVal = q1.Remove();
                sum += curVal;
                q2.Insert(curVal);
            }
            while (!q2.IsEmpty())
            {
                q1.Insert(q2.Remove());
            }
            return ((double) sum)/Q4(q1);
        }
        public static int Q10(Queue<int> q1)
        {
            int smallestNum = int.MaxValue;
            Queue<int> q2 = new Queue<int>();
            while (!q1.IsEmpty())
            {
                int curVal = q1.Remove();
                if (!(curVal < smallestNum)) { smallestNum = curVal; }
                q2.Insert(curVal);
            }
            while (!q2.IsEmpty())
            {
                q1.Insert(q2.Remove());
            }
            return smallestNum;
        }
        public static int Q11(Queue<int> q1)
        {
            int biggestNum = int.MinValue;
            Queue<int> q2 = new Queue<int>();
            while (!q1.IsEmpty())
            {
                int curVal = q1.Remove();
                if (!(curVal > biggestNum)) { biggestNum = curVal; }
                q2.Insert(curVal);
            }
            while (!q2.IsEmpty())
            {
                q1.Insert(q2.Remove());
            }
            return biggestNum;
        }
        public static void Q12(Queue<int> q1)
        {
            Queue<int> q2 = new Queue<int>();
            while (!q1.IsEmpty())
            {
                int curVal = q1.Remove();
                if (curVal < 10) { curVal += 5; }
                q2.Insert(curVal);
            }
            while (!q2.IsEmpty())
            {
                q1.Insert(q2.Remove());
            }
        }
        public static int Q13(Queue<int> q1)
        {
            int lastNum;
            if (!q1.IsEmpty()) {lastNum = q1.Head(); } else { return 0; }
            Queue<int> q2 = new Queue<int>();
            while (!q1.IsEmpty())
            {
                int curVal = q1.Remove();
                lastNum = curVal;
                q2.Insert(curVal);
            }
            while (!q2.IsEmpty()){
                q1.Insert(q2.Remove());
            }
            return lastNum;
        }

        public static int Q14(Queue<int> q1, int ind)
        {
            int curInd = 0;
            int res = -1;
            Queue<int> q2 = new Queue<int>();
            while (!q1.IsEmpty())
            {
                int curVal = q1.Remove();
                if (curInd == ind)
                {
                    res = curVal;
                }

                q2.Insert(curVal);
                curInd += 1;
            }
            while (!q2.IsEmpty())
            {
                q1.Insert(q2.Remove());
            }
            return res;
        }
        public static void Q16(Queue<int> q1, int num)
        {
            bool alreadyPlaced = false;
            Queue<int> q2 = new Queue<int>();
            while (!q1.IsEmpty())
            {
                int curVal = q1.Remove();
                if (curVal > num && alreadyPlaced == false)
                {
                    q2.Insert(num);
                    alreadyPlaced = true;
                }
                q2.Insert(curVal);
            }
            while (!q2.IsEmpty())
            {
                q1.Insert(q2.Remove());
            }
        }
        public static Queue<int> Q18(Queue<int> q1, Queue<int> q2)
        {
            if(Q11(q1) > Q11(q2)) { return q1; } else { return q2; }
        }
        public static int Q19(Queue<int> q1, Queue<int> q2)
        {
            return Math.Min(Q10(q1), Q10(q2));  
        }
        public static Queue<int> Q20(Queue<int> q1, Queue<int> q2)
        {
            if(Q9(q1) > Q9(q2)) { return q1; } else { return q2; }
        }
        public static Queue<int> Q21(Queue<int> q1, Queue<int> q2)
        {
            Queue<int> q3 = new Queue<int>();
            Queue<int> q4 = new Queue<int>();
            while (!q1.IsEmpty())
            {
                int curVal = q1.Remove();
                q4.Insert(curVal);
                q3.Insert(curVal);
            }
            while (!q3.IsEmpty())
            {
                q1.Insert(q3.Remove());
            }

            while (!q2.IsEmpty())
            {
                int curVal = q2.Remove();
                q4.Insert(curVal);
                q3.Insert(curVal);
            }
            while (!q3.IsEmpty())
            {
                q2.Insert(q3.Remove());
            }
            return q4;
        }


    }
}
