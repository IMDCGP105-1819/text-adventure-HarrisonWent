class TextCorrection:

    def filter_string(input_string):
        input_string = input_string.lower()
        input_string = input_string.replace('\n', '').replace('\r', '')
        input_string = input_string.replace(' ', "")
        return input_string


    def clean_string(input_string):
        input_string = TextCorrection.filter_string(input_string)

        punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
        temp = ""

        for char in input_string:
            if char not in punctuations:
                temp = temp + char

        input_string = temp
        return input_string


    def create_list(input_string):
        input_string = TextCorrection.filter_string(input_string)
        stripped_input = input_string
        return stripped_input.split(",")
