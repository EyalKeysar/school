using System;
using System.Collections.Generic;
using System.Text;

namespace ThePixelTask
{
    class Pixel
    {
        private int red, green, blue;
        public Pixel(int red, int green, int blue) { this.SetRed(red); this.SetGreen(green); this.SetBlue(blue); }

        public int GetRed() { return this.red; }
        public int GetGreen() { return this.green; }
        public int GetBlue() { return this.blue; }


        public void SetRed(int newVal) { if (newVal >= 0 && newVal <= 255) { this.red = newVal; } else { this.red = 0; } }
        public void SetGreen(int newVal) { if (newVal >= 0 && newVal <= 255) { this.green = newVal; } else { this.green = 0; } }
        public void SetBlue(int newVal) { if (newVal >= 0 && newVal <= 255) { this.blue = newVal; } else { this.blue = 0; } }

        public bool IsRed() { return this.GetRed() > 0 && this.GetGreen() == 0 && this.GetBlue() == 0; }
        public bool IsGreen() { return this.GetRed() == 0 && this.GetGreen() > 0 && this.GetBlue() == 0; }
        public bool IsBlue() { return this.GetRed() == 0 && this.GetGreen() == 0 && this.GetBlue() > 0; }

        public bool IsBlack() { return this.GetRed() == 0 && this.GetGreen() == 0 && this.GetBlue() == 0; }
        public bool IsWhite() { return this.GetRed() == 255 && this.GetGreen() == 255 && this.GetBlue() == 255; }

    }
}
