import time
from pyknow import *
import json

class Contexts(KnowledgeEngine):
    @DefFacts()
    def _initial_action(self):
        yield Fact(name="a",time_stamp=1)
        yield Fact(name="b",time_stamp=2)

        yield Fact(name="c",time_stamp=3)
        yield Fact(name="d",time_stamp=4)

        yield Fact(name="x",time_stamp=5)
        yield Fact(name="z",time_stamp=6)

        # yield Fact(name="d",time_stamp=5)
        # yield Fact(name="e",time_stamp=6)

        
    @Rule(AS.first << Fact(name='d'),
        # Fact(name='z'),
        AS.second << Fact(name='b'),
        TEST(lambda first, second: first.get("time_stamp") < second.get("time_stamp")))
    def aaa(self, first, second):
        print("e")
        # self.declare(Fact(name='e',time_stamp=1))

    @Rule(AS.first << Fact(name='c'),
        AS.second << Fact(name='a'),
        TEST(lambda first, second: first.get("time_stamp") < second.get("time_stamp")))
    def door_move(self, first, second):
        print("f")
        # self.declare(Fact(name='f',time_stamp=2))

    @Rule(AS.first << Fact(name='e'),
        AS.second << Fact(name='f'),
        TEST(lambda first, second: first.get("time_stamp") < second.get("time_stamp")))
    def going_home(self, first, second):
        print("g")




engine = Contexts()
engine.reset()
engine.run()