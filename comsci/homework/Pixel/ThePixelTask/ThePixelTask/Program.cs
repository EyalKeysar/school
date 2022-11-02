using System;
using static ThePixelTask.Pixel;
using static ThePixelTask.Structure;
namespace ThePixelTask
{
    class Program
    {
        static void Main(string[] args)
        {
            Pixel p1 = new Pixel(0, 0, 0);
            Console.WriteLine("black: " + p1.IsBlack() + "\nwhite" + p1.IsWhite());
            p1.SetBlue(255); p1.SetGreen(255); p1.SetRed(255);
            Console.WriteLine("black: " + p1.IsBlack() + "\nwhite" + p1.IsWhite());

            Pixel p2 = new Pixel(100, 0, 0);
            Console.WriteLine("red: " + p2.IsRed());
            p2.SetRed(0); p2.SetGreen(100);
            Console.WriteLine("green: " + p2.IsGreen());
            p2.SetGreen(0); p2.SetBlue(100);
            Console.WriteLine("blue: " + p2.IsBlue());

            Structure s1 = new Structure(10);
            Pixel ps1 = new Pixel(100, 0, 0);
            Pixel ps2 = new Pixel(0, 100, 0);
            s1.AddPIxel(ps1);
            s1.AddPIxel(ps2);
            Console.WriteLine("False: " + s1.IsBalanced() + "\n False: " + s1.IsBlackWhite());
            Pixel ps3 = new Pixel(0, 0, 100);
            s1.AddPIxel(ps3);
            Console.WriteLine("True: " + s1.IsBalanced());

            Structure s2 = new Structure(10);
            Pixel pbw1 = new Pixel(0, 0, 0);
            Pixel pbw2 = new Pixel(255, 255, 255);
            Pixel pbw3 = new Pixel(0, 0, 0);
            s2.AddPIxel(pbw1);
            s2.AddPIxel(pbw2);
            s2.AddPIxel(pbw3);

            Console.WriteLine("True : " + s2.IsBlackWhite());


        }
    }
}
