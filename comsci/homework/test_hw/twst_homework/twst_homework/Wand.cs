using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace twst_homework
{
    internal class Wand
    {
        string name;
        string material;

        public Wand(string name, string material)
        {
            this.name = name;
            this.material = material;
        }
        public string GetName(){return name;}
        public string GetMaterial() { return this.material; }
        public void SetName(string name) {this.name = name;}
        public void SetMaterial(string material) { this.material = material; }  
    }
}
