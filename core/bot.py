from abc import ABC, abstractmethod


class Bot(ABC):
    """
    Base class for all simulation types (sim, paper, trade)
    """

    def __init__(self, args, config_file):
        super(Bot, self).__init__()
        self.args = args


    @abstractmethod
    def get_next(self, interval):
        pass