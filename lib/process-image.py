from PIL import Image, ExifTags, ImageFilter
import sys, getopt

pre_path = "../pre-proc"
post_path = "../post-proc"

options = dict(
    Sharpen = True,
    Center = True,
    MaxSize = 1024
)

def process_image(input_file, output_file):
    with Image.open(input_file) as im:

        # crop
        cropped = square_crop(im)
        # resize
        cropped = cropped.resize((options['MaxSize'], options['MaxSize']))
        # save
        cropped.save(output_file)
        # report
        print(f'input: {input_file} h:{im.size[1]}px x w:{im.size[0]}px')
        print(f'output: {output_file} h:{cropped.size[1]}px x w:{cropped.size[0]}px')

        # cropped.show()

# asbtract this differently later
def square_crop(img):
    # orient the imgage as per the EXIF
    for orientation in ExifTags.TAGS.keys():
        if ExifTags.TAGS[orientation]=='Orientation':
            break
    
    exif = img._getexif()

    if exif[orientation] == 3:
        img = img.rotate(180, expand=True)
    elif exif[orientation] == 6:
        img = img.rotate(270, expand=True)
    elif exif[orientation] == 8:
        img = img.rotate(90, expand=True)

    width, height = img.size   # Get dimensions
    new_edge_length = min(width, height)

    left = (width - new_edge_length)/2
    top = (height - new_edge_length)/2
    right = (width + new_edge_length)/2
    bottom = (height + new_edge_length)/2

    # sharpen
    if options['Sharpen']:
        img = img.filter(ImageFilter.SHARPEN)

    # Crop the center of the image and return that
    return img.crop((left, top, right, bottom))

def main(argv):
    input_file = ''
    output_file = ''
    opts, args = getopt.getopt(argv,"hi:o:",["ifile=","ofile="])
    for opt, arg in opts:
        if opt == '-h':
            print (f'usage: {sys.argv[0]} -i <inputfile> -o <outputfile>')
            sys.exit()
        elif opt in ("-i", "--ifile"):
            input_file = arg
        elif opt in ("-o", "--ofile"):
            output_file = arg

    if input_file == '':
        print('No input file specified, exiting')
        print (f'usage: {sys.argv[0]} -i <inputfile> -o <outputfile>')
        sys.exit()

    if output_file == '':
        print('No output file specified, exiting')
        print (f'usage: {sys.argv[0]} -i <inputfile> -o <outputfile>')
        sys.exit()

    process_image(input_file, output_file)

if __name__ == "__main__":
    main(sys.argv[1:])
    