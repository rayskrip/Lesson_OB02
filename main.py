class User():
    def __init__(self, user_id, name):
        self._user_id = user_id
        self._name = name
        self._access_level = 'user'

    def get_user_id(self):
        return self._user_id

    def get_name(self):
        return self._name

    def get_access_level(self):
        return self._access_level

    def set_name(self, name):
        self._name = name

    def __str__(self):
        return f"{self._user_id}: {self._name}, Access Level: {self._access_level}"

class Admin(User):
    def __init__(self, user_id, name):
        super().__init__(user_id, name)
        self._access_level = 'admin'
        self._user_list = []

    def __add_user(self, user):
        if isinstance(user, User):
            self._user_list.append(user)
            print(f"Пользователь {user.get_name()} добавлен.")
        else:
            print("Только объект User может быть добавлен.")

    def __remove_user(self, user_id):
        for user in self._user_list:
            if user.get_user_id() == user_id:
                self._user_list.remove(user)
                print(f"Пользователь с ID {user_id} удален.")
                return
        print(f"Пользователь с ID {user_id} не найден.")

    def manage_user(self, action, user=None, user_id=None):
        if action == 'add' and user is not None:
            self.__add_user(user)
        elif action == 'remove' and user_id is not None:
            self.__remove_user(user_id)
        else:
            print("Действие не поддерживается или отсутствуют параметры.")


    def list_users(self):
        for user in self._user_list:
            print(user)


# Пример
admin = Admin("1", "Антон")
user1 = User("2", "Маша")
user2 = User("3", "Вова")

admin.manage_user('add', user=user1)
admin.manage_user('add', user=user2)
admin.list_users()

admin.manage_user('remove', user_id="2")
admin.list_users()
