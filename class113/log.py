# sistema de log fictício

# mixin: é uma classe que contém métodos para utilização por
# outras classes sem ter que ser a classe principal 

class LogMixin:
    @staticmethod
    def write(msg):
        with open('log.log', 'a+') as f:
            f.write(msg)
            f.write('\n')

    def log_info(self, msg):
        self.write(f'INFO: {msg}')

    def log_error(self, msg):
        self.write(f'ERROR: {msg}')
