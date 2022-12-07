using System;
//using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using Unit4.CollectionsLib;

namespace ConsoleApp1
{
    class Bucket
    {
        private int capacity;
        private double currentAmount;

        public Bucket(int capacity)
        {
            this.capacity = capacity;
        }
        public void Empty()
        {
            this.currentAmount = 0;
        }
        public bool IsEmpty()
        {
            return this.currentAmount == 0;
        }
        public void fill(double amountToFill)
        {
            if(this.currentAmount + amountToFill < this.capacity)
            {
                this.currentAmount += amountToFill;
            }
            else
            {
                this.currentAmount = this.capacity;
            }
        }
        public int GetCapacity()
        {
            return this.capacity;
        }
        public double GetCurrentAmount()
        {
            return this.currentAmount;
        }
        public void PourInto(Bucket bucketInto)
        {
            if(bucketInto.GetCurrentAmount() + this.GetCurrentAmount() < bucketInto.GetCapacity())
            {
                bucketInto.fill(this.GetCurrentAmount());
                this.Empty();
            }
            else
            {
                double left = bucketInto.GetCapacity() - bucketInto.GetCurrentAmount(); 
                bucketInto.fill(bucketInto.GetCapacity());
                this.currentAmount -= left;
                if(this.currentAmount < 0) { this.currentAmount = 0; }
            }
        }
        public string ToString()
        {
            return "capacity: " + this.capacity.ToString() + "\ncurrent amount: " + this.currentAmount.ToString();
        }

    }
}
