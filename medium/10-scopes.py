def funcion_externa():
    def do_local():
        var = "local variable"
        print("Asignacion local:", var)

    def do_nonlocal():
        nonlocal var
        var = "nonlocal variable"

    def do_global():
        global var
        var = "global var"
    
    var = "var de la funcion externa"
    do_local()
    print("After local assignment:", var)
    
    do_nonlocal()
    print("After nonlocal assignment:", var)
    
    do_global()
    print("After global assignment:", var)

funcion_externa()
print("In global scope:", var)