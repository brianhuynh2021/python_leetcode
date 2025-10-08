# Day 06 - Scalability Example Code


# Simple Round Robin Load Balancer
class LoadBalancer:
    def __init__(self, servers):
        self.servers = servers
        self.index = 0

    def get_server(self):
        server = self.servers[self.index]
        self.index = (self.index + 1) % len(self.servers)
        return server


if __name__ == "__main__":
    servers = ["server1", "server2", "server3"]
    lb = LoadBalancer(servers)

    print("Distributing requests:")
    for i in range(6):
        print(f"Request {i+1} -> {lb.get_server()}")
