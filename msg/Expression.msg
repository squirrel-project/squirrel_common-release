# Robot expressions
# These can be epxressed via sound (beep), head movements (nod), body movements (wiggle)
# The expression message itself is just a regular string, but only the constants
# below should be used!
#
# Michael Zillich, April 2016

# complete list of all expressions that the robot can display

# -------------- standard expressions --------------

# just looking neutral, straight ahead
string NEUTRAL = NEUTRAL

# hello
string HELLO = HELLO

# and good bye
string GOODBYE = GOODBYE

# ok, acknowledge
string OK = OK

# yes, as an answer to a polar question
string YES = YES

# no, as an answer to a polar question
string NO = NO

# something succeeded, expressing happiness
string CHEERING = CHEERING

# something went wrong, expressing distress
string OH_NO = OH_NO

# whaat? something is unclear, I am confused
string CONFUSED = CONFUSED

# something unexpected just happened
string SURPRISED = SURPRISED

# I am waiting for some input from you
string ASKING = ASKING

# I need time to think harder
string THINKING = THINKING

# look here, here! trying to grab the user's attention
string HERE_HERE = HERE_HERE

# ouch! a bumper was touched
string OUCH = OUCH


# -------------- special, scenario specific expressions --------------

# robot e.g. pushes away relevant object for the task
string ANTAGONIST = ANTAGONIST

# moving base of 30 degrees to target object (necessary task knowledge)
string REFERENTIAL_INFO = REFERENTIAL_INFO

# handing an object to child by placing object in front of the child
string HANDOVER_OBJECT_DOWN = HANDOVER_OBJECT_DOWN

# handing an object to child by placing object into the hand of the child 
string HAND_TO_HAND = HAND_TO_HAND

# while pushing an object
string PUSHING = PUSHING
