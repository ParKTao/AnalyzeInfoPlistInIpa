import os
from io import BytesIO
from builtins import print
import zipfile, plistlib, sys, re
debug = True
'''获取主infoplist与额外的infoplist'''
def analyze_ipamainplist_with_plistlib(ipa_path,otherInfoPlist_name):
    ipa_file = zipfile.ZipFile(ipa_path)
    plist_path = find_plist_path(ipa_file ,'Info.plist')
    print('plist_path = '+plist_path)
    if plist_path is not None:
        outputplist(ipa_file, plist_path)
    else:
        print('Can not find the info.plist')

    if otherInfoPlist_name is not None:
        otherplist_path = find_plist_path(ipa_file,otherInfoPlist_name)
        if otherplist_path is not None:
            outputplist(ipa_file, otherplist_path)
        else:
            print('Can not find the '+otherInfoPlist_path)



def find_plist_path(zip_file,infolist_path):
    name_list = zip_file.namelist()
    pattern = re.compile(r'Payload/[^/]*.app/'+infolist_path)
    for path in name_list:
        m = pattern.match(path)
        if m is not None:
            return m.group()

def write_infoplist(plist_root,plist_path):
    infoPlistName = os.path.basename(plist_path)
    newinfoplist = open(workSpace+'/'+infoPlistName,'w')
    fp = BytesIO()
    plistlib.dump(plist_root,fp)
    if debug :
        print('fp = ', (fp.getvalue()).decode('utf-8'))

    newinfoplist.write((fp.getvalue()).decode('utf-8'))
    newinfoplist.close


'''将ipa中plist输出到文件中'''
def outputplist(ipa_file, plist_path):
    plist_data = ipa_file.read(plist_path)
    plist_root = plistlib.loads(plist_data)
    write_infoplist(plist_root,plist_path)





'''cmd命令传入的参数'''
ipa_path = sys.argv[1]
'''相对于ipa的路径即可'''
otherInfoPlist_path = None
workSpace= os.getcwd()

if otherInfoPlist_path is None:
    print('无额外plist需要读取')

if not os.path.isdir(workSpace):
    os.makedirs(workSpace)

if os.path.isfile(ipa_path):
    analyze_ipamainplist_with_plistlib(ipa_path,otherInfoPlist_path)
else:
    print('当前路径不存在ipa包：',ipa_path)