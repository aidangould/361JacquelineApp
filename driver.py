import zmq

context = zmq.Context()
socket = context.socket(zmq.REQ)
socket.connect("tcp://localhost:5555")

#send notification to admin that user added recipe

socket.send_string("TYPE: admin; CONTACT: gouldai@oregonstate.edu; USER: xyz@gmail.com; RECIPE NAME: \"avocado \
    toast\"; RECIPE: ingredients: bread, avocado. instructions: mash avacado, toast bread, spread avacado on toast")

#send summary of recipe to user that created it

socket.send_string("TYPE: user; CONTACT: gouldai@oregonstate.edu; RECIPE NAME: \"avocado toast\"")
