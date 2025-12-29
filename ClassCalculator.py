class Calculator:
    def __init__(self):
        pass

    def reshenie(self, x, y, deistvie):
        if deistvie == 'plus':
            return x + y
        if deistvie == 'minus':
            return x - y
        if deistvie == 'umnojenie':
            return x * y
        if deistvie == 'delenie':
            return x / y
