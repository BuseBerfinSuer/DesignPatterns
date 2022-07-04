class Target:
   
    def request(self):
        return 

class Adaptee:

    def specific_request(self):
        return ".eetpadA eht fo roivaheb laicepS"


class Adapter(Target, Adaptee):
   
    def request(self):
        return f"Adapter: (TRANSLATED) {self.specific_request()[::-1]}"


def client_code(target: "Target") -> None:

    print(target.request(), end="")

adaptee = Adaptee()
print("Client: Hi. Give me the information.:")
print(f"Adaptee: {adaptee.specific_request()}", end="\n\n")


print("Client: I don't understand it:")
adapter = Adapter()
client_code(adapter)