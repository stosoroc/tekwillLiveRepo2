from lesson_21_homework.solutions.ex_2.CurrencyConverter import CurrencyConverter


def main():
    conv_service = CurrencyConverter.initialize_conv_service(
        'C:\\Users\\mariu\\PycharmProjects\\tekwillLiveRepo2\\lesson_21_homework\\conversion_rates.json', 'MDL')
    while True:
        result = CurrencyConverter.handle_user_io(conv_service)
        if not result:
            break


main()
