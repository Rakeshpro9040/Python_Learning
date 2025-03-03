import os
import zipfile
import shutil

os.system('cls')
# f = open('fileone.txt','w+')
# f.close()

# os.system('cls')
# f = open('filetwo.txt','w+')
# f.close()

'''------------Compress-----------------'''
# comp_file = zipfile.ZipFile('comp_file.zip','w')
# comp_file.write('fileone.txt', compress_type=zipfile.ZIP_DEFLATED)
# comp_file.write('filetwo.txt', compress_type=zipfile.ZIP_DEFLATED)
# comp_file.close()

'''------------Extract-----------------'''
# ext_file = zipfile.ZipFile('comp_file.zip','r')
# ext_file.extractall('extracted_content')

'''------------Compress: shutil-----------------'''
# print(os.getcwd())
# os.chdir('C:\\Users\\rakes\\PycharmProjects\\Python_Introduction\\Advanced Modules')
# print(os.getcwd())
# dir_to_zip = 'C:\\Users\\rakes\\PycharmProjects\\Python_Introduction\\Advanced Modules\\extracted_content'
# out_filename = 'example_compress_shu'
# shutil.make_archive(out_filename, 'zip', dir_to_zip)

'''------------Extract: shutil-----------------'''
# shutil.unpack_archive('example_compress_shu.zip', 'example_compress_shu_unzip', format='zip')