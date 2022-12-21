using System;
//using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using Unit4.CollectionsLib;

namespace ConsoleApp1
{
    class WaitingList
    {
        private Queue<Waiting> fastQueue;
        private Queue<Waiting> slowQueue;
        public WaitingList()
        {
            this.fastQueue = new Queue<Waiting>();
            this.slowQueue = new Queue<Waiting>();
        }
        public void insertWaiting(Waiting person, string fastOrSlow)
        {
            if (fastOrSlow.Equals("fast"))
            {
                this.fastQueue.Insert(person);
            }
            else
            {
                this.slowQueue.Insert(person);
            }
        }
        public Waiting removeWaiting()
        {
            if (!fastQueue.IsEmpty())
            {
                return this.fastQueue.Remove();
            }
            else
            {
                return this.slowQueue.Remove();
            }
        }
        public bool IsEmpty()
        {
            return this.fastQueue.IsEmpty() && this.slowQueue.IsEmpty();
        }
        private string QueueToString(Queue<Waiting> q)
        {
            string res = "";
            Queue<Waiting> q2 = new Queue<Waiting>();
            while (!q.IsEmpty())
            {
                Waiting cur = q.Remove();
                q2.Insert(cur);
                res += "> " + cur.ToString();
            }
            while (!q2.IsEmpty())
            {
                q.Insert(q2.Remove());
            }
            return res;
        }
        override public string ToString()
        {
            return $"\nfast queue: {this.fastQueue.ToString()}\nslow queue: {this.slowQueue.ToString()}\n";
        }
    }
}
