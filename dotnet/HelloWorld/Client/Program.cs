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
			Start();

		}

		public static void Start()
		{
			using (NetMQContext context = NetMQContext.Create())
			using (NetMQSocket clientSocket = context.CreateRequestSocket())
			{
				clientSocket.Connect("tcp://127.0.0.1:5556");

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
