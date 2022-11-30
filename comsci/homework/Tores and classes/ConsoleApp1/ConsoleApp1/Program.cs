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
        static void Main(string[] args)
        {
            Bank b1 = new Bank("BankOne");

            b1.AddTransaction(101);
            b1.AddTransaction(-19);
            b1.AddTransaction(-100);
            b1.AddTransaction(20);
            b1.AddTransaction(20);

            Console.WriteLine("cur amount = " + b1.TotalAmount());
            Console.WriteLine("cur num of transaction: " + b1.worked());
            Console.WriteLine("last transaction : " + b1.LastTransaction());


            Bank b2 = new Bank("BankSecond");
            b2.AddTransaction(53);
            b2.AddTransaction(-341);
            b2.AddTransaction(-12);
            b2.AddTransaction(2231);

            if (b1.TotalAmount() > b2.TotalAmount()) { Console.WriteLine(b1.GetName()); }
            else { Console.WriteLine(b2.GetName()); }

            if (b1.worked() > b2.worked()) { Console.WriteLine(b1.GetName()); }
            else { Console.WriteLine(b2.GetName()); }

            if (b1.GetName().Length > b2.GetName().Length) { Console.WriteLine(b1.GetName()); }
            else { Console.WriteLine(b2.GetName()); }

            Bank b3 = new Bank("BankThree");
            b3.AddTransaction(5312);
            b3.AddTransaction(-3421);
            b3.AddTransaction(123);

            Bank[] bArr = new Bank[5];
            bArr[0] = b1;
            bArr[1] = b2;
            bArr[2] = b3;
            // 2 pointers to each bank, one when I created it and one from thae array.
            bArr[3] = new Bank("BankFour");
            // 1 pointer because the bank created in the array pointer. when we created array of bankes it allocated space in heap for the banks,

            string longestName = "";
            int longestNameInd = -1;
            int richestSum = int.MinValue; int richestInd = -1;
            for (int i = 0; i < bArr.Length; i++)
            {
                if(bArr[i] != null)
                {
                    if (bArr[i].GetName().Length > longestName.Length)
                    {
                        longestName = bArr[i].GetName();
                        longestNameInd = i;
                    }
                    if (bArr[i].TotalAmount() > richestSum)
                    {
                        richestInd = i;
                        richestSum = bArr[i].TotalAmount();
                    }
                    if (bArr[i].MoreOrLess() == 1)
                    {
                        Console.WriteLine("more positive transaction: " + bArr[i].GetName());
                    }
                }
 
            }
            if(longestNameInd >= 0)
            {
                Console.WriteLine("longest name: " + bArr[longestNameInd].GetName());
            }
            if(richestInd >= 0)
            {
                Console.WriteLine("richest name " + bArr[richestInd].GetName());
            }
            Console.ReadLine();
        }
    }
}
