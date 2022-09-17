using System;
using System.Collections.Generic;
using System.Text;

namespace EyalKeysar_2
{
    class Point
    {
        // Variables
        private int x;
        private int y;

        // Constructors
        public Point()
        {
            x = 0;
            y = 0;
        }
        public Point(int x, int y)
        {
            this.x = x;
            if (y > 0) { this.y = y; }
            else { this.y = 0; }
            
        }

        // Getters Setters and simple methodes
        public void SetX(int x)
        {
            this.x = x;
        }
        public void SetY(int y)
        {
            if (y > 0) { this.y = y; }
            else { Console.WriteLine("Y value can not be non positive number!");}
        }
        public int GetX()
        {
            return x;
        }
        public int GetY()
        {
            return y;
        }
        public double Distance()
        {
            return (Math.Sqrt(Math.Pow(x, 2) + Math.Pow(y, 2)));
        }
        public bool IsBigger(Point otherPoint)
        {
            return this.y > otherPoint.GetY();
        }

     
    }
}
