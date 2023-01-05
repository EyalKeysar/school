using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace ConsoleApp3
{
    class PairOfNums
    {
        private int num1;
        private int num2;

        PairOfNums(int num1, int num2)
        {
            if(isValidPair(num1, num2)
            {
                this.num1 = num1;
                this.num2 = num2;
            }
            else
            {
                Console.WriteLine($"not valid{num1}, {num2}");
            }
        }

        private bool isValidPair(int num1, int num2)
        {
            return (num1 > 0 && num2 > 0 && (getFirstDig(num1) == getLastDig(num2) || getLastDig(num1) == getFirstDig(num2)))
        }

        public void setNum1(int num1)
        {
            if(isValidPair(num1, this.num2))
            {
                this.num1 = num1;
            }
            else
            {
                Console.WriteLine($"non valid setnum1 {num1}, {this.num2}");
            }
        }
        public void setNum2(int num2)
        {
            if (isValidPair(this.num1, num2))
            {
                this.num2 = num2;
            }
            else
            {
                Console.WriteLine($"non valid setnum2 {this.num1}, {num2}");
            }
        }
        public int getNum1()
        {
            return this.num1;
        }
        public int getNum2()
        {
            return this.num2;
        }
        private int getFirstDig(int num)
        {
            return num % 10;
        }
        private int getLastDig(int num)
        {
            while(num > 9)
            {
                num /= num;
            }
            return num;
        }

    }
}
