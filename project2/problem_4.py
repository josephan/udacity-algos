class Group(object):
    def __init__(self, _name, cache):
        self.name = _name
        self.groups = []
        self.users = []
        self.cache = cache

    def add_group(self, group):
        self.groups.append(group)

    def add_user(self, user):
        self.users.append(user)
        self.cache.cache_user(user, self)

    def get_groups(self):
        return self.groups

    def get_users(self):
        return self.users

    def get_name(self):
        return self.name

class UsersByGroupCache:
    def __init__(self):
        self.cache = {}

    def cache_user(self, user, group):
        if group in self.cache:
            self.cache[group][user] = True
        else:
            self.cache[group] = {user: True}

    def is_user_in_group(self, user, group):
        """
        Return True if user is in the group, False otherwise.

        Args:
        user(str): user name/id
        group(class:Group): group to check user membership against
        """
        if group in self.cache:
            return user in self.cache[group]
        return False


cache = UsersByGroupCache()
parent = Group("parent", cache)
child = Group("child", cache)
sub_child = Group("subchild", cache)

sub_child_user = "sub_child_user"
sub_child.add_user(sub_child_user)

child.add_group(sub_child)
parent.add_group(child)

# test if a user is in group
def test1():
    print(cache.is_user_in_group(sub_child_user, sub_child))

test1()
# Should return True

# test if a fake user is not in group
def test2():
    print(cache.is_user_in_group("", sub_child))

test2()
# Should return False


# test if a real user is not in fake group
def test3():
    print(cache.is_user_in_group(sub_child_user, ""))

test3()
# Should return False

