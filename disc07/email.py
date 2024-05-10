class Email:
    """Every email object has 3 instance attributes: the
    message, the sender name, and the recipient name.
    """

    def __init__(self, msg, sender_name, recipient_name):
        self.msg = msg
        self.sender_name = sender_name
        self.recipient_name = recipient_name


class Server:
    """Each Server has an instance attribute clients, which
    is a dictionary that associates client names with
    client objects.
    """

    def __init__(self):
        self.clients = {}

    def send(self, email):
        """Take an email and put it in the inbox of the client
        it is addressed to.
        """
        name = email.recipient_name
        client = self.clients[name]
        client.receive(email)

    def register_client(self, client, client_name):
        """Takes a client object and client_name and adds them
        to the clients instance attribute.
        """
        self.clients[client_name] = client


class Client:
    """Every Client has instance attributes name (which is
    used for addressing emails to the client), server
    (which is used to send emails out to other clients), and
    inbox (a list of all emails the client has received).
    """

    def __init__(self, server, name):
        self.inbox = []
        self.name = name
        self.server = server
        server.register_client(self, self.name)

    def compose(self, msg, recipient_name):
        """Send an email with the given message msg to the
        given recipient client.
        """
        email = Email(msg, self.name, recipient_name)
        self.server.send(email)

    def receive(self, email):
        """Take an email and add it to the inbox of this
        client.
        """
        self.inbox += [email]


server = Server()
wqj = Client(server, "wqj")
wcy = Client(server, "wcy")

eamil1 = Email("I LOVE YOU", wqj.name, wcy.name)
eamil2 = Email("I LOVE YOU TOO", wcy.name, wqj.name)

wqj.compose("I love you", "wcy")
wcy.compose("I love you too", "wqj")
wqj.compose("I love you more", "wcy")
wcy.compose("I love you most", "wqj")
print("wqj's mail box:")
for mail in wqj.inbox:
    print(mail.msg)
print("wcy's mail box:")
for mail in wcy.inbox:
    print(mail.msg)
