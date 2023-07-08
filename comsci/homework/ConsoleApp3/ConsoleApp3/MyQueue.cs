using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace ConsoleApp3
{
    public class MyQueue
    {
        private int[] items;
        private int front;
        private int rear;
        private int size;

        public MyQueue(int capacity)
        {
            items = new int[capacity];
            front = 0;
            rear = -1;
            size = 0;
        }

        public void Enqueue(int item)
        {
            if (rear == items.Length - 1)
            {
                Console.WriteLine("Queue is full");
                return;
            }
            rear++;
            items[rear] = item;
            size++;
        }

        public int Dequeue()
        {
            if (size == 0)
            {
                Console.WriteLine("Queue is empty");
                return -1;
            }
            int item = items[front];
            front++;
            size--;
            return item;
        }
    }
}
