from HtmlWriter import HtmlWriter
from DbWriter import DbWriter


def main():
    html_writer = HtmlWriter('file.html', 4)
    db_writer = DbWriter('spacey_db1.sl3')
    db_writer.write_in_html(html_writer, "flights")

if __name__ == "__main__":
    main()
