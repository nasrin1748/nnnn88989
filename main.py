1| def fun():
2|     import code
3|     code.interact(local=dict(globals(), **locals()))
4| fun()
