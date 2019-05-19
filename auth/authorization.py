from .authentication import Authenticator, InvalidUsername, NotLoggedInError, NotPermittedError


class PermissionError(Exception):
    pass


class Authorizor:
    def __init__(self, authenticator):
        """
        Initializes the Authorizor.
        """
        self.authenticator = authenticator
        self.permissions = {}

    def add_permission(self, perm_name):
        """
        Create a new permission that users
        can be added to
        """
        try:
            perm_set = self.permissions[perm_name]
        except KeyError:
            self.permissions[perm_name] = set()
        else:
            raise PermissionError("Permission Exists")

    def permit_user(self, perm_name, username):
        """
        Grant the given permission to the user
        """
        try:
            perm_set = self.permissions[perm_name]
        except KeyError:
            raise PermissionError("Permission does not exist")
        else:
            if username not in self.authenticator.users:
                raise InvalidUsername(username)
            perm_set.add(username)

    def check_permission(self, perm_name, username):
        """
        Check whether a user has a specific permission or not.
        In order for them to be granted access, they have to be both 
        logged into the authenticator and in the set of people who 
        have been granted access to that privilege.
        If either of these conditions is unsatisfied, an exception is raised.
        """
        if not self.authenticator.is_logged_in(username):
            raise NotLoggedInError(username)
        try:
            perm_set = self.permissions[perm_name]
        except KeyError:
            raise PermissionError("Permission does not exist")
        else:
            if username not in perm_set:
                raise NotPermittedError(username)
            else:
                return True