using System;
//using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using Unit4.CollectionsLib;

namespace ConsoleApp1
{
    class Waiting
    {
        private string name;
        private string id;
        private string phone;
        public Waiting(string name, string id, string phone)
        {
            this.name = name;
            this.id = id;
            this.phone = phone;
        }
        public string GetPhone() { return this.phone; }
        public string GetId() { return this.id; }
        public string GetName() { return this.name; }
        override public string ToString()
        {
            return $" | name = {this.name} - id = {this.id} - phone = {this.phone} |";
        }
    }
}
