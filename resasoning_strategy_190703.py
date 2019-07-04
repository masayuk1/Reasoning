import time
from pyknow import *


class Greetings(KnowledgeEngine):
    @DefFacts()
    def _initial_action(self):
        yield Fact(action="greet")
        global a
        global b
        a,b=input().split()
        print("hoge2")

    @Rule(Fact(action='greet'),
          NOT(Fact(name=W())))
    def ask_name(self):
        self.declare(Fact(name=a,time_stamp=b))
        print("a:%s b:%s c:%s e:%s"  %(a,b,c,e))

    @Rule(Fact(action='greet'),
          NOT(Fact(location=W())))
    def ask_location(self):
        print("test")
        self.declare(Fact(location=input()))

    @Rule(Fact(action='greet'),
          Fact(name=MATCH.name),
          Fact(location=MATCH.location))
    def greet(self, name, location):
        print("Hi %s! How is the weather in %s?" % (name, location))

engine = Greetings()
engine.reset()  # Prepare the engine for the execution.
c,e=input().split()
print("Hi %s! How is the weather in %s?" % (c,e))
print("hoge")
engine.run()  # Run it!