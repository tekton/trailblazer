using System;
using System.Collections.Generic;
using System.Linq;
using System.Threading.Tasks;

using Xunit;
using Amazon.Lambda.Core;
using Amazon.Lambda.TestUtilities;

using cflatHasher;

namespace cflatHasher.Tests
{
    public class TrailblazerTest
    {
        [Fact]
        public void TestHasherFunction()
        {
            // Invoke the lambda function and confirm the string was upper cased.
            var tb = new Trailblazer();
            var hash = tb.Hasher(1000);

            Assert.Equal("iq", hash);

            hash = tb.Hasher(10000);
            Assert.Equal("sBc", hash);
            
            hash = tb.Hasher(100000);
            Assert.Equal("Ua0", hash);
            
            hash = tb.Hasher(1000000);
            Assert.Equal("cjme", hash);
        }
    }
}
