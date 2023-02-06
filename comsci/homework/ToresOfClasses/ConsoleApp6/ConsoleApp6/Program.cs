using System;
//using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using Unit4.CollectionsLib;

namespace ConsoleApp6
{
    class Program
    {
        static void Main(string[] args)
        {
            Node<int> n1 = new Node<int>(14);
            Node<int> n2 = new Node<int>(24);
            Node<int> n3 = new Node<int>(34);
            Node<int> n4 = new Node<int>(44);
            Node<int> n5 = new Node<int>(54);

            n1.SetNext(n2);
            n2.SetNext(n3);
            n3.SetNext(n4);
            n4.SetNext(n5);
            Print(n1);

            Node<int> n6 = new Node<int>(19);
            AddNode(n1, n6);
            Print(n1);

            Node<int> n7 = new Node<int>(23);
            AddNodeInd(n1, n7, 2);
            Print(n1);

            Node<int> n8 = new Node<int>(63);
            AddHead(n1, n8);
            Print(n1);

            Console.Read();
        }

        static void Print(Node<int> Head)
        {
            Node<int> ptr = Head;
            while(ptr != null)
            {
                Console.Write(">>" + ptr.GetValue());
                ptr = ptr.GetNext();
            }
            Console.WriteLine();
        }

        static void AddNodeInd(Node<int> head, Node<int> node, int index)
        {
            Node<int> ptr = head;
            int cur = 1;
            while(cur + 1 != index)
            {
                ptr = ptr.GetNext();
                cur++;
            }
            node.SetNext(ptr.GetNext());
            ptr.SetNext(node);
        }

        static void AddNode(Node<int> Head, Node<int> node)
        {
            Node<int> ptr = Head;
            while (ptr.GetNext() != null)
            {
                ptr = ptr.GetNext();
            }
            ptr.SetNext(node);

        }

        static void AddHead(Node<int> head, Node<int> node)
        {
            node.SetNext(head);
        }

    }
}
