using System;
using System.Collections.Generic;
using System.Text;

namespace Bank
{
    class Account
    {
        string cName;
        int accountNo;
        double balance;
        public Account(string cName, int accountNo)
        {
            this.cName = cName;
            this.accountNo = accountNo;
            balance = 0;
        }
        public string GetName()
        {
            return cName;
        }
        public int GetAccountNo()
        {
            return accountNo;
        }
        public double GetBalance()
        {
            return balance;
        }

        public void SetName(string name)
        {
            cName = name;
        }
        public void SetAccountNo(int number)
        {
            accountNo = number;
        }
        public void SetBalance(double number)
        {
            balance = number;
        }
    }
}
