using System;
using NetMQ;
using System.Linq;

namespace HelloWorld.Client
{
	public static class Program
	{

		public static void Main()
		{
			Console.WriteLine("Starting Client:");
			string url;

			if (args != null && args.Length == 1)
				url = args [0];
			else
				url = "tcp://*:5556";

			Do(url);	

		}

		public static void Start(string url)
		{
			using (NetMQContext context = NetMQContext.Create())
			using (NetMQSocket clientSocket = context.CreateRequestSocket())
			{
				clientSocket.Connect(url);

				while (true)
				{
					Console.WriteLine("Please enter your message:");
					string message = Console.ReadLine();
					clientSocket.Send(message);

					string answer = clientSocket.ReceiveString();
					Console.WriteLine("Answer from server: {0}", answer);

					if (message == "exit")
					{
						break;
					}
				}
			}
		}
	}
}
