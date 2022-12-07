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
        public static int GetQueueLen(Queue<Bucket> q1)
        {
            Queue<Bucket> q2 = new Queue<Bucket>();
            int sum = 0;
            while (!q1.IsEmpty())
            {
                Bucket cur = q1.Remove(); q2.Insert(cur);
                sum++;
            }
            while (!q2.IsEmpty())
            {
                q1.Insert(q2.Remove());
            }
            return sum;
        }

        public static void printBucketQueue(Queue<Bucket> q1)
        {
            Queue<Bucket> q2 = new Queue<Bucket>();
            while (!q1.IsEmpty())
            {
                Bucket cur = q1.Remove(); q2.Insert(cur);
                Console.WriteLine(cur.ToString() + "\n >>");
            }
            while (!q2.IsEmpty())
            {
                q1.Insert(q2.Remove());
            }
        }
        static void Main(string[] args)
        {

            Bucket b1 = new Bucket(10);
            Bucket b2 = new Bucket(15);
            Bucket b3 = new Bucket(20);

            Queue<Bucket> q1 = new Queue<Bucket>();
            q1.Insert(b1);
            q1.Insert(b2);
            q1.Insert(b3);
            Bucket b4 = new Bucket(17);
            q1.Insert(b4);

            printBucketQueue(q1);
            Console.WriteLine("len = " + GetQueueLen(q1));

            Console.ReadLine();
        }

        public static void EmptyQueueOfBuckets(Queue<Bucket> q1)
        {
            Queue<Bucket> q2 = new Queue<Bucket>();
            while (!q1.IsEmpty())
            {
                Bucket cur = q1.Remove();
                cur.Empty();
                q2.Insert(cur);
            }
            while (!q2.IsEmpty())
            {
                q1.Insert(q2.Remove());
            }
        }

        public static Bucket GetBiggestBucketFromQueue(Queue<Bucket> q1)
        {
            Bucket b1 = q1.Head();
            Queue<Bucket> q2 = new Queue<Bucket>();
            while (!q1.IsEmpty())
            {
                Bucket cur = q1.Remove();

                if(cur.GetCapacity() > b1.GetCapacity())
                {
                    b1 = cur;
                }

                q2.Insert(cur);
            }
            while (!q2.IsEmpty())
            {
                q1.Insert(q2.Remove());
            }
            return b1; 
        }
        public static Bucket GetSmallestBucketFromQueue(Queue<Bucket> q1)
        {
            Bucket b1 = q1.Head();
            Queue<Bucket> q2 = new Queue<Bucket>();
            while (!q1.IsEmpty())
            {
                Bucket cur = q1.Remove();

                if (cur.GetCapacity() < b1.GetCapacity())
                {
                    b1 = cur;
                }

                q2.Insert(cur);
            }
            while (!q2.IsEmpty())
            {
                q1.Insert(q2.Remove());
            }
            return b1;
        }
        public static double GetAmountOfFillInBucketQueue(Queue<Bucket> q1)
        {
            Queue<Bucket> q2 = new Queue<Bucket>();
            double sum = 0;
            while (!q1.IsEmpty())
            {
                Bucket cur = q1.Remove(); q2.Insert(cur);
                sum += cur.GetCurrentAmount();
            }
            while (!q2.IsEmpty())
            {
                q1.Insert(q2.Remove());
            }
            return sum;
        }
        public static bool IsSortedBucketQueue(Queue<Bucket> q1)
        {
            Queue<Bucket> q2 = new Queue<Bucket>();
            bool sorted = true;
            int lastCap = q1.Head().GetCapacity();
            while (!q1.IsEmpty())
            {
                Bucket cur = q1.Remove(); q2.Insert(cur);
                if(lastCap > cur.GetCapacity())
                {
                    sorted = false;
                }
                lastCap = cur.GetCapacity();
            }
            while (!q2.IsEmpty())
            {
                q1.Insert(q2.Remove());
            }
            return sorted;
        }
        public static Bucket RemoveSmallest(Queue<Bucket> q1)
        {
            Queue<Bucket> q2 = new Queue<Bucket>();
            Bucket smallest = GetSmallestBucketFromQueue(q1);
            while (!q1.IsEmpty())
            {
                Bucket cur = q1.Remove(); 
                if(cur != smallest)
                {
                    q2.Insert(cur);
                }
            }
            while (!q2.IsEmpty())
            {
                q1.Insert(q2.Remove());
            }
            return smallest;
        }
        public static Bucket addFiveLiters(Queue<Bucket> q1)
        {
            Queue<Bucket> q2 = new Queue<Bucket>();
            double sum = 0;
            while (!q1.IsEmpty())
            {
                Bucket cur = q1.Remove();
                if (cur != smallest)
                {
                    q2.Insert(cur);
                }
            }
            while (!q2.IsEmpty())
            {
                q1.Insert(q2.Remove());
            }
            return smallest;
        }
    }
}
