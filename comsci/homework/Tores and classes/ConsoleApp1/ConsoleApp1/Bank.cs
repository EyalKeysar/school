using System;
//using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using Unit4.CollectionsLib;

namespace ConsoleApp1
{
    class Bank
    {
        /**
         * Q1:
         *  The name of the bank is a string, self explanatory.
         *  The transaction is a queue of integers, its the only data structure we have learned.
         */
        private string name;
        private Queue<int> transaction;
        /**
         * Set name.
         * O(1).
         * (** O(n) if we represent the name as array of char like in c ).
         */
        public Bank(string name)
        {
            this.name = name;
            this.transaction = new Queue<int>();
        }

        /**
         * Gets name of bank.
         * O(1).
         */
        public string GetName() { return this.name; }

        /**
         * Adds transaction to the transaction queue of the bank.
         * O(1).
         */
        public void AddTransaction(int num)
        {
            transaction.Insert(num);
        }

        /**
         * Return thae total amount of money in the bank.
         * O(n).
         */
        public int TotalAmount()
        {
            int sum = 0;
            Queue<int> q2 = new Queue<int>();
            while (!this.transaction.IsEmpty())
            {
                int curVal = this.transaction.Remove();
                sum += curVal;
                q2.Insert(curVal);
            }
            while (!q2.IsEmpty())
            {
                this.transaction.Insert(q2.Remove());
            }
            return sum;
        }
        
        /**
         * Return how many transation the bank committed.
         * O(n).
         */
        public int worked()
        {
            int sum = 0;
            Queue<int> q2 = new Queue<int>();
            while (!this.transaction.IsEmpty())
            {
                int curVal = this.transaction.Remove();
                sum++;
                q2.Insert(curVal);
            }
            while (!q2.IsEmpty())
            {

                this.transaction.Insert(q2.Remove());
            }
            return sum;
        }
        
        /**
         * Return the last transaction the bank has committed.
         * O(n).
         */
        public int LastTransaction()
        {
            int val = 0;
            Queue<int> q2 = new Queue<int>();
            while (!this.transaction.IsEmpty())
            {
                int curVal = this.transaction.Remove();
                q2.Insert(curVal);
            }
            while (!q2.IsEmpty())
            {
                val = q2.Remove();
                this.transaction.Insert(val);

            }
            return val;
        }

        /**
         * Return if the bank has committed more positive transaction or
         * more negative transaction.
         * O(n).
         */
        public int MoreOrLess()
        {
            int sum = 0;
            Queue<int> q2 = new Queue<int>();
            while (!this.transaction.IsEmpty())
            {
                int curVal = this.transaction.Remove();
                if(curVal > 0)
                {
                    sum++;
                }
                if(curVal < 0)
                {
                    sum = sum - 1;
                }
                q2.Insert(curVal);
            }
            while (!q2.IsEmpty())
            {
                this.transaction.Insert(q2.Remove());
            }
            if(sum > 0) { return 1; }
            else if(sum == 0) { return 0; }
            else { return -1; }
        }

        /**
         * Prints bank transaction history.
         * O(n).
         */
        public void History()
        {
            Console.WriteLine("Bank Name:" + this.GetName());
            int val = 0;
            Queue<int> q2 = new Queue<int>();
            while (!this.transaction.IsEmpty())
            {
                val++;
                int curVal = this.transaction.Remove();
                Console.WriteLine("transaction num" + val + ":" + curVal);
                q2.Insert(curVal);
            }
            while (!q2.IsEmpty())
            {
                this.transaction.Insert(q2.Remove());
            }
        }
    }
}
