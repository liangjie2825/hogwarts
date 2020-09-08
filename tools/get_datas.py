import yaml

class GetDatas():
    def __init__(self,filepath,encode):
        self.filepath = filepath
        self.encode = encode
    def get_datas(self):
        with open(self.filepath,encoding=self.encode) as f:
           datas = yaml.safe_load(f)
           #获取注册用户时的数据
           registrydatas = datas['registry']['datas']
           registryids = datas['registry']['ids']
           #获取用户登录时的数据
           logindatas = datas['login']['datas']
           loginids = datas['login']['ids']
           #获取企业认证数据
           authdatas = datas['authentication']['data']
           authids = datas['authentication']['ids']
           return [registrydatas,registryids,logindatas,loginids,authdatas,authids]