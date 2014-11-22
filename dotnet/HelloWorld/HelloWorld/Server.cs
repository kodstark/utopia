using System;
using NetMQ;
using System.Linq;
using System.Threading.Tasks;

namespace HelloWorld
{
	public class Program
	{
		public static void Main()
		{
			using (NetMQContext context = NetMQContext.Create())
			{
				Task serverTask = Task.Factory.StartNew(() => Server(context));
				Task clientTask = Task.Factory.StartNew(() => Client(context));
				Task.WaitAll(serverTask, clientTask);
			}		
		}

		public static void Server(NetMQContext context)
		{
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

		public static void Client(NetMQContext context)
		{
			using (NetMQSocket clientSocket = context.CreateRequestSocket())
			{
				clientSocket.Connect("tcp://127.0.0.1:5556");

				while (true)
				{
					Console.WriteLine("Please enter your message:");
					string message = Console.ReadLine();
					clientSocket.Send(message);
					try{
					string answer = clientSocket.ReceiveString();
						Console.WriteLine("Answer from server: {0}", answer);
					
					}catch(Exception e){
						var temp = e.Message;
					}


					if (message == "exit")
					{
						break;
					}
				}
			}
		}
	}
}

