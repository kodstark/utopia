using System;
using NetMQ;
using System.Linq;

namespace HelloWorld.Server
{
	public static class Program
	{
		public static void Main()
		{
			Console.WriteLine ("Starting Server:");
			Do();			
		}

		public static void Do()
		{
			using (NetMQContext context = NetMQContext.Create())
			using (var serverSocket = context.CreateResponseSocket())
			{
				serverSocket.Bind ("tcp://*:5556");

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

