class State:
    def __init__(self, missionaries, cannibals, canoe):
        self.missionaries = missionaries
        self.cannibals = cannibals
        self.canoe = canoe
        self.color = None
        self.parent = None
    
    def canoe_across(self, missionaries, cannibals):
        new_state = State(self.missionaries, self.cannibals, self.canoe)
        new_state.missionaries = new_state.missionaries - missionaries if new_state.canoe == 0 \
            else new_state.missionaries + missionaries
        new_state.cannibals = new_state.cannibals - cannibals if new_state.canoe == 0 else \
            new_state.cannibals + cannibals
        new_state.canoe = 0 if new_state.canoe == 1 else 1
        new_state.parent = self
        return new_state

    def find_next_possible_states(self):
        possible_states = []
        max_allowed_missionaries = self.missionaries if self.canoe == 0 else 3 - self.missionaries
        max_allowed_cannibals = self.cannibals if self.canoe == 0 else 3 - self.cannibals

        for i in range(max_allowed_missionaries + 1):
            for j in range(max_allowed_cannibals + 1):
                if 1 <= i + j <= 2:
                    new_state = self.canoe_across(i, j)
                    possible_states.append(new_state)
        return possible_states

    def is_already_generated(self, generated_list):
        return self in generated_list

    def is_dead(self):
        return (self.missionaries < self.cannibals and self.missionaries !=0) or \
            (3 - self.missionaries < 3 - self.cannibals and 3 - self.missionaries !=0)

    def get_state(self):
        return (self.missionaries, self.cannibals, self.canoe)

    def operator(self):
        direction = "←" if self.parent.canoe == 0 else "→" 
        return f"""({abs(self.parent.missionaries - self.missionaries)},
         {abs(self.parent.cannibals - self.cannibals)})\n{direction}"""

    def __eq__(self, o):
        return self.missionaries == o.missionaries and self.cannibals == o.cannibals and \
            self.canoe == o.canoe
    
    def __repr__(self):
        return f"({self.missionaries}, {self.cannibals}, {self.canoe})"


def bfs(initial_state):
    generated = []
    fringe = []

    initial_state.color = "pink"
    fringe.append(initial_state)

    while fringe:
        element = fringe.pop(0)

        if element.get_state() == (0, 0, 1):
            element.color = "green"
            generated.append(element)
            continue

        if element.is_dead():
            element.color = "red"
            generated.append(element)
            continue
        
        if element.is_already_generated(generated):
            element.color = "gray"
            generated.append(element)
            continue
        
        element.color = "pink"
        generated.append(element)
        children = element.find_next_possible_states()
        fringe.extend(children)
    
    return generated


if __name__ == "__main__":
    initial_state = State(3, 3, 0)
    states = bfs(initial_state)
    print(states)
    print(len(states))