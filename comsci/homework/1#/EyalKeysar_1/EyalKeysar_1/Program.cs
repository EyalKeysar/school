using System;
// Eyal Keysar


namespace EyalKeysar_1
{
    class Program
    {
        static void Main(string[] args)
        {
            // Run the game
            PlayMagicSquare(CreateBasicMagicSquare());
        }

        // #1
        public static int[,] CreateBasicMagicSquare()
        {
            /*
             *  This function creates 2D array that follow the given rule of "magic square".
             * 
             *  Returns 4x4 array (magic square).
             */
            int[,] newMat = new int[4, 4];
            int numberIndex = 1;  // Counter
            for (int row = 0; row < newMat.GetLength(0); row++)
            {
                for (int col = 0; col < newMat.GetLength(1); col++)
                {
                    // Each loop put current index as the cell's value and add 1 to the index.
                    newMat[col, row] = numberIndex;
                    numberIndex++;
                }
            }
            return newMat;
        }
        // #2
        public static void PlayMagicSquare(int[,] mat)
        {
            /*
             *  This function let the player play a 2D i by i magic square.
             * 
             *  Returnes nothing.
             */
            PrintMat(mat);  // Prints the matrix with all the numbers.
            int[] history = new int[4];  // History log to avoid the same number to be choosen again.
            for (int turn = 0; turn < mat.Length; turn++)
            {
                bool validInput = false;
                int col = 0;
                int row = 0;
                while (!validInput)  // This loop will take input from user until the input is valid.
                {
                    Console.WriteLine("turn@" + (turn + 1) + " num:");
                    int num = int.Parse(Console.ReadLine());
                    if (!(num > Math.Pow(mat.GetLength(0), 2) || num < 1) && !(InArr(history, num)))  // If the number is in the valid range and hasn't been already choosen.
                    {
                        row = GetRow(mat, num);
                        col = GetCol(mat, num);
                        if(mat[col, row] != 0) // If cell value is not 0 
                        {
                            validInput = true;
                            history[turn] = num; // Add number to history log.
                        }
                        else
                        {
                            Console.WriteLine("Cell is zero.");
                        }                    
                    }
                    else
                    {
                        Console.WriteLine("Input out of range or already been choosen.");
                    }
                }
                // Change all row and col of the number to zero and prints updated matrix.
                ZeroCol(mat, col, row);
                ZeroRow(mat, col, row);
                PrintMat(mat);

            }
            Console.WriteLine("sum = " + GetSum(history)); // Prints magic sum.
        }
        public static bool InArr(int[] arr, int num)
        {
            /*
             *  This function cheacks if a integer value is in an integer array. 
             * 
             *   Returns true if the value is in the array and false if it is not.
             */
            for (int i = 0; i < arr.Length; i++)
            {
                if(arr[i] == num)  // The value is in the array.
                {
                    return true;
                }
            }
            return false; // If has not been returned yet value is not in the array.
        }
        public static int GetSum(int[] arr)
        {
            /*
             *  This function calculates sum of values in an integer array. 
             * 
             *  Returns sum of all values
             */
            int sum = 0;
            for (int i = 0; i < arr.Length; i++)
            {
                sum += arr[i];
            }
            return sum;
        }
        public static int GetCol(int[,] mat, int num)
        {
            /*
             *  This function calculate what is the column of given value as in magic square 
             * 
             *  Returns the colmn of the number
             */
            return (num-1) % mat.GetLength(0);
        }
        public static int GetRow(int[,] mat, int num)
        {
            /*
             *  This function calculate what is the row of given value as in magic square 
             * 
             *  Returns the row of the number
             */
            return (num-1) / mat.GetLength(0);
        }
        public static void ZeroCol(int[,] mat, int col, int row)
        {
            /*
             *  This function set all cells in 2D matrix in given column to zero. 
             */
            for (int i = 0; i < mat.GetLength(0); i++)
            {
                if (i != row)
                {
                    mat[col, i] = 0;
                }
            }
        }
        public static void ZeroRow(int[,] mat, int col, int row)
        {
            /*
             *  This function set all cells in 2D matrix in given row to zero. 
             */
            for (int i = 0; i < mat.GetLength(0); i++)
            {
                if (i != col)
                {
                    mat[i, row] = 0;
                }
            }
        }


        public static void PrintMat(int[,] mat)
        {
            /*
             *  This function prints the matrix cells to the user.
             */
            for (int row = 0; row < mat.GetLength(0); row++)
            {
                for (int col = 0; col < mat.GetLength(1); col++)
                {
                    Console.Write(mat[col, row] + " ");
                }
                Console.WriteLine(); // End line
            }
            return;
        }
    }
}
