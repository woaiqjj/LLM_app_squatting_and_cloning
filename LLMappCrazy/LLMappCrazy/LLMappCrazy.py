import deformation_method
from optparse import OptionParser
import csv  # 导入CSV库

# 使用命令python llmappcrazy.py --appname "ExampleAppName" --file "output.csv"

if __name__ == "__main__":
    usage = "usage:%prog [options] arg"
    parser = OptionParser()
    parser.add_option("-a", "--appname",action="store", type="string",dest="appname", default=False, help="appname deformation")
    # parser.add_option("-p", "--packagename", action="store", type="string",dest="packagename", default=False, help="packagename deformation")
    parser.add_option("-f", "--file", action="store", type="string", dest="filename", default=False, help="write results to filename.csv")
    options,args = parser.parse_args()

    p_result_dic = {}
    A_result_dic = {}
    # if options.packagename is not False:
    #     p_variants = deformation_method.DeformationMethod(options.packagename.lower())
    #     p_variants.packagename_deformation()
    #     p_result_dic = p_variants.variant_dic

    if options.appname is not False:
        # A_variants = deformation_method.DeformationMethod(options.appname.lower())
        A_variants = deformation_method.DeformationMethod(options.appname)
        A_variants.appname_deformation()
        A_result_dic = A_variants.variant_dic

    if options.filename is False:
        print("AppCrazy Deformation Result")
        print("ori_appname:%20s"%options.appname)
        print("ori_packagename:%10s"%options.packagename)
        print("")
        print("Squatting Generation Models %20s"%("Squatting Name"))
        print("- - - - - - - - - - - - - - - - - - - - - - - - - - -")
        for key,value in A_result_dic.items():
            print("%s %s"%(value.ljust(40),key))
        for key,value in p_result_dic.items():
            print("%s %s"%(value.ljust(40),key))
    else:
        # 使用CSV写入
        with open(options.filename, mode='w', newline='', encoding='utf-8') as file:
            csv_writer = csv.writer(file)
            csv_writer.writerow(['Squatting Name', 'Variant'])
            for key, value in A_result_dic.items():
                csv_writer.writerow([value, key])
            for key, value in p_result_dic.items():
                csv_writer.writerow([value, key])
