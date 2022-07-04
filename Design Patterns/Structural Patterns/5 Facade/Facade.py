from __future__ import annotations


class Facade:

    def __init__(self, sub1: Sub1, sub2: Sub2):

        self._sub1 = sub1 or Sub1()
        self._sub2 = sub2 or Sub2()

    def operation(self):

        results = []
        results.append("Initializes subs:")
        results.append(self._sub1.operation1())
        results.append(self._sub2.operation1())
        results.append("Perform the action:")
        results.append(self._sub1.operation_n())
        results.append(self._sub2.operation_z())
        return "\n".join(results)


class Sub1:

    def operation1(self):
        return "Subsystem1: Ready!"

    def operation_n(self):
        return "Subsystem1: Go!"


class Sub2:
    
    def operation1(self):
        return "Subsystem2: Get ready!"

    def operation_z(self):
        return "Subsystem2: Fire!"


def client(facade: Facade) -> None:

    print(facade.operation(), end="")


sub1 = Sub1()
sub2 = Sub2()
facade = Facade(sub1, sub2)
client(facade)