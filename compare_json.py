'''
# 主旨
 - jsonのファイル比較
# 機能
 - 指定ディレクトリから全jsonファイルを取得
 - 取得したファイルを比較
  -- ファイル群の中で単一の項目（ちょっとした内容の変更も全部記入する）
  -- ファイル群のすべての項目（ちょっとした内容の変更も全部記入する）
'''
import json
import os
import glob

class compare_json():

    ###################################
    ### 初期化関数
    ###################################
    def __init__(self, *args, **kwargs):
        self.get_json_files(os.path.dirname(os.path.abspath(__file__)))
        self.all_data = []
        self.only_data = []

    ###################################
    ### jsonファイルがあるディレクトリの場所
    ### を指定する。
    ###################################
    def get_json_files(self,dir_path):
        self.files = glob.glob(os.path.join(dir_path,'*.json'))

    ###################################
    ### 全てのファイルから全ての項目を取得(重複は削除)
    ###################################
    def compare_get_all(self,opt = 'None'):
        for json_file_path in self.files:
            json_file = open(json_file_path,'r')
            if opt == 'all' or opt == 'None':
                self.all_data = self.create_all_file(json_file)
            elif opt == 'only':
                self.only_data = self.create_only_file(json_file)

    ###################################
    ### 全ファイルを集めたファイルの作成
    ###################################
    def create_all_file(self,json_files):
        all_file = self.all_data
        for file in json.load(json_files):
            if file in all_file:
                pass
            else:
                all_file.append(file)
        return all_file

    ###################################
    ### １ファイルにしかなかったデータファイルの作成
    ###################################
    def create_only_file(self,json_files):
        only_files = self.only_data
        suffer_files = []
        for file in json.load(json_files):
            if file in only_files:
                only_files.remove(file)
                suffer_files.append(file)
            elif file in suffer_files:
                pass
            else:
                only_files.append(file)
        return only_files




if __name__ == '__main__':
    comp_json = compare_json()
    # comp_json.dir_path = 'file_dir'
    
    comp_json.compare_get_all(opt='all')
    print(comp_json.all_data)

    print('----------------------------')

    comp_json.compare_get_all(opt='only')
    print(comp_json.only_data)
