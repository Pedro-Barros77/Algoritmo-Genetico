from backend.models import gen_alg_data

def data(**kwargs):
    """A container class to hold genetic_algorithm result values.
    """
    return gen_alg_data.data(**kwargs)