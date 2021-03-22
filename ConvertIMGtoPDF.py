from PIL import Image
import os, time

file_arr = os.listdir('.')
print("Found {} files in the directoy. Will process only jpg, png and jped files".format(len(file_arr)))

for fi in file_arr:
    print(">> Next File : {}".format(os.path.basename(fi)))
    if (os.path.isfile(fi)) and (os.path.basename(fi).split('.')[1]) in ('jpg','png','jpeg'):
        print(">>>> Processing files : {}".format(os.path.basename(fi)))
        image1 = Image.open(fi)
        im1 = image1.convert('RGB')
        if im1.width>800:
            im1 = im1.resize((800,int(im1.height/(im1.width/800))),resample=Image.LANCZOS)
            print("New Size Height {} Width {}".format(im1.height,im1.width))
        elif im1.width<300:
            im1 = im1.resize((im1.width+300,int(im1.height/(im1.width/(im1.width+300)))),resample=Image.LANCZOS)
            print("New Size Height {} Width {}".format(im1.height,im1.width))
        fi_op = ((os.path.basename(fi)).split('.')[0]) + ".pdf"
        print(">>>> Creating PDF : {}".format(fi_op))
        im1.save(fi_op, resolution=96)

print("All files processed. Closing in 5 seconds.")
time.sleep(5)
