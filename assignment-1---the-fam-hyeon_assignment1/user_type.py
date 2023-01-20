class UserType:

    def __init__(self, kind, lock_status):
        self._kind = kind
        self._lock_status = False
        self._warning_budget_limit = None
        self.set_warning_budget_limit()

    def set_lock_status(self, new_status):
        self._lock_status = new_status

    def set_warning_budget_limit(self):
        if self._kind == "Angel":
            self._warning_budget_limit = 0.9
        elif self._kind == "Rebel":
            self._warning_budget_limit = 120
        elif self._kind == "Troublemaker":
            self._warning_budget_limit = 60

    def exceeding_notify(self, limit, spend):
        if (spend / limit) >= self._warning_budget_limit:
            print("Your spending exceeds", self._warning_budget_limit)
