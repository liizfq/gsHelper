import copy

import yaml
from mojo import uninit,YamlFileException

class Configuration():
    def __init__(self,filepath):
        self.filepath=filepath
        self.__conf=uninit
        self.isInit=True


    def getConf(self):
        if not self.isInit:
            print("配置文件未成功加载")
            return uninit
        if self.__conf == uninit:
            self.__conf = self.loadConf()
        else:
            pass
        try:
            Configuration.check_conf(self.__conf)
        except YamlFileException:
            self.isInit=False
            print("配置文件不可用，启动扫描模式")
            self.__conf=uninit
        else:
            if self.__conf == None:
                self.__conf=uninit
                print("conf参数为None，启动扫描模式")
        return self.__conf


    # def get(self):
    #     self.getConf()

    def get(self,name,default=uninit):
        print("父类Configuration未定义get方法")
        return default

    @staticmethod
    def check_conf( conf):
        if conf==uninit:
            raise YamlFileException("conf为uninit")
        if type(conf)!=type({}):
            raise YamlFileException("conf参数的格式不正确")
        # if conf == []:
        #     raise YamlFileException("yaml文件读取的值为空值[]")
        if conf == None:
            raise YamlFileException("yaml文件读取的值为None")
        c=copy.copy(conf)
        for i in c:
            try:
                if i==None or c[i]:
                    pass
            except Exception:
                print("========point.yml中 %s 错误值=========="%(i))
                conf.pop(i)

    # @staticmethod
    # def check_conf( conf):
    #     if conf==uninit:
    #         raise YamlFileException("conf为uninit")
    #     if type(conf)!=type({}):
    #         raise YamlFileException("conf参数的格式不正确")
    #     if conf == {}:
    #         raise YamlFileException("yaml文件读取的值为空值{}")
    #     for c in conf:
    #         if c == None:
    #             raise YamlFileException("yaml文件读取的值为空")
    #         elif type(c) == type({}):
    #             Configuration.check_conf( c)
    #         elif c == []:
    #             raise YamlFileException("yaml文件读取的值为空值[]")
    #         else:
    #             pass

    def updateConf(self,name,conf):
        if conf==None:
            raise Exception("conf不能为None")
        if self.__conf==uninit or self.__conf==None:
            self.__conf={}
        self.isInit=True
        self.__conf[name]=conf


    def loadConf(self):
        with open(self.filepath, "r", encoding='utf-8') as f:
            return yaml.safe_load(f.read())

    def writeConf(self):
        with open(self.filepath, "w", encoding='utf-8') as f:
            yaml.safe_dump(data=self.__conf, stream=f, allow_unicode=True)


class PointConf(Configuration):
    def __init__(self,filepath):
        Configuration.__init__(self,filepath)

    def get(self,name,default=uninit):

        c=self.getConf()
        val=c.get(name,default)
        if val!=default:
            x,y=(val[0],val[1])
            return (x,y)
        return default

class TextConf(Configuration):
    def __init__(self, filepath):
        Configuration.__init__(self,filepath)

    def get(self, name, default=uninit):
        c = self.getConf()
        val = c.get(name, default)
        if val != default:
            left, top,right,bot = (val[0],val[1],val[2],val[3])
            return (left, top,right,bot)
        return default


point_conf = PointConf("config/point.yml")
text_conf = TextConf("config/picText.yml")