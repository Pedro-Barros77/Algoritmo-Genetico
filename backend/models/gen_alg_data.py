class data():
    """A container class to hold genetic_algorithm result values.
    """
    def __init__(self, **kwargs):
        self.time_list = kwargs.get("time_list") or []
        self.bestscores_list = kwargs.get("bestscores_list") or []
        self.mutations_list = kwargs.get("mutations_list") or []
        self.generations_list = kwargs.get("generations_list") or []
    
    time_list = []
    bestscores_list = []
    mutations_list = []
    generations_list = []