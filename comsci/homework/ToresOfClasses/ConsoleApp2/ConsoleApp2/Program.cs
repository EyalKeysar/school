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
        static void Main(string[] args)
        {
            Queue<Queue<int>> q = new Queue<Queue<int>>();
            Queue<int> q1 = new Queue<int>();
            Queue<int> q2 = new Queue<int>();
            Queue<int> q3 = new Queue<int>();
            q1.Insert(1); q1.Insert(2);
            q2.Insert(3); q2.Insert(4);
            q3.Insert(4); q3.Insert(5);
            q.Insert(q1); q.Insert(q2); q.Insert(q3);
            secret(q);
            Console.ReadLine();
        }

        public static Queue<Double> secret(Queue<Queue<int>> que)
        {
            Queue<Double> qNew = new Queue<Double>(); 
            Queue<int> q;
            while (!que.IsEmpty()) { 
                q = que.Remove(); 
                int sum = 0, count = 0; 
                while (!q.IsEmpty()) {
                    Console.WriteLine("s = " + sum + "\n" + "c = " + count);
                    sum = sum + q.Remove(); count++; 
                } 
                if (count != 0) 
                    qNew.Insert((double)sum / count); 
            }
            return qNew;
        }
    }
}
