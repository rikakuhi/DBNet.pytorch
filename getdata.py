import os


def get_images(img_path):
    '''
    find image files in data path
    :return: list of files found
    '''
    files = []
    exts = ['jpg', 'png', 'jpeg', 'JPG', 'PNG']
    for parent, dirnames, filenames in os.walk(img_path):
        for filename in filenames:
            for ext in exts:
                if filename.endswith(ext):
                    files.append(os.path.join(parent, filename))
                    break
    print('Find {} images'.format(len(files)))
    return sorted(files)


def get_txts(txt_path):
    '''
    find gt files in data path
    :return: list of files found
    '''
    files = []
    exts = ['txt']
    for parent, dirnames, filenames in os.walk(txt_path):
        for filename in filenames:
            for ext in exts:
                if filename.endswith(ext):
                    files.append(os.path.join(parent, filename))
                    break
    print('Find {} txts'.format(len(files)))
    return sorted(files)


if __name__ == '__main__':
    import json

    img_train_path = './datasets/train/img'
    img_test_path = './datasets/test/img'
    train_files = get_images(img_train_path)
    test_files = get_images(img_test_path)

    txt_train_path = './datasets/train/gt'
    txt_test_path = './datasets/test/gt'
    train_txts = get_txts(txt_train_path)
    test_txts = get_txts(txt_test_path)
    n_train = len(train_files)
    n_test = len(test_files)
    assert len(train_files) == len(train_txts) and len(test_files) == len(test_txts)
    # with open('train.txt', 'w') as f:
    with open('./datasets/train.txt', 'w') as f:
        for i in range(n_train):
            line = train_files[i] + '\t' + train_txts[i] + '\n'
            f.write(line)
    with open('./datasets/test.txt', 'w') as f:
        for i in range(n_test):
            line = test_files[i] + '\t' + test_txts[i] + '\n'
            f.write(line)
