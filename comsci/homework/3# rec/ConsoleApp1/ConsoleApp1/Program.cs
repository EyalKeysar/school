using System;

namespace ConsoleApp1
{
    class Program
    {
        static void Main(string[] args)
        {
        }

        /*
         * This is a recursive function that calculate the sum of the numbers up to a given number.
         * 
         * Get:
         *      int: num  --> number to calculate.
         * Return:
         *      int: the sum of current number and current number - 1.
         */
        static int Q1(int num)
        {
            // Check that the number is valid.
            if(num <= 0)
            {
                return 0;
            }

            if(num == 1)
            {
                return 1;
            }
            else
            {
                return num + Q1(num - 1);
            }
        }

        /*
         * This is a recursive function that calculate the factorial of a given number.
         * 
         * Get:
         *      int: num  --> number to calculate.
         * Return:
         *      int: the multiplication of current number and current number - 1.
         */
        static int Q2(int num)
        {
            // Check that the number is valid.
            if (num <= 0)
            {
                return 0;
            }

            if (num == 1)
            {
                return 1;
            }
            else
            {
                return num * Q2(num - 1);
            }
        }

        /*
         * This is a recursive function that calculate the multiplication of all odd numbers from 1 to a given number.
         * 
         * Get:
         *      int: num  --> number to calculate.
         * Return:
         *      int: the multiplication of current number and current this function given number - 2 if its odd, and this function given number - 1 if its even.
         */
        static int Q3(int num)
        {
            // Check that the number is valid.
            if (num <= 0)
            {
                return 0;
            }

            if (num == 1)
            {
                return 1;
            }
            else
            {
                // Check if number is even or odd
                if(num%2 != 0)
                {
                    // Odd number - 2 equal odd number.
                    return num * Q3(num - 2);
                }
                else
                {
                    // Even number - 1 equal odd number. 
                    return Q3(num - 1);
                }
            }
        }
        /*
         * This is a recursive function that calculates the number of digits of given number.
         * 
         * Get:
         *      int: num --> number to calculate.
         * Return:
         *      int: if num is valid the function returns 1 + this function given num / 10. else: returns 0.
         */
        static int Q4(int num)
        {
            // Check if there is no more digits to count.
            if(num == 0)
            {
                
                return 0;
            }
            else
            {
                // Each time take 1 digit out of the number and add 1 to the sum od digits.
                return 1 + Q4(num / 10);
            }
        }
        /*
         * This is a recursive function that calculate the division of a given number by other given number, only using - and + operators.
         * 
         * Get:
         *      int: num1  --> number to divide.
         *      int: num2  --> number to divide by.
         * Return:
         *      int: if number is valid returns 1 + this function given num1-num2, num2 else returns 0.
         */
        static int Q5(int num1, int num2)
        {
            if(num1 - num2 < 0)
            {
                return 0;
            }
            else
            {
                return 1 + Q5(num1 - num2, num2);
            }
        }
        /*
         * This is a recursive function that calculate the modulo of two given numbers.
         * 
         * Get:
         *      int: num1  --> number to divide.
         *      int: num2  --> number to divide by.
         * Return:
         *      int: if num1 is negative, return num1. if num1 positive or 0 return this function given num1-num2, num2.
         */
        static int Q6(int num1, int num2)
        {
            if (num1 < 0)
            {
                return num1*(-1);
            }
            else
            {
                return Q6(num1 - num2, num2);
            }
        }

        /*
         * This recursive function returnes if a given number is a multiplication of another given number.
         * 
         * Get:
         *      int: num1  --> number to divide.
         *      int: num2  --> number to divide by.
         */
        static bool Q7(int num1, int num2) { 
            if(Q6(num1, num2) == 0)
            {
                return true;
            }
            else
            {
                return false;
            }
        }


        /*
         * 
         * 
         */
        static bool Q8(int num)
        {
            return Q8_help(2, num);
        }
        static bool Q8_help(int ind, int num)
        {
            if(ind > num - 1)
            {
                return true;
            }
            else
            {
                if(num%ind == 0)
                {
                    return false;
                }
                else
                {
                    return Q8_help(ind + 1, num);
                }
            }
        }


        /*
         * 
         * 
         */
        static bool Q9(int num)
        {
            return Q9_help(num, (num % 10) % 2 == 0);
        }
        static bool Q9_help(int num, bool isEven)
        {
            if (num == 0)
            {
                return true;
            }
            else
            {
                if(isEven == true && (num%10)%2 == 0)
                {
                    return Q9_help(num / 10, isEven);
                }
                else if(isEven == false && (num%10)%2 == 1)
                {
                    return Q9_help(num / 10, isEven);
                }
                else
                {
                    return false;
                }
            }
        }


        /*
         * 
         * 
         */
        static int Q10(int num)
        {
            return Q10_help(num, 1, true);
        }
        static int Q10_help(int num, int ind, bool boolInd)
        {
            if(ind == num + 1)
            {
                return 0;
            }
            if (boolInd)
            {
                return ind * 2 + Q10_help(num, ind + 1, !boolInd);
            }
            else
            {
                return (int)(Math.Pow(ind, 2)) + Q10_help(num, ind + 1, !boolInd);
            }
        }


        /*
         * This recursive function returnes the sum of 1-sqrt(3)+5-sqrt(7).... until the n index.
         */
        static double Q11(int num)
        {
            return Q11_help(num, 0);
        }
        static double Q11_help(int num, int index)
        {
            if(index >= num)
            {
                // If the index equal to n stop the recursion.
                return 0;
            }
            else
            {
                double curNum = 2 * index + 1;
                if(index%2 == 1)
                {
                    curNum = -1 * (Math.Sqrt(curNum));
                }
                return curNum + Q11_help(num, index + 1);
            }
        }

        static int Q12(int num1, int num2)
        {
            return Q12_help(num1, num2, num1);
        }
        static int Q12_help(int num1, int num2, int newNum1)
        {
            if(newNum1 > num2)
            {
                return 0;
            }
            else
            {
                newNum1 += num1;
                return 1 + Q12_help(num1, num2, newNum1);
            }
        }

        static int Q13(int num)
        {
            return Q13_help(num, 1, 0, 3);
        }
        static int Q13_help(int num, int lastNum, int lastLastNum, int index)
        {
            if(index == num)
            {
                return (int) (Math.Pow(lastNum, 2) + Math.Pow(lastLastNum, 2));
            }
            else
            {
                int nextNum = (int)(Math.Pow(lastNum, 2) + Math.Pow(lastLastNum, 2));
                lastLastNum = lastNum;
                lastNum = nextNum;
                return Q13_help(num, lastNum, lastLastNum, index + 1);
            }
        }

    }
}