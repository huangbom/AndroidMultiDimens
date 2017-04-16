import os

values = {
    'values': 1,
    'values-sw360dp': 1.125,
    'values-sw480dp': 1.5,
    'values-sw600dp': 1.875,
    'values-sw720dp': 2.25
}

min_size = 1;
max_size = 700;

dimen_str = '    <dimen name="size_%s">%sdp</dimen>'

file_name = 'dimens.xml'


def join(path,paths):
    return os.path.join(path,paths);


def create_dimen_dir(path,dimen):
    dimenDir = join(path,dimen)
    if os.path.exists(dimenDir):
        print('exists dir :'+ dimenDir)
    else:
        os.mkdir(dimenDir)
        print('mkdir:' + dimenDir)
    return dimenDir;

def create_dimen_file(dir,density):
    filePath = join(dir,file_name)
    with open(filePath, 'w', encoding='utf-8') as f:
        print('mk file:'+filePath)

        f.write('<?xml version="1.0" encoding="utf-8"?>' + '\n')
        f.write('<resources>' + '\n')
        for value in range(min_size,max_size):
            f.write((dimen_str % (value,value*density)) + '\n')
        f.write('</resources>' + '\n')


# start in here
abspath = os.path.abspath('.')
multiDir = join(abspath, 'multi_dimens')
print("current dir:" + abspath)

if not os.path.exists(multiDir):
        os.mkdir(multiDir)
            
print("mkdir:"+ multiDir)

for k, v in values.items():
    dimenDir = create_dimen_dir(multiDir,k)
    create_dimen_file(dimenDir,v)


# os.mkdir create a dir

#<dimen name="size_105">118dp</dimen>
#<?xml version="1.0" encoding="utf-8"?>
#<resources>
#</resources>
#values-sw360dp 1.125
#values-sw480dp 1.5
#values-sw600dp 1.875
#values-sw720dp 2.25
