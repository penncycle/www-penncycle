#!/usr/bin/python

with open("index.html", "r") as f:
    with open("local.html", "w") as g:
        g.write(f.read().replace("localhost:8001", "www.penncycle.org"))

