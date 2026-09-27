class User:
    def __init__(self, user):
        if isinstance(user, dict):
            self.email = user.get('email')
            self.name = user.get('name')
            self.id = user.get('id')
            self.cost = user.get('cost') or 0
            self.time = user.get('time') or 0
            self.career = user.get('career')
        else:
            # Handle py2neo Node objects
            self.email = getattr(user, 'email', None)
            self.name = getattr(user, 'name', None)
            self.id = getattr(user, 'id', None) or user.identity if hasattr(user, 'identity') else None
            self.cost = getattr(user, 'cost', 0) or 0
            self.time = getattr(user, 'time', 0) or 0
            self.career = getattr(user, 'career', None)

    def is_time(self):
        return self.time is not None and self.time > 0

    def is_cost(self):
        return self.cost is not None and self.cost > 0

    def get_user(self):
        return {
            "id": self.id,
            "name": self.name,
            "email": self.email,
            "cost": self.cost,
            "time": self.time,
            "career": self.career
        }
