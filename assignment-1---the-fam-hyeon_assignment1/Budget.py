class Budget:
    def __init__(self, budget, limit, locked):
        self._budget = budget
        self._limit = limit
        self._locked = locked

    def get_limit(self):
        return self._limit

    def set_limit(self, limit):
        self._limit = int(limit)

    def get_budget(self):
        return self._budget

    def set_budget(self, budget):
        self._budget = int(budget)

    def get_locked(self):
        return self._locked

    def set_locked(self, is_locked):
        self._locked = is_locked

    def __str__(self):
        return f"hello {self._budget} limit is {self._limit}"