import telebot
import socket


def print_hi_every_20_seconds(port=8080):
    bot = telebot.TeleBot('8086087869:AAFk_Giw_GNfERxvhv_ykkm-qANw2jOjIcA')

    # Create a socket object
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    
    # Bind the socket to a host and port
    host = "0.0.0.0"  # Listen on all available interfaces
    server_socket.bind((host, port))
    
    # Listen for incoming connections
    server_socket.listen(1)
    print(f"Server is running and listening on port {port}...")
    @bot.message_handler(commands=['start', 'hello'])
    def send_welcome(message):
        bot.reply_to(message, "Welcome to the chaos, my friend! 🌟 I’m Mondo—your quirky guide to a world of randomness, laughs, and surprises. Got a wild idea? Throw it at me, and let’s turn it into a masterpiece... or at least something worth sharing! Let’s Mondo-fy your day! 😎🎨")
    bot.infinity_polling()
    
    while True:
        print(f"Server is running and listening on port {port}...")
        # Wait for a client to connect
        client_socket, client_address = server_socket.accept()
        
        
        try:
            # Send "hi" to the client every 20 seconds
            while True:
                print('')
        except (BrokenPipeError, ConnectionResetError):
            print(f"Connection lost with {client_address}. Waiting for a new connection...")
            client_socket.close()

# Call the function and bind it to port 8080
print_hi_every_20_seconds(port=8080)
