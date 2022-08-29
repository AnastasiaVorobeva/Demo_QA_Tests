def print_fuction_args(func):
    for arg in func:
        print('Имя функции: ', arg.__name__.capitalize().replace('_', ' '))
        args_function = list(arg.__code__.co_varnames)
        print('Аргументы функции: ', end = '')
        print(*args_function, sep=", ")


def open_browser(browser_name):
    pass


def go_to_companyname_homepage(page_url):
    pass


def find_registration_button_on_login_page(page_url, button_text):
    pass


functions = [open_browser, go_to_companyname_homepage, find_registration_button_on_login_page]

print_fuction_args(functions)