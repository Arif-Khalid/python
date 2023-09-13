import glob
toAdd = 'dithercrossfade'
dirname = "C:\\UnityProjects\\forestia-bel-prototype2\\Assets\\Shaders"

ext = ('.py')

for filename in glob.glob(dirname + '\\**\\*.shader', recursive=True):
    try:
        file = open(filename, 'r')
    except OSError:
        print('For shader file: ' + filename + 'an error occurred while opening the file')
        continue

    data = file.readlines()
    needToWrite = False
    for index, line in enumerate(data):
        if('#pragma surface' in line and not line.lstrip().startswith('//')):
            if(not line.rstrip().endswith('dithercrossfade')):
                data[index] = line.rstrip() + ' ' + toAdd + '\n'
                needToWrite = True
                break
    if(not needToWrite):
        continue
    print(filename)
    file = open(filename, 'w')
    file.writelines(data)