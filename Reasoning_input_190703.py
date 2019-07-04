import time
from pyknow import *
import json

class Contexts(KnowledgeEngine):
    @Rule(AS.first << Fact(name='1'),
        Fact(name='2'),
        AS.second << Fact(name='3'),
        TEST(lambda first, second: first.get("time_stamp") < second.get("time_stamp")))
    def a(self, first, second):
        print("a")
        self.declare(Fact(name='a',time_stamp=100))

    @Rule(AS.first << Fact(name='2'),
        AS.second << Fact(name='3'),
        TEST(lambda first, second: first.get("time_stamp") < second.get("time_stamp")))
    def b(self, first, second):
        print("b")
        self.declare(Fact(name='b',time_stamp=102))

    @Rule(Fact(name='2'),
        Fact(name='a'))
        # TEST(lambda first, second: first.get("time_stamp") < second.get("time_stamp")))
    def c(self):
        print("c")
        self.declare(Fact(name='c',time_stamp=103))


    # @Rule(AS.first << Fact(name='4'),
    #     AS.second << Fact(name='a'),
    #     TEST(lambda first, second: first.get("time_stamp") < second.get("time_stamp")))
    # def c(self, first, second):
    #     print("c")
    #     self.declare(Fact(name='c',time_stamp=103))

    @Rule(AS.first << Fact(name='4'),
        AS.second << Fact(name='a'),
        TEST(lambda first, second: first.get("time_stamp") < second.get("time_stamp")))
    def d(self, first, second):
        print("d")
        self.declare(Fact(name='d',time_stamp=104))

    @Rule(AS.first << Fact(name='1'),
        AS.second << Fact(name='3'),
        TEST(lambda first, second: first.get("time_stamp") < second.get("time_stamp")))
    def e(self, first, second):
        print("e")
        self.declare(Fact(name='e',time_stamp=105))

    @Rule(AS.first << Fact(name='1'),
        AS.second << Fact(name='2'),
        TEST(lambda first, second: first.get("time_stamp") < second.get("time_stamp")))
    def f(self, first, second):
        print("f")
        self.declare(Fact(name='f',time_stamp=106))


    # @Rule(AS.first << Fact(name='c'),
    #     Fact(name='g'),
    #     AS.second << Fact(name='e'),
    #     TEST(lambda first, second: first.get("time_stamp") < second.get("time_stamp")))
    # def e(self, first, second):
    #     print("s")
    #     self.declare(Fact(name='s',time_stamp=1))

    # @Rule(AS.first << Fact(name='s'),
    #     AS.second << Fact(name='g'),
    #     TEST(lambda first, second: first.get("time_stamp") < second.get("time_stamp")))
    # def f(self, first, second):
    #     print("t")
    #     self.declare(Fact(name='t',time_stamp=4))

engine = Contexts()
engine.reset()

engine.declare(Fact(name="1",time_stamp=1))
engine.run()
engine.declare(Fact(name="2",time_stamp=2))
engine.run()
engine.declare(Fact(name="3",time_stamp=3))
print("1番目ののfact")
engine.run()

engine.declare(Fact(name="4",time_stamp=4))
engine.declare(Fact(name="5",time_stamp=5))
print("2番目のfact")
engine.run()

engine.declare(Fact(name="2",time_stamp=6))
print("3番目のfact")
engine.run()

engine.declare(Fact(name="2",time_stamp=7))
print("4番目のfact")
engine.run()

# engine.declare(Fact(name="3",time_stamp=6))
# print("4番目のfact")
# engine.run()

engine.declare(Fact(name="6",time_stamp=6))
engine.declare(Fact(name="7",time_stamp=7))
engine.declare(Fact(name="8",time_stamp=8))
engine.declare(Fact(name="9",time_stamp=9))
engine.declare(Fact(name="10",time_stamp=10))
engine.declare(Fact(name="11",time_stamp=11))
engine.declare(Fact(name="12",time_stamp=12))

engine.run()