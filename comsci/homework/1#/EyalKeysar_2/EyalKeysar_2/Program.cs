using System;

namespace EyalKeysar_2
{
    class Program
    {
        static void Main(string[] args)
        {
            Point[] pointArray = CreatArrayOfPoint(10);
            Print(pointArray);
        }
        // Part B check class
        public static void Print(Point p1)
        {
            Console.WriteLine("(" + p1.GetX() + "," + p1.GetY() + ")");
        }
        public static void PartBOtherTasks()
        {
            // 2
            Point point1 = new Point(3, 4);
            Print(point1);
            // 3
            Console.WriteLine(point1.Distance());
            // 4
            point1.SetX(3);
            point1.SetY(-2); // Y value can not be non positive number!
            Print(point1); // "(3,4)"
            //5
            Point point2 = new Point(-7, 2);
            Print(point2); // (-7,2) no problem with non positive x value
            //6
            Console.WriteLine(point1.IsBigger(point2)); // true
        }

        // Part C
        public static void Swap(Point p1)
        {
            int tempX = p1.GetX();  // save x value
            if (tempX < 0) // x cannot be negative because y cannot be negative
            {
                tempX = 0;
            }
            p1.SetX(p1.GetY());
            p1.SetY(tempX);
        }
        public static void Subtract(Point p1, int num)
        {
            p1.SetX(p1.GetX() - num);
            if (p1.GetY() - num > 0)
            {
                p1.SetY(p1.GetY() - num);
            }
        }
        public static void Swap(Point p1, Point p2)
        {
            int tempVal = p1.GetX();
            p1.SetX(p2.GetX());
            p2.SetX(tempVal);

            tempVal = p1.GetY();
            p1.SetY(p2.GetY());
            p2.SetY(tempVal);
        }


        // Part D
        // ------------------------------------------------------------------------
        public static Point CreatRandomPoint()
        {
            Random rand = new Random();
            Point ans = new Point(rand.Next(-100, 100), rand.Next(0, 100));

            return ans;
        }
        public static Point[] CreatArrayOfPoint(int size)
        {
            Point[] arrPoint = new Point[size];
            for (int i = 0; i < arrPoint.Length; i++)
            {
                arrPoint[i] = CreatRandomPoint();
            }

            return arrPoint;
        }
        // --------------------------------------------------------------------

        // 1
        public static void Print(Point[] arr)
        {
            for (int i = 0; i < arr.Length; i++)
            {
                Print(arr[i]);
            }
        }

        // 2
        public static Point Highest(Point[] arr)
        {
            int highestIndex = 0;
            for (int i = 0; i < arr.Length; i++)
            {
                if (!arr[highestIndex].IsBigger(arr[i]))
                {
                    highestIndex = i;
                }
            }
            return arr[highestIndex];
        }
        public static Point FarFarAway(Point[] arr)
        {
            int farestIndex = 0;
            for (int i = 0; i < arr.Length; i++)
            {
                if (arr[farestIndex].Distance() < arr[i].Distance())
                {
                    farestIndex = i;
                }
            }
            return arr[farestIndex];
        }
        public static Point FarFarAway(Point[] arr, Point p1)
        {
            int farestIndex = 0;
            int lastLength = (int)Math.Sqrt(Math.Pow(Math.Abs(arr[0].GetX() - p1.GetX()), 2) + Math.Pow(Math.Abs(arr[0].GetY() - p1.GetY()), 2));
            for (int i = 0; i < arr.Length; i++)
            {
                int curLength = (int) Math.Sqrt(Math.Pow(Math.Abs(arr[i].GetX() - p1.GetX()), 2) + Math.Pow(Math.Abs(arr[i].GetY() - p1.GetY()), 2));
                if (curLength > lastLength)
                {
                    lastLength = curLength;
                    farestIndex = i;
                }
            }
            return arr[farestIndex];
        }

    }
}
