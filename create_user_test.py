import sender_stand_request
import data


# эта функция меняет значения в параметре firstName
def get_user_body(first_name):
    # копирование словаря с телом запроса из файла data, чтобы не потерять данные в исходном словаре
    current_body = data.user_body.copy()
    # изменение значения в поле firstName
    current_body["firstName"] = first_name
    # возвращается новый словарь с нужным значением firstName
    return current_body


def test_create_user_2_letter_in_first_name_get_success_response():
    # В переменную user_body сохраняется обновленное тело запроса с именем “Аа”
    user_body = get_user_body("Аb")
    # В переменную user_response сохраняется результат запроса на создание пользователя
    user_response = sender_stand_request.post_new_user(user_body)
    # Проверяется, что код ответа равен 201
    assert user_response.status_code == 201
    # Проверяется, что в ответе есть поле authToken, и оно не пустое
    assert user_response.json()["authToken"] != ""


def test_create_user_2_letter_in_first_name_get_success_response():
    # В переменную user_body сохраняется обновленное тело запроса с именем “Аа”
    user_body = get_user_body("Аа")
    # В переменную user_response сохраняется результат запроса на создание пользователя
    user_response = sender_stand_request.post_new_user(user_body)
    # Проверяется, что код ответа равен 201
    assert user_response.status_code == 201
    # Проверяется, что в ответе есть поле authToken, и оно не пустое
    assert user_response.json()["authToken"] != ""
    # В переменную users_table_response сохраняется результат запрос на получение данных из таблицы user_model
    users_table_response = sender_stand_request.get_users_table()
    # Строка, которая должна быть в ответе запроса на получение данных из таблицы users
    str_user = user_body["firstName"] + "," + user_body["phone"] + "," \
               + user_body["address"] + ",,," + user_response.json()["authToken"]
    # Проверка, что такой пользователь есть, и он единственный
    assert users_table_response.text.count(str_user) == 1


def test_create_user_15_letter_in_first_name_get_success_response(): #2
    user_body = get_user_body("Aaaaaaaaaaaaaaa")
    user_response = sender_stand_request.post_new_user(user_body)
    assert user_response.status_code == 201
    assert user_response.json()["authToken"] != ""
    users_table_response = sender_stand_request.get_users_table()
    str_user = user_body["firstName"] + "," + user_body["phone"] + "," \
               + user_body["address"] + ",,," + user_response.json()["authToken"]
    assert users_table_response.text.count(str_user) == 1


def negative_assert_symbol(first_name): #3 1
    user_body = get_user_body(first_name)
    user_response = sender_stand_request.post_new_user(user_body)
    assert user_response.status_code == 400
    assert user_response.json()["code"] == 400
    assert user_response.json()["message"] == "Имя пользователя введено некорректно. " \
                                         "Имя может содержать только русские или латинские буквы, " \
                                         "длина должна быть не менее 2 и не более 15 символов"


def test_create_user_1_letter_in_first_name_get_error_response(): #3
    user_body = get_user_body("A")
    user_response = sender_stand_request.post_new_user(user_body)
    assert user_response.status_code == 400
    assert user_response.json()["code"] == 400
    assert user_response.json()["message"] == "Имя может содержать только русские и английские буквы," \
                                         "не менее 2 и не более 15 символов"


def test_create_user_1_letter_in_first_name_get_error_response(): #4
    user_body = get_user_body("Aaaaaaaaaaaaaaaa")
    user_response = sender_stand_request.post_new_user(user_body)
    assert user_response.status_code == 400
    assert user_response.json()["code"] == 400
    assert user_response.json()["message"] == "Имя может содержать только русские и английские буквы," \
                                         "не менее 2 и не более 15 символов"


def test_create_user_english_letter_in_first_name_get_success_response(): #5
    user_body = get_user_body("QWErty")
    user_response = sender_stand_request.post_new_user(user_body)
    assert user_response.status_code == 201
    assert user_response.json()["authToken"] != ""
    users_table_response = sender_stand_request.get_users_table()
    str_user = user_body["firstName"] + "," + user_body["phone"] + "," \
               + user_body["address"] + ",,," + user_response.json()["authToken"]
    assert users_table_response.text.count(str_user) == 1


def test_create_user_russian_letter_in_first_name_get_success_response(): #6
    user_body = get_user_body("Мария")
    user_response = sender_stand_request.post_new_user(user_body)
    assert user_response.status_code == 201
    assert user_response.json()["authToken"] != ""
    users_table_response = sender_stand_request.get_users_table()
    str_user = user_body["firstName"] + "," + user_body["phone"] + "," \
               + user_body["address"] + ",,," + user_response.json()["authToken"]
    assert users_table_response.text.count(str_user) == 1


def test_create_user_has_space_in_first_name_get_error_response(): #7
    user_body = get_user_body("Человек и Ко")
    user_response = sender_stand_request.post_new_user(user_body)
    assert user_response.status_code == 400
    assert response.json()["message"] == "Имя может содержать только русские и английские буквы," \
                                         "не менее 2 и не более 15 символов"


def test_create_user_has_special_symbol_in_first_name_get_error_response(): #8
    user_body = get_user_body("№%@")
    user_response = sender_stand_request.post_new_user(user_body)
    assert user_response.status_code == 400
    assert user_response.json()["message"] == "Имя может содержать только русские и английские буквы," \
                                         "не менее 2 и не более 15 символов"

def test_create_user_has_number_in_first_name_get_error_response(): #9
    user_body = get_user_body("123")
    user_response = sender_stand_request.post_new_user(user_body)
    assert user_response.status_code == 400
    assert user_response.json()["message"] == "Имя может содержать только русские и английские буквы," \
                                         "не менее 2 и не более 15 символов"


def negative_assert_no_first_name(user_body): #10 11
    user_response = sender_stand_request.post_new_user(user_body)
    assert user_response.status_code == 400
    assert user_response.json()["code"] == 400
    assert user_response.json()["message"] == "Не все необходимые параметры были переданы"


def test_create_user_no_first_name_get_error_response(): #10
        # Копируется словарь с телом запроса из файла data в переменную user_body
        # Иначе можно потерять данные из исходного словаря
        user_body = data.user_body.copy()
        # Удаление параметра firstName из запроса
        user_body.pop("firstName")
        # Проверка полученного ответа
        negative_assert_no_first_name(user_body)


# Параметр fisrtName состоит из пустой строки
def test_create_user_empty_first_name_get_error_response(): #11
    # В переменную user_body сохраняется обновлённое тело запроса
    user_body = get_user_body("")
    # Проверка полученного ответа
    negative_assert_no_first_name(user_body)


def test_create_user_number_type_first_name_get_error_response(): #12
    user_body = get_user_body(12)
    user_response = sender_stand_request.post_new_user(user_body)
    assert user_response.status_code == 400
