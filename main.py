from ArgParser import ArgParser
import spellcheck


def main():
    args = ArgParser().parse_args()

    inp = args.input
    out = args.output
    lang = args.lang
    create = args.create

    try:
        link = get_link(lang)
        opt = 'load'
        s = spellcheck.Spellchecker(link, opt, lang)
    except UnboundLocalError:
        file = create
        opt = 'create'
        s = spellcheck.Spellchecker(file, opt, opt)

    if inp == 'console':
        text = input('enter your text: ')
    else:
        with open(inp, 'r') as f:
            text = f.read()

    w = spellcheck.Writer(text, s, out, inp)
    w.write_corrected_text()

    print('\n')
    print('done!')
    print('thank you for using spellchecker')


def get_link(lang):
    if lang == 'eng':
        link = 'https://drive.google.com/' \
               'uc?export=download&id=1lbYlUr5QOaPdi4rqvHVt7eIk601cnX6K'
    elif lang == 'test_eng':
        link = 'https://drive.google.com/' \
               'uc?export=download&id=1oHIU8fYI3ZxIqB1ZhmdGEr6rkqQE1nZx'
    elif lang == 'test_rus':
        link = 'https://drive.google.com/' \
               'uc?export=download&id=1vtGbi9ozjV7nWDXHleS_ilTv7bsrpcif'
    elif lang == 'rus':
        link = 'https://drive.google.com/' \
               'uc?export=download&id=1dNmTiVbc0YQp_LGnCMM7vFzA7XSVODMH'
    elif lang == 'created':
        link = input('enter link for creating dictionary: ')
    return link


if __name__ == '__main__':
    main()
