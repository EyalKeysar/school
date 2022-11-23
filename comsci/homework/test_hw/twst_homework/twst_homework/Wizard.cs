using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace twst_homework
{
    class Wizard
    {
        string name;
        Wand wizWand;
        int level;
        public Wizard(string name, Wand wizWand, int level)
        {
            this.name = name;
            this.wizWand = wizWand;
            this.level = level;
        }
        public string GetName()
        {
            return name;
        }
        public Wand GetWand() { return wizWand; }
        public int GetLevel() { return level; }
        public void SetLevel(int level) { this.level = level; }
        public void SetName(string name) { this.name= name; }
        public void SetWand(Wand wizWand) { this.wizWand = wizWand; }


        public bool CheckWizard(string mat, int lvl)
        {
            return mat == this.wizWand.GetMaterial() && lvl <= this.level;
        }

    }
}
