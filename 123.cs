using System;

namespace Namespace {
    class Bulok
    {
        static void Main(string[] args)
        {
            string s = "ANANA";
            char[] c = new char[s.Length];

            // Correct the line below - it should be 's.ToCharArray()' not just 's.'
            c = s.ToCharArray();

            int match = 0;
            int index = 0;

            for (index = 0; index < s.Length; index++)
            {
                c[s.Length - 1 - index] = s[index];
            }
            for (index = 0; index < s.Length; index++)
            {
                if (s[index] == c[index]) match++;
            }
            if (match == s.Length) // It's a palindrome
            {
                string s2 = new string(c);
                Console.WriteLine("The string is a palindrome.");
            }
            else
            {
                Console.WriteLine("The string is not a palindrome.");
            }
        }
    }
}
