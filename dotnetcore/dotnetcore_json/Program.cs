using System;
using System.Net.Http;
using System.Net.Http.Headers;
using System.Threading.Tasks;

namespace dotnetcore_json
{
    class Program
    {
        static void Main(string[] args)
        {
            // Fast, best for io bound work like json requests.
            AsyncJsonClient.ProcessRepositories().Wait();

        }
    }
}
