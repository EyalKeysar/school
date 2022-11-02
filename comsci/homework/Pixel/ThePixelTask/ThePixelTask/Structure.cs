using System;
using System.Collections.Generic;
using System.Text;
using static ThePixelTask.Pixel;

namespace ThePixelTask
{
    class Structure
    {
        Pixel[] arr;
        public Structure(int size){ arr = new Pixel[size]; }

        public bool IsBalanced()
        {
            int redCnt = 0, greenCnt = 0, blueCnt = 0;
            for (int i = 0; i < this.arr.Length; i++)
            {
                if(arr[i] != null)
                {
                    if (arr[i].IsRed()) { redCnt++; }
                    else if (arr[i].IsGreen()) { greenCnt++; }
                    else if (arr[i].IsBlue()) { blueCnt++; }
                }
            }
            return redCnt == greenCnt && greenCnt == blueCnt;
        }
        public bool IsBlackWhite()
        {
            bool hasWhite = false, hasBlack = false;
            foreach(Pixel p in this.arr)
            {
                if(p != null)
                {
                    if (p.IsBlack()) { hasBlack = true; } else if (p.IsWhite()) { hasWhite = true; } else { return false; }
                }
            }
            return hasWhite && hasBlack;
        }

        public void AddPIxel(Pixel p1)
        {
            for (int i = 0; i < this.arr.Length; i++)
            {
                if (this.arr[i] == null)
                {
                    this.arr[i] = p1;
                    return;
                }

            }
        }
    }
}
