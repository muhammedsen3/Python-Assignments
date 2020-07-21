def not_string(x):
    return (lambda x:print(x) if x[:3]==('not') else print('not', x))(x)
not_string('mahmut')