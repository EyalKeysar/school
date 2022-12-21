using System;
//using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using Unit4.CollectionsLib;

namespace ConsoleApp1
{
    class Program
    {
        public static void printD(Queue<double> q)
        {
            Queue<double> q2 = new Queue<double>();
            while (!q.IsEmpty())
            {
                double cur = q.Remove(); q2.Insert(cur);
                Console.Write($"| {cur} | <");
            }
            while (!q2.IsEmpty())
            {
                q.Insert(q2.Remove());
            }
        }

        static void Main(string[] args)
        {
            /*Queue<Queue<int>> qu = new Queue<Queue<int>>();
            Queue<int> q1 = new Queue<int>();
            q1.Insert(5); q1.Insert(2); q1.Insert(13); q1.Insert(54);
            Queue<int> q2 = new Queue<int>();
            Queue<int> q3 = new Queue<int>();
            q3.Insert(841); q3.Insert(27); q3.Insert(500);
            Queue<int> q4 = new Queue<int>();
            q4.Insert(12);
            Queue<int> q5 = new Queue<int>();
            q5.Insert(7); q5.Insert(2); q5.Insert(4); q5.Insert(3); q5.Insert(11);
            Queue<int> q6 = new Queue<int>();
            q6.Insert(8); q6.Insert(5);

            qu.Insert(q1); qu.Insert(q2); qu.Insert(q3); qu.Insert(q4); qu.Insert(q5); qu.Insert(q6);

            Queue<double> resQu = secret(qu);
            printD(resQu);*/

            /*Queue<int> q1 = new Queue<int>(); q1.Insert(4); q1.Insert(-7); q1.Insert(1); 
            Queue<int> q2 = new Queue<int>(); q2.Insert(5); q2.Insert(2); q2.Insert(4); q2.Insert(3);
            Console.WriteLine(secret(q1, q2));*/

            /*   Queue<int> queue7 = new Queue<int>();
               queue7.Insert(2); queue7.Insert(5); queue7.Insert(6); queue7.Insert(9); queue7.Insert(1); queue7.Insert(3);

               PrintQ(Q7(queue7, 3));*/

            /*Queue<int> q8 = new Queue<int>();
            q8.Insert(1); q8.Insert(2); q8.Insert(3); q8.Insert(4);
            PrintQ(Q8Rec(q8));*/

            /*   Queue<string> q = new Queue<string>();
               q.Insert("ab"); q.Insert("bc"); q.Insert("cd"); q.Insert("de");
               Console.WriteLine(Q9(q, 4));*/
            Q10();

            Console.Read();
        }
        /* public static Queue<double> secret(Queue<Queue<int>> que)
         {
             Queue<Double> qNew = new Queue<Double>();
             Queue<int> q;
             while (!que.IsEmpty())
             {
                 q = que.Remove();
                 int sum = 0, count = 0;
                 while (!q.IsEmpty())
                 {
                     sum = sum + q.Remove();
                     count++;
                 }
                 if (count != 0)
                     qNew.Insert((double)sum / count);
             }
             return qNew;
         }*/
      /*  public static int secret(Queue<int> q1, Queue<int> q2)
        {
            if (q1.IsEmpty() || q2.IsEmpty())
                return 0;
            if (q1.Head() > q2.Head())
                return q1.Remove() + q2.Remove() + secret(q1, q2);
            return q1.Head() + q2.Remove() + secret(q1, q2);
        }*/

        public static Queue<int> Q6(Queue<int> q1)
        {
            Queue<int> q2 = new Queue<int>();
            Queue<int> sortedQueue = new Queue<int>();
            int zeroCount = 0;
            while (!q1.IsEmpty())
            {
                int cur = q1.Remove(); q2.Insert(cur);
                if (cur < 0)
                {
                    sortedQueue.Insert(cur);
                }
                else if (cur == 0)
                {
                    zeroCount++;
                }
            }
            while(zeroCount > 0)
            {
                sortedQueue.Insert(0);
                zeroCount--;
            }
            while (!q2.IsEmpty())
            {
                int cur = q2.Remove(); q1.Insert(cur);
                if(cur > 0)
                {
                    sortedQueue.Insert(cur);
                }
            }
            return sortedQueue;
        }
        public static int intQueueLength(Queue<int> q)
        {
            int len = 0;
            Queue<int> q2 = new Queue<int>();
            while (!q.IsEmpty())
            {
                q2.Insert(q.Remove());
                len++;
            }
            while (!q2.IsEmpty())
            {
                q.Insert(q2.Remove());
            }
            return len;
        }
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
        public static Queue<int> Q7(Queue<int> q, int m)
        {
            Queue<int> q2 = new Queue<int>();
            Queue<int> midQueue = new Queue<int>();
            int startingIndex = (int) ((intQueueLength(q) - m) / 2);
            int index = 0;
            while (!q.IsEmpty())
            {
                int cur = q.Remove(); q2.Insert(cur);
                if(index >= startingIndex && index < startingIndex + m)
                {
                    midQueue.Insert(cur);
                }

                index++;
            }
            while (!q2.IsEmpty())
            {
                q.Insert(q2.Remove());
            }
            return midQueue;
        }
        public static Queue<int> Q8(Queue<int> q)
        {
            Queue<int> q2 = new Queue<int>();
            Queue<int> revQueue = new Queue<int>();
            Stack<int> s = new Stack<int>();
            while (!q.IsEmpty())
            {
                int cur = q.Remove(); q2.Insert(cur);
                s.Push(cur);
            }
            while (!q2.IsEmpty())
            {
                q.Insert(q2.Remove());
            }
            while (!s.IsEmpty())
            {
                revQueue.Insert(s.Pop());
            }
            return revQueue;
        }


        public static Queue<int> Q8Rec(Queue<int> q)
        {
            Queue<int> q2 = new Queue<int>();
            return Q8Rec_help(q, q2);
        }
        public static Queue<int> Q8Rec_help(Queue<int> q, Queue<int> q2) 
        {
            int cur = q.Remove();
            q2.Insert(cur);
            if (q.IsEmpty())
            {
                while (!q2.IsEmpty())
                {
                    q.Insert(q2.Remove());
                }
                Queue<int> qu = new Queue<int>();
                qu.Insert(cur);
                return qu;
            }
            else
            {
                Queue<int> qu = Q8Rec_help(q, q2);
                qu.Insert(cur);
                return qu;
            }
        }


        public static int lenOfStrQueue(Queue<string> q)
        {
            int len = 0;
            Queue<string> q2 = new Queue<string>();
            while (!q.IsEmpty())
            {
                q2.Insert(q.Remove());
                len++;
            }
            while (!q2.IsEmpty())
            {
                q.Insert(q2.Remove());
            }
            return len;
        }

        public static string Q9(Queue<string> q, int k)
        {
            Queue<string> qSave = new Queue<string>();
            Queue<string> q1 = new Queue<string>();
            Queue<string> q2 = new Queue<string>();
            while (!q.IsEmpty())
            {
                string cur = q.Remove(); qSave.Insert(cur); q1.Insert(cur);
            }
            while (!qSave.IsEmpty())
            {
                q.Insert(qSave.Remove());
            }
            int index = 0;
            int curQ = 1;
            while (lenOfStrQueue(q1) + lenOfStrQueue(q2) != 1)
            {
                if (curQ == 1)
                {
                    if (q1.IsEmpty())
                    {
                        curQ = 2;
                    }

                    else if (((index + 1) % k) == 0)
                    {
                        string a = q1.Remove();
                        Console.WriteLine("removed = " + a);
                        index++;
                    }
                    else
                    {
                        q2.Insert(q1.Remove());
                        index++;
                    }
                }
                else
                {
                    if (q2.IsEmpty())
                    {
                        curQ = 1;
                    }
                    else if (((index + 1) % k) == 0)
                    {
                        string a = q2.Remove();
                        Console.WriteLine("removed = " + a);
                        index++;
                    }
                    else
                    {
                        q1.Insert(q2.Remove());
                        index++;
                    }
                }

            }
            if (q1.IsEmpty())
            {
                return q2.Remove();
            }
            else
            {
                return q1.Remove();
            }
        }
        public static void Q10()
        {
            Waiting wf1 = new Waiting("Jhon", "1234567890", "053-444-3333");
            Waiting wf2 = new Waiting("Mike", "0987654321", "053-666-7777");
            Waiting wf3 = new Waiting("Arik", "1029384756", "053-999-8888");
            Waiting ws1 = new Waiting("Jane", "1122334455", "054-010-1010");
            Waiting ws2 = new Waiting("Sarit", "0099887766", "054-232-2323");
            Waiting ws3 = new Waiting("Dror", "1100229933", "054-454-4545");
            WaitingList wl = new WaitingList();
            wl.insertWaiting(wf1, "fast"); wl.insertWaiting(wf2, "fast"); wl.insertWaiting(wf3, "fast");
            wl.insertWaiting(ws1, "slow"); wl.insertWaiting(ws2, "slow"); wl.insertWaiting(ws3, "slow");
            Console.WriteLine(wl.ToString());
            wl.removeWaiting();
            Console.WriteLine(wl.ToString());
            wl.removeWaiting();
            Console.WriteLine(wl.ToString());
            wl.removeWaiting();
            Console.WriteLine(wl.ToString());
            wl.removeWaiting();
            Console.WriteLine(wl.ToString());
            wl.removeWaiting();
            Console.WriteLine(wl.ToString());
            wl.removeWaiting();
            Console.WriteLine(wl.ToString());
        }
    }
}
