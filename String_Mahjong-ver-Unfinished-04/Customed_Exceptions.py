class LoopCannotBreakError(Exception):
    """When a loop cannot be break and this exception will be thrown.
        当一个循环无法正常跳出的时候将抛出该异常。"""
    def __init__(self, loop_name):
        self.name = loop_name

    def __str__(self):
        return ("{} this loop cannot break. 无法跳出 {} 循环".format(repr((self.name, self.name)))
