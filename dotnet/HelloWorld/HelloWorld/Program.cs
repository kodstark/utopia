using System;
using NetMQ;
using System.Linq;

namespace HelloWorld.Server
{
	public static class Program
	{
		public static void Main(string[] args)
		{

			Console.WriteLine ("Starting Server:");

			string url;

			if (args != null && args.Length == 1)
				url = args [0];
			else
				url = "tcp://*:5556";

			Do(url);			
		}

		public static void Do(string url)
		{
			using (NetMQContext context = NetMQContext.Create())
			using (var serverSocket = context.CreateResponseSocket())
			{
				serverSocket.Bind (url);

				while (true)
				{
					var message = serverSocket.ReceiveString ();
					Console.WriteLine("Receive message {0}", message);

					serverSocket.Send("World");          

					if (message == "exit")
					{
						break;
					}
				}	
			}
		}
	}


}

