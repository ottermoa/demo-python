def loop(func_name, args=[]):
    '''
   func_name -> str
   args -> [str]
   condition -> function
   '''
    if (globals["condition"].__doc__ == "for"):
        _condition = eval("condition()", globals, locals)
        for _ in range(_condition):
            eval(func_name + f"({','.join(args)})", globals, locals)
 
        return 1
    elif (globals["condition"].__doc__ == "while"):
        while 1:
            _condition = eval("condition()", globals, locals)
            if not(_condition):
                break
            eval(func_name + f"({','.join(args)})", globals, locals)
 
        return 1
    else:
        raise ValueError(f"Condition's docstring should be while or for.")