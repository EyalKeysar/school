using System;
using System.Collections.Generic;
using System.Text;

namespace Q2BAG21
{
    class ReportCard
    {
        private string stuName;
        private Subject[] subArray;

        public string getStuName() { return this.stuName; }
        public Subject[] getSubArray() { return this.subArray; }
        public void setStuName(string newName) { this.stuName = newName; }
        public void setSubArray(Subject[] newSubArr) { this.subArray = newSubArr; }

        public ReportCard(string name, int num)
        {this.stuName = name; this.subArray = new Subject[num];}

        public double Average()
        {
            double sum = 0;
            foreach(Subject subj in this.subArray)
            {
                if(subj != null)
                {
                    sum += subj.getGrade();
                }
            }
            return (sum / this.subArray.Length);
        }
        public bool IsExcellent()
        {
            bool oneHundred = false; bool aboveFiftyFour = true;
            foreach (Subject subj in this.subArray)
            {
                if(subj != null)
                {
                    if (subj.getGrade() <= 54) { aboveFiftyFour = false; }
                    if (subj.getGrade() == 100) { oneHundred = true; }
                }
            }
            return oneHundred && aboveFiftyFour && (this.Average() >= 85);
        }
    }
}
