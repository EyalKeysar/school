using System;
//using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using Unit4.CollectionsLib;

namespace ConsoleApp1
{
    internal class Program
    {
        static void Main(string[] args)
        {
            BinNode<int> bt = new BinNode<int>(10);
            bt.GetValue(); // -> int
            bt.SetValue(0); // -> void

            bt.HasRight(); // -> bool
            bt.HasLeft(); // -> bool


            BinNode<int> br = new BinNode<int>(10), bl = new BinNode<int>(10);
            bt.SetRight(br); // -> void
            bt.SetLeft(bl); // -> void

            bt.GetLeft(); // -> BinNode<int>
            bt.GetRight(); // -> BinNode<int>

        }
    }
}
