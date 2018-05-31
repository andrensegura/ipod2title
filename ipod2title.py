from tinytag import TinyTag
import glob, os, sys

def name_file_by_title(dir):
    if not os.path.exists(dir + "/titled"):
        os.makedirs(dir + "/titled")

    errors = []
    for file in glob.glob(dir + '/**/*.*', recursive=True):
        name, ext = os.path.splitext(file)
        try:
            tags = TinyTag.get(file)
            title = (tags.title).replace(' ', '_') + ext
            title = title.replace('/', '-')
            newdir = dir + "/titled/" + title
            os.rename(file, newdir )
            print("-- Renamed: {} --> {}".format(file, newdir))
        except Exception as e:
            errors.append((file, e))

    if errors:
        print("\nCOULD NOT RENAME THE FOLLOWING FILES:")
        for e in errors:
            print(" - {}\n{}\n".format(e[0], e[1]))

if __name__ == "__main__":
    try:
        name_file_by_title(sys.argv[1])
    except IndexError:
        print("Usage examples:\n  python ipod2title.py /path/to/Music\n  python ipod2title.py C:\\Path\\to\\Music")
