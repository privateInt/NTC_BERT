def read_text(fn):
    with open(fn, 'rt',encoding='UTF8') as f:
        lines = f.readlines()

        labels, texts = [], []
        for line in lines:
            if line.strip() != '':
                # The file should have tab delimited two columns.
                # First column indicates label field,
                # and second column indicates text field.
                label, text = line.strip().split('\t')
                labels += [label]
                texts += [text]

    return labels, texts
