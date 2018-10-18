class HtmlWriter:
    def __init__(self, filename, width):
        self.filename = filename
        self.width = width
        self.text = ''

    def add_simle_line(self, content):
        if self.text == '':
            self.text = '<table border="1" width="100%">\n'
        self.text += '<tr>\n<td colspan=' + str(self.width) + '">' + content + '</td>\n</tr>\n'

    def add_file_arr(self, content):
        self.text += '<tr>\n'
        for cell in content:
            self.text += '<td>' + str(cell) + '</td>\n'
        self.text += '</tr>\n'

    def write(self):
        file_handler = open(self.filename, 'w')
        file_handler.write(self.text)
        file_handler.close()

    def close(self):
        file_handler = open(self.filename, 'a')
        file_handler.write('</table>')
        file_handler.close()
