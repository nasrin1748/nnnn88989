def fun():
    import code
    code.interact(local=dict(globals(), **locals()))
fun()
