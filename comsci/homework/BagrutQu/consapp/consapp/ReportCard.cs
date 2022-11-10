using System;
using System.Collections.Generic;
using System.Text;
using static consapp.Subject;

namespace consapp
{
    class ReportCard
    {
        private string stuName;
        private Subject[] subArray;

        public string GetName() { return this.stuName; }
        public Subject[] GetSubArray() { return this.subArray; }
        public void SetName(string newname) { this.stuName = newname; }
        public void SetSubArray(Subject[] newSub) { this.subArray = newSub; }

    }
}
