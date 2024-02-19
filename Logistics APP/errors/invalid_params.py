class InvalidParams(Exception):
    def __init__(self, count: int, cmd_name):
        super().__init__(f'{cmd_name} command expects {count} parameters.')