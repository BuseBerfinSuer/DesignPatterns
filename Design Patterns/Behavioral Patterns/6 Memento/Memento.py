import copy

class Originator(object):

    class Memento(object):
        def __init__(self, mstate):
            self.mstate = mstate

        def rollback_state(self):
            return self.mstate

    def set_state(self, state):
        print ('Setup state to {0}'.format(state))
        self.state = state

    def save_state(self):
        print ('Saving state')
        return self.Memento(copy.deepcopy(self))

    def rollback_state(self, memento):
        self = memento.rollback_state()
        print ('Rollback to state {0}'.format(self.state))

orig = Originator()
orig.set_state('1')
orig.set_state('2')
saved_state = orig.save_state()
orig.set_state('3')
orig.rollback_state(saved_state)