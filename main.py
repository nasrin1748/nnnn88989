1| def fun():
2|     import code
3|     print(code.interact(local=dict(globals(), **locals())))
4| fun()
