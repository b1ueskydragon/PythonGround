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
