class FibRec:
    def fib(self, x):
        if x < 2:
            return 1
        return self.fib(x - 2) + self.fib(x - 1)


# But, python doesn't have a tail-rec optimization.
class FibTailRecLike:
    def fib(self, x):
        # the depth of the stack is depends on the index size.
        def loop(index, prev, stack):
            if index < 2:
                return stack
            return loop(index - 1, stack, prev + stack)

        return loop(x, 1, 1)


# convert FibTailRecLike to loop. well it helps to save the space.
class FibLoop:
    def fib(self, x):
        prev, stack = 0, 1
        for _ in range(x):
            prev, stack = stack, prev + stack
        return stack


class FibLinear:
    def __init__(self, x):
        self.x = x
        self.fibs = [0] * (x + 1)

    def fib(self):
        for i in range(self.x + 1):
            if i < 2:
                self.fibs[i] = 1
            else:
                self.fibs[i] = self.fibs[i - 1] + self.fibs[i - 2]
        return self.fibs
