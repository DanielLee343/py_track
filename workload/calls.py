import time


class PythonFunctionCalls:

    version = 2.0
    operations = 5*(1+4+4+2)
    rounds = 60000

    def test(self):

        global f, f1, g, h

        # define functions
        def f():
            pass

        def f1(x):
            pass

        def g(a, b, c):
            return a, b, c

        def h(a, b, c, d=1, e=2, f=3):
            return d, e, f

        # do calls
        for i in range(self.rounds):

            f()
            f1(i)
            f1(i)
            f1(i)
            f1(i)
            g(i, i, i)
            g(i, i, i)
            g(i, i, i)
            g(i, i, i)
            h(i, i, 3, i, i)
            h(i, i, i, 2, i, 3)

            f()
            f1(i)
            f1(i)
            f1(i)
            f1(i)
            g(i, i, i)
            g(i, i, i)
            g(i, i, i)
            g(i, i, i)
            h(i, i, 3, i, i)
            h(i, i, i, 2, i, 3)

            f()
            f1(i)
            f1(i)
            f1(i)
            f1(i)
            g(i, i, i)
            g(i, i, i)
            g(i, i, i)
            g(i, i, i)
            h(i, i, 3, i, i)
            h(i, i, i, 2, i, 3)

            f()
            f1(i)
            f1(i)
            f1(i)
            f1(i)
            g(i, i, i)
            g(i, i, i)
            g(i, i, i)
            g(i, i, i)
            h(i, i, 3, i, i)
            h(i, i, i, 2, i, 3)

            f()
            f1(i)
            f1(i)
            f1(i)
            f1(i)
            g(i, i, i)
            g(i, i, i)
            g(i, i, i)
            g(i, i, i)
            h(i, i, 3, i, i)
            h(i, i, i, 2, i, 3)

    def calibrate(self):

        global f, f1, g, h

        # define functions
        def f():
            pass

        def f1(x):
            pass

        def g(a, b, c):
            return a, b, c

        def h(a, b, c, d=1, e=2, f=3):
            return d, e, f

        # do calls
        for i in range(self.rounds):
            pass

###


class ComplexPythonFunctionCallsrange:

    version = 2.0
    operations = 4*5
    rounds = 100000

    def test(self):

        # define functions
        def f(a, b, c, d=1, e=2, f=3):
            return f

        args = 1, 2
        kwargs = dict(c=3, d=4, e=5)

        # do calls
        for i in range(self.rounds):
            f(a=i, b=i, c=i)
            f(f=i, e=i, d=i, c=2, b=i, a=3)
            f(1, b=i, **kwargs)
            f(*args, **kwargs)

            f(a=i, b=i, c=i)
            f(f=i, e=i, d=i, c=2, b=i, a=3)
            f(1, b=i, **kwargs)
            f(*args, **kwargs)

            f(a=i, b=i, c=i)
            f(f=i, e=i, d=i, c=2, b=i, a=3)
            f(1, b=i, **kwargs)
            f(*args, **kwargs)

            f(a=i, b=i, c=i)
            f(f=i, e=i, d=i, c=2, b=i, a=3)
            f(1, b=i, **kwargs)
            f(*args, **kwargs)

            f(a=i, b=i, c=i)
            f(f=i, e=i, d=i, c=2, b=i, a=3)
            f(1, b=i, **kwargs)
            f(*args, **kwargs)

    def calibrate(self):

        # define functions
        def f(a, b, c, d=1, e=2, f=3):
            return f

        args = 1, 2
        kwargs = dict(c=3, d=4, e=5)

        # do calls
        for i in range(self.rounds):
            pass

###


class BuiltinFunctionCallsrange:

    version = 2.0
    operations = 5*(2+5+5+5)
    rounds = 60000

    def test(self):

        # localize functions
        f0 = globals
        f1 = hash
        f2 = cmp
        f3 = range

        # do calls
        for i in range(self.rounds):

            f0()
            f0()
            f1(i)
            f1(i)
            f1(i)
            f1(i)
            f1(i)
            f2(1, 2)
            f2(1, 2)
            f2(1, 2)
            f2(1, 2)
            f2(1, 2)
            f3(1, 3, 2)
            f3(1, 3, 2)
            f3(1, 3, 2)
            f3(1, 3, 2)
            f3(1, 3, 2)

            f0()
            f0()
            f1(i)
            f1(i)
            f1(i)
            f1(i)
            f1(i)
            f2(1, 2)
            f2(1, 2)
            f2(1, 2)
            f2(1, 2)
            f2(1, 2)
            f3(1, 3, 2)
            f3(1, 3, 2)
            f3(1, 3, 2)
            f3(1, 3, 2)
            f3(1, 3, 2)

            f0()
            f0()
            f1(i)
            f1(i)
            f1(i)
            f1(i)
            f1(i)
            f2(1, 2)
            f2(1, 2)
            f2(1, 2)
            f2(1, 2)
            f2(1, 2)
            f3(1, 3, 2)
            f3(1, 3, 2)
            f3(1, 3, 2)
            f3(1, 3, 2)
            f3(1, 3, 2)

            f0()
            f0()
            f1(i)
            f1(i)
            f1(i)
            f1(i)
            f1(i)
            f2(1, 2)
            f2(1, 2)
            f2(1, 2)
            f2(1, 2)
            f2(1, 2)
            f3(1, 3, 2)
            f3(1, 3, 2)
            f3(1, 3, 2)
            f3(1, 3, 2)
            f3(1, 3, 2)

            f0()
            f0()
            f1(i)
            f1(i)
            f1(i)
            f1(i)
            f1(i)
            f2(1, 2)
            f2(1, 2)
            f2(1, 2)
            f2(1, 2)
            f2(1, 2)
            f3(1, 3, 2)
            f3(1, 3, 2)
            f3(1, 3, 2)
            f3(1, 3, 2)
            f3(1, 3, 2)

    def calibrate(self):

        # localize functions
        f0 = dir
        f1 = hash
        f2 = range
        f3 = range

        # do calls
        for i in range(self.rounds):
            pass

###


class PythonMethodCallsrange:

    version = 2.0
    operations = 5*(6 + 5 + 4)
    rounds = 30000

    def test(self):

        class c:

            x = 2
            s = 'string'

            def f(self):

                return self.x

            def j(self, a, b):

                self.y = a
                self.t = b
                return self.y

            def k(self, a, b, c=3):

                self.y = a
                self.s = b
                self.t = c

        o = c()

        for i in range(self.rounds):

            o.f()
            o.f()
            o.f()
            o.f()
            o.f()
            o.f()
            o.j(i, i)
            o.j(i, i)
            o.j(i, 2)
            o.j(i, 2)
            o.j(2, 2)
            o.k(i, i)
            o.k(i, 2)
            o.k(i, 2, 3)
            o.k(i, i, c=4)

            o.f()
            o.f()
            o.f()
            o.f()
            o.f()
            o.f()
            o.j(i, i)
            o.j(i, i)
            o.j(i, 2)
            o.j(i, 2)
            o.j(2, 2)
            o.k(i, i)
            o.k(i, 2)
            o.k(i, 2, 3)
            o.k(i, i, c=4)

            o.f()
            o.f()
            o.f()
            o.f()
            o.f()
            o.f()
            o.j(i, i)
            o.j(i, i)
            o.j(i, 2)
            o.j(i, 2)
            o.j(2, 2)
            o.k(i, i)
            o.k(i, 2)
            o.k(i, 2, 3)
            o.k(i, i, c=4)

            o.f()
            o.f()
            o.f()
            o.f()
            o.f()
            o.f()
            o.j(i, i)
            o.j(i, i)
            o.j(i, 2)
            o.j(i, 2)
            o.j(2, 2)
            o.k(i, i)
            o.k(i, 2)
            o.k(i, 2, 3)
            o.k(i, i, c=4)

            o.f()
            o.f()
            o.f()
            o.f()
            o.f()
            o.f()
            o.j(i, i)
            o.j(i, i)
            o.j(i, 2)
            o.j(i, 2)
            o.j(2, 2)
            o.k(i, i)
            o.k(i, 2)
            o.k(i, 2, 3)
            o.k(i, i, c=4)

    def calibrate(self):

        class c:

            x = 2
            s = 'string'

            def f(self):

                return self.x

            def j(self, a, b):

                self.y = a
                self.t = b

            def k(self, a, b, c=3):

                self.y = a
                self.s = b
                self.t = c

        o = c

        for i in range(self.rounds):
            pass

###


class Recursionrange:

    version = 2.0
    operations = 5
    rounds = 100000

    def test(self):

        global f

        def f(x):

            if x > 1:
                return f(x-1)
            return 1

        for i in range(self.rounds):
            f(10)
            f(10)
            f(10)
            f(10)
            f(10)

    def calibrate(self):

        global f

        def f(x):

            if x > 0:
                return f(x-1)
            return 1

        for i in range(self.rounds):
            pass


# Test to make Fredrik happy...
if __name__ == '__main__':
    start_time = time.time()
    for i in range(20):
        ins1 = PythonFunctionCalls()
        ins1.test()
        ins1.calibrate()
        ins2 = ComplexPythonFunctionCallsrange()
        ins2.test()
        ins2.calibrate()
        ins3 = PythonMethodCallsrange()
        ins3.test()
        ins3.calibrate()
        ins4 = Recursionrange()
        ins4.test()
        ins4.calibrate()

    elapsed_time = time.time() - start_time
    print(f"Compute time: {elapsed_time:.2f} seconds")
