using System;

namespace cflatHasher
{
    public class Trailblazer
    {
        public String Hasher(long blur)
        {

        	var alphabet = "abcdefghijklmnopqrstuvwxyz0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ";
        	long baseLen = (long)(int) alphabet.Length;
        	System.Text.StringBuilder hashBuilder = new System.Text.StringBuilder("");

        	while (blur > 0)
            {
                var x = blur % baseLen;
                _ = hashBuilder.Append(alphabet[(int)x]);
                blur = blur / baseLen;
            }

            return hashBuilder.ToString();
        }
    }
} 