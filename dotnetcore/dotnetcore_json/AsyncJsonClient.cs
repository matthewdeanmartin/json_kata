using System;
using System.Collections.Generic;
using System.Net.Http;
using System.Net.Http.Headers;
using System.Text;
using System.Threading.Tasks;

namespace dotnetcore_json
{
    /// <summary>
    /// Starting point: https://docs.microsoft.com/en-us/dotnet/csharp/tutorials/console-webapiclient
    /// </summary>
    public class AsyncJsonClient
    {
        private static readonly HttpClient Client = new HttpClient();
        
        public static async Task ProcessRepositories()
        {
            Client.DefaultRequestHeaders.Accept.Clear();
            Client.DefaultRequestHeaders.Accept.Add(
                new MediaTypeWithQualityHeaderValue("application/vnd.github.v3+json"));
            Client.DefaultRequestHeaders.Add("User-Agent", ".NET Foundation Repository Reporter");

            var stringTask = Client.GetStringAsync("https://api.github.com/orgs/dotnet/repos");

            var msg = await stringTask;
            Console.Write(msg);
        }
    }
}
