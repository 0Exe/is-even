def even(num:int):
    if num % 2 != 0:
        return(False)
    else:
        return(True)

async def async_even(num:int):
    if num % 2 != 0:
        return(False)
    else:
        return(True)
    
def odd(num:int):
    if num % 2 == 0:
        return(False)
    else:
        return(True)

async def async_odd(num:int):
    if num % 2 == 0:
        return(False)
    else:
        return(True)
