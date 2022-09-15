using System;
using System.Collections.Generic;
using System.Text;

namespace Bank
{
    class Bank
    {
        int bankNo;
        int branchNo;
        Account[] accounts;
        public Bank(int bankNo, int branchNo, int n)
        {
            this.bankNo = bankNo;
            this.branchNo = branchNo;
            accounts = new Account[n];
        }
        public int GetBankNo()
        {
            return bankNo;
        }
        public int GetBranchNo()
        {
            return branchNo;
        }
        public Account[] GetAccounts()
        {
            return accounts;
        }
        public void SetBankNo(int bankNo)
        {
            this.bankNo = bankNo;
        }
        public void SetBranchNo(int branchNo)
        {
            this.branchNo = branchNo;
        }
        public void SetAccounts(Account[] newAccounts)
        {
            int ind = 1;
            foreach(Account account in newAccounts)
            {
                accounts[ind].SetName(account.GetName());
                accounts[ind].SetAccountNo(account.GetAccountNo());
                accounts[ind].SetBalance(account.GetBalance());
                ind++;
            }
        }
        public double AccountsBalance()
        {
            double sum = 0;
            foreach(Account account in accounts)
            {
                sum += account.GetBalance();
            }
            return sum;
        }
        public void AddAccount(Account newAccount)
        {
            foreach (Account account in accounts)
            {
                if(account != null)
                {
                    account.SetName(newAccount.GetName());
                    account.SetAccountNo(newAccount.GetAccountNo());
                    account.SetBalance(newAccount.GetBalance());
                }
            }
        }
        public Account[] BestAccout(int n)
        {
            Account[] bestAccouts = new Account[n];
            for (int i = 0; i < n; i++)
            {
                bestAccouts[i].SetAccountNo(accounts[i].GetAccountNo());
                bestAccouts[i].SetBalance(accounts[i].GetBalance());
                bestAccouts[i].SetName(accounts[i].GetName());
            }
            for (int i = 0; i < accounts.Length - n; i++)
            {
                Account nextCheck = accounts[i];
                int min = 0;
                for (int k = 0; k < n; k++)
                {
                    if(bestAccouts[k].GetBalance() < bestAccouts[min].GetBalance())
                    {
                        bestAccounts[min] = bestAccouts[k];
                    }
                }
                if(nextCheck.GetBalance() > bestAccounts[min].GetBalance())
                {
                    bestAccouts[min] = nextCheck;
                }
            }
        }





    }
}
