def null_check(value):
    if value:
        return value
    else:
        raise ValueError("is null!")
    
__all__ = [
    "null_check"
]