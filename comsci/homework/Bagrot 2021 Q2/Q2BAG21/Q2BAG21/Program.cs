using System;

namespace Q2BAG21
{
    class Program
    {
        static void Main(string[] args)
        {

        }

        public void PrintExcellent(ReportCard[] repoArr)
        {
            foreach(ReportCard curRepo in repoArr)
            {
                if(curRepo != null)
                {
                    if (curRepo.IsExcellent()) { Console.WriteLine(curRepo.getStuName()); }
                }
            }
        }
    }
}
