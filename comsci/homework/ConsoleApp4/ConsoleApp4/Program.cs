using System;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
//using System.Collections.Generic;
using Unit4.CollectionsLib;

namespace ConsoleApp4
{
    class Program
    {
        static void Main(string[] args)
        {

        }
        public bool Is100(BinNode<int> bn)
        {
            if (bn == null) return false;
            return Is100Otef(bn.GetRight(), 0 + bn.GetValue()) || Is100Otef(bn.GetLeft(), 0 + bn.GetValue());
        }

        public bool Is100Otef(BinNode<int> bn, int sum)
        {
            if(bn == null) return sum == 100;
            return Is100Otef(bn.GetRight(), sum + bn.GetValue()) || Is100Otef(bn.GetLeft(), sum + bn.GetValue());
        }

        public Queue<BinNode<int>> QueueHandried(Queue<BinNode<int>> queue) { 
        
        }
    }
}