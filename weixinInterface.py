# -*- coding:utf-8 -*-
import hashlib
import web
import lxml
import time 
import os
import urllib2,json
from lxml import etree
import pylibmc
from django.utils.encoding import smart_str, smart_unicode 
import re
from random import choice



class WeixinInterface:
    
    def __init__(self):
        self.app_root = os.path.dirname(__file__)
        self.templates_root = os.path.join(self.app_root,'templates')
        self.render = web.template.render(self.templates_root)
        
    def GET(self):
        #获得输入参数
        data = web.input()
        signature=data.signature
        timestamp=data.timestamp
        nonce=data.nonce
        echostr=data.echostr
        #自己的token
        token="tftwechat"
        #字典序排序
        list=[token,timestamp,nonce]
        list.sort()
        sha1=hashlib.sha1()
        map(sha1.update,list)
        hashcode=sha1.hexdigest()
        #sha1加密算法 
        
        #如果是来自微信的请求，则回复echostr
        if hashcode == signature:
            return echostr
        
    def POST(self):
        str_xml = web.data() #获得post来的数据
        xml = etree.fromstring(str_xml) #进行XML解析
        #content = xml.find("Content").text #获得用户所输入的内容
        msgType = xml.find("MsgType").text 
        fromUser = xml.find("FromUserName").text
        toUser = xml.find("ToUserName").text
        mc = pylibmc.Client() #初始化一个memcache实例用来保存用户的操作
        



        
        
        
        music_baseURL=r'http://tftwechat-tftfiles.stor.sinaapp.com/'
        mp3_suffix=r'.mp3'
        
        
        sample_list = {'AAT快速版': u'重口味~',
                       'AAT慢速版': u'小清新~',
                     }
        
        
        mp3_list = {'蓝精灵': u'摇滚版哟~',
                     '那些花儿':u'只是怀旧~',
                     'Swallowed In The Sea':u'coldplay~',
                     'WE WILL ROCK YOU':u'请一定要忍住，不要笑~',
                     'home':u'家,是可以让人放心的地方~',
                     '樱桃小丸子':u'要学跳舞，先学会走路~',
                     '突然好想你':u'五月天~',
                     '42':u'coldplay~',
                     '女儿情':u'韩寒觉得功勋老师推荐给学生的歌不错~',
                     '我爱你':u'英文版~',
                     '执着':u'许巍~',
                     'Boston':u'No one knows my name~',
                     '宝宝':u'给你爱的人~',
                     'Lose Yourself':u"Let's Rap~",             
                     }
        
        
                
        
        dict_kw_url  =  {'报名':r'http://mp.weixin.qq.com/s?__biz=MzA4NjI5MzUwOQ==&mid=200334404&idx=4&sn=57f567bce5ab1a8728d3298ef957f816#rd',
                         '文书':r'http://mp.weixin.qq.com/s?__biz=MzA4NjI5MzUwOQ==&mid=200470547&idx=1&sn=a9d076bf4b7c2063eada702e573ae389#rd',
                         '素材':r'http://mp.weixin.qq.com/s?__biz=MzA4NjI5MzUwOQ==&mid=200423173&idx=1&sn=e5923697538e53524c1528e61e4d9cd8#rd',
                         '林书豪':r'http://mp.weixin.qq.com/s?__biz=MzA4NjI5MzUwOQ==&mid=200310584&idx=1&sn=177d5707ee733611a36cf5072b563b3a#rd',
                         '歌手比较':r'http://mp.weixin.qq.com/s?__biz=MzA4NjI5MzUwOQ==&mid=200259703&idx=1&sn=dfcd529bd6e7c6cf07ad073a81cce0be#rd',
                         '工作vs社交':r'http://mp.weixin.qq.com/s?__biz=MzA4NjI5MzUwOQ==&mid=200207365&idx=1&sn=2270b1613f8627d5b6637f802e03a220#rd',
                         '开朗':r'http://mp.weixin.qq.com/s?__biz=MzA4NjI5MzUwOQ==&mid=200203324&idx=1&sn=b8b90315c9c0e7aee66527f28bf844a3#rd',
                         '乔布斯':r'http://mp.weixin.qq.com/s?__biz=MzA4NjI5MzUwOQ==&mid=200165755&idx=1&sn=e1c391f90b62d07017dc017d2de7aebb#rd',
                         '奥巴马':r'http://mp.weixin.qq.com/s?__biz=MzA4NjI5MzUwOQ==&mid=200172902&idx=1&sn=cb722d479a9ab264e379799c03a3f61b#rd',
                         '学外语':r'http://mp.weixin.qq.com/s?__biz=MzA4NjI5MzUwOQ==&mid=200159844&idx=1&sn=b3318b861f5ea610c64745c3974e41c9#rd',
                         '泰勒斯威夫特':r'http://mp.weixin.qq.com/s?__biz=MzA4NjI5MzUwOQ==&mid=200163564&idx=1&sn=83ffa61dd62cbe5a7bf8f9fe9a39655f#rd',
                         '建筑':r'http://mp.weixin.qq.com/s?__biz=MzA4NjI5MzUwOQ==&mid=200099882&idx=1&sn=1e174f79074dc86ad5979bef7f221b0c#rd',
                         '海岛':r'http://mp.weixin.qq.com/s?__biz=MzA4NjI5MzUwOQ==&mid=200108442&idx=1&sn=5c17188267cb6312e607d378e7623d8c#rd',
                         '餐厅':r'http://mp.weixin.qq.com/s?__biz=MzA4NjI5MzUwOQ==&mid=200092232&idx=1&sn=66895d345e7ff52bbd6193fb409f3e44#rd',
                         '地铁':r'http://mp.weixin.qq.com/s?__biz=MzA4NjI5MzUwOQ==&mid=200094460&idx=1&sn=bf22f0f3fc37d8b48a44b89c3058d612#rd',
                         '足球':r'http://mp.weixin.qq.com/s?__biz=MzA4NjI5MzUwOQ==&mid=200084000&idx=1&sn=d5355a2a91f6226f2f5b82685aa0418c#rd',
                         '饺子':r'http://mp.weixin.qq.com/s?__biz=MzA4NjI5MzUwOQ==&mid=200085982&idx=1&sn=dc8ab9ab695564c5e27a10b1b92ecb76#rd',
                         '节日':r'http://mp.weixin.qq.com/mp/appmsg/show?__biz=MzA4NjI5MzUwOQ==&appmsgid=200074386&itemidx=1&sign=5d64af72e8fc308897cd4141bb941067#wechat_redirect',
                         '蒙娜丽莎':r'http://mp.weixin.qq.com/mp/appmsg/show?__biz=MzA4NjI5MzUwOQ==&appmsgid=200077559&itemidx=1&sign=59c8860ef6c6739acd8894d443996135#wechat_redirect',
                         '母亲':r'http://mp.weixin.qq.com/s?__biz=MzA4NjI5MzUwOQ==&mid=200069057&idx=1&sn=e52934595b7859d01ace8582f0191686#rd',
                         '诚信':r'http://mp.weixin.qq.com/s?__biz=MzA4NjI5MzUwOQ==&mid=200060369&idx=1&sn=c772ef23db45e1dcdc51fadea60660a9#rd',
                         '烹饪':r'http://mp.weixin.qq.com/s?__biz=MzA4NjI5MzUwOQ==&mid=200065474&idx=1&sn=dffdfb4a6cab480375128117fa83f68f#rd',
                         '自信':r'http://mp.weixin.qq.com/s?__biz=MzA4NjI5MzUwOQ==&mid=200184081&idx=1&sn=1d77597165f5602911489464ad5586f1#rd',
                         '阿黛尔':r'http://mp.weixin.qq.com/s?__biz=MzA4NjI5MzUwOQ==&mid=200058701&idx=1&sn=e835da3a3edd73b5c86fe2f12160b8d6#rd',
                         '哈利波特':r'http://mp.weixin.qq.com/s?__biz=MzA4NjI5MzUwOQ==&mid=200056528&idx=1&sn=4cdeef836e2f9c01c152c4473f2d5210#rd',
                         '歌手':r'http://mp.weixin.qq.com/s?__biz=MzA4NjI5MzUwOQ==&mid=200112239&idx=1&sn=ec40866fdff8e95de87767eecc545e00#rd',
                         '北京':r'http://mp.weixin.qq.com/s?__biz=MzA4NjI5MzUwOQ==&mid=200474933&idx=1&sn=38eb9ff037e536ae65a454a7cf6ba339#rd',
                         '语言':r'http://mp.weixin.qq.com/s?__biz=MzA4NjI5MzUwOQ==&mid=200472660&idx=1&sn=6998769ce975806eca4d9691040e5203#rd',
                         'beijing':r'http://mp.weixin.qq.com/s?__biz=MzA4NjI5MzUwOQ==&mid=200474933&idx=1&sn=38eb9ff037e536ae65a454a7cf6ba339#rd',
                         '足球足球':r'http://mp.weixin.qq.com/s?__biz=MzA4NjI5MzUwOQ==&mid=200480498&idx=1&sn=42c6a0a5f27c94ba841256eaf5802b7f#rd',
                         '小组阿黛尔':r'http://mp.weixin.qq.com/s?__biz=MzA4NjI5MzUwOQ==&mid=200484394&idx=1&sn=e693e2b22374e269bb9c08ae211a8637#rd',
                         '火车':r'http://mp.weixin.qq.com/s?__biz=MzA4NjI5MzUwOQ==&mid=200488318&idx=1&sn=d839fdc0ff475bc3e0b55966e3ed256f#rd',
                         '唱歌':r'http://mp.weixin.qq.com/s?__biz=MzA4NjI5MzUwOQ==&mid=200493244&idx=1&sn=fd6bca3af09fa611d8f3c6ff4324c647#rd',
                         '开明':r'http://mp.weixin.qq.com/s?__biz=MzA4NjI5MzUwOQ==&mid=200496087&idx=1&sn=375db9f5ddf1db4a9f6d7457cf31695f#rd',
                         '小组节日':r'http://mp.weixin.qq.com/s?__biz=MzA4NjI5MzUwOQ==&mid=200505640&idx=1&sn=afe686a05a561ec7c95f2dcfa69f1425#rd',
                         '小组艺术':r'http://mp.weixin.qq.com/s?__biz=MzA4NjI5MzUwOQ==&mid=200509253&idx=1&sn=a994a45c0f085635c8623dfef029d8b4#rd',
                         '兰迪教授':r'http://mp.weixin.qq.com/s?__biz=MzA4NjI5MzUwOQ==&mid=200513033&idx=1&sn=b69f4cfacbe2976c6da782637dc0103d#rd',
                         }

        
        menuText = u'''感谢您关注功勋老师的留学分享，我们会定期为大家分享美式纯正口语素材，让大家摆脱中式英语的苦恼，同时也会为大家分享很多留学经验哦 ~ 作为一个码农，我们的公众号当然会比大多数的公众号智能一些咯，不信就回复下面的关键字试试吧~
【1】回复“素材”就能看到往期所有口语素材的关键词列表咯~
【2】回复“文章”就可以看到我们收录的原创和推荐的文章哦~
【3】回复“小组“快来看看大家是怎么说“Thirsty For Thirty口语锻造小组”的吧~
【4】回复“文书”快看看小组最专业的文书服务吧~
【5】回复“dict” 我就会变成一个活字典哦，快来查我吧~
【6】回复“flirt” 就会进入调戏勋哥模式，来嘛来嘛~
【7】回复“music” 就会随机播放一首我推荐的歌曲哦~
【8】回复“help”回到本菜单~
加入“Thirsty for Thirty 口语交流群”，获得更多资料和帮助，群号：342708120, 感谢大家的关注和支持~'''
        
        menuText_clip = menuText
       
        unsubscribeText=u'不嘛不嘛，嘛不嘛，不嘛，嘛。。。'
        
        inflirtText=u'您已经进入flirt调戏模式，请尽情的调戏他吧！他聪明的时候可是会讲笑话算命的哟~'
        
        indictText=u'您已经进入dict字典模式，查个词试试吧~'
        
        outflirtText=u'您已经跳出flirt调戏模式，输入help来显示操作指令吧~'
        
        outdictText=u'您已经跳出了dict字典模式，输入help来显示操作指令吧~'
        
        suffixflirtText=u'\n---------------------\n当前为flirt模式\n退出请输入quit'
        
        suffixdictText=u'\n---------------------\n当前为dict模式\n退出请输入quit'
        
        
        
        
        
        
        
        
        
        
        
        #Event Case
        if msgType == "event": # mind that it should be msgType (not mstype)
            mscontent = xml.find("Event").text
            if mscontent == "subscribe":
                return self.render.reply_text(fromUser,toUser,int(time.time()),menuText)
            if mscontent == "unsubscribe": 
                return self.render.reply_text(fromUser,toUser,int(time.time()),unsubscribeText)
        
        
        #Text Case
        if msgType == 'text':
            
            content=xml.find("Content").text
            # flirt setup
            if content.lower() == 'flirt':
                mc.set(fromUser+'_mode','flirt')
                return self.render.reply_text(fromUser,toUser,int(time.time()),inflirtText) 
            
            # dict setup
            elif content.lower() == 'dict':
                mc.set(fromUser+'_mode','dict')
                return self.render.reply_text(fromUser,toUser,int(time.time()),indictText) 
            
            # set up the mode
            mode = mc.get(fromUser+'_mode')
            
            
            
            # flirt mode
            if mode =='flirt':
                #print "enter mode:",mode
                #print "input:",content
                if content.lower() == 'quit':
                    mc.delete(fromUser+'_mode')
                    return self.render.reply_text(fromUser,toUser,int(time.time()),outflirtText)         
                else:
                    
                    res = tulingRobot(content) # 在这里输入机器人名字
                    reply_text = res['text']+suffixflirtText
                    #reply_text = res['data'][0]['text']+suffixflirtText
                    #reply_text = res['sentence_resp'] # 这里用来测试小黄鸡
                    if u'微信' in reply_text:
                        reply_text = u"勋哥脑袋出问题了，请换个问题吧~" #这里小黄鸡会有广告，我索性就全给屏蔽了
                    return self.render.reply_text(fromUser,toUser,int(time.time()),reply_text)
            
            # dict mode 
            if mode =='dict':
                if content.lower() == 'quit':
                    mc.delete(fromUser+'_mode')
                    return self.render.reply_text(fromUser,toUser,int(time.time()),outdictText)
                else:
                    if type(content).__name__ == "unicode": # 处理中文
                		content = content.encode('UTF-8')
                    Nword = youdao(content) +suffixdictText
                    return self.render.reply_text(fromUser,toUser,int(time.time()),Nword)
            
            
            # reply mode
            else: 
                if type(content).__name__ == "unicode": # 处理中文
                		content = content.encode('UTF-8')
                
                # 菜单        
            	if content.lower() == 'help':
                    return self.render.reply_text(fromUser,toUser,int(time.time()),menuText_clip)
                
                
                
                #音乐mp3
                elif mp3_list.has_key(content):
                    musicTitle = urllib2.quote(content)
                    musicDes = mp3_list[content]
                    musicURL = music_baseURL+musicTitle+mp3_suffix
                    musicTitle = content
                    return self.render.reply_music(fromUser,toUser,int(time.time()),musicTitle,musicDes,musicURL)
                    
                
                #段子MP3
                elif sample_list.has_key(content):
                    musicTitle = urllib2.quote(content)
                    musicDes = sample_list[content]
                    musicURL = music_baseURL+musicTitle+mp3_suffix
                    musicTitle = content
                    return self.render.reply_music(fromUser,toUser,int(time.time()),musicTitle,musicDes,musicURL)
                
                
                
                
                elif content.lower() == 'music':
                    keys=list(mp3_list)
                    musicTitle=choice(keys)
                    musicTitleURL = urllib2.quote(musicTitle)
                    musicDes=mp3_list[musicTitle]
                    musicURL=music_baseURL+musicTitleURL+mp3_suffix
                    return self.render.reply_music(fromUser,toUser,int(time.time()),musicTitle,musicDes,musicURL)
                
                #elif content == '1323':
                 #   musicTitle=u'女儿情'
                  #  musicDes=u'给我可爱的学生们~'
                   # musicURL=r'http://tftwechat-tftfiles.stor.sinaapp.com/%E7%AB%A5%E4%B8%BD_%E5%A5%B3%E5%84%BF%E6%83%85.mp3'
                    #return self.render.reply_music(fromUser,toUser,int(time.time()),musicTitle,musicDes,musicURL)
               #elif content.lower() == 'rain':
                #    musicTitle=u'Rainy Mood'
                 #   musicDes=u'keep calm and have fun~'
                  #  musicURL=r'http://pan.baidu.com/s/1i3zJuKl'
                   # return self.render.reply_music(fromUser,toUser,int(time.time()),musicTitle,musicDes,musicURL)
                
                
                
                #素材
                elif dict_kw_url.has_key(content):
                    url=dict_kw_url[content]
                    parsed=parseNewsUrl(url)
                    #print parsed[1]
                    return self.render.reply_news(fromUser,toUser,int(time.time()),parsed[0],parsed[1],parsed[2],parsed[3])
                
                
                #文章
                elif content=='文章':
                    url=r'http://mp.weixin.qq.com/s?__biz=MzA4NjI5MzUwOQ==&mid=200154653&idx=1&sn=85edc59a909adf3b56823aec73cfb9fa#rd'
                    parsed=parseNewsUrl(url)
                    return self.render.reply_news(fromUser,toUser,int(time.time()),parsed[0],parsed[1],parsed[2],parsed[3])
                
                
                elif content == '小组':
                    #print '小组'
                    parsed = []
                    url=[r'http://mp.weixin.qq.com/s?__biz=MzA4NjI5MzUwOQ==&mid=200334404&idx=1&sn=64e840e52585b3d539cd5de1421d5319#rd',
                         r'http://mp.weixin.qq.com/s?__biz=MzA4NjI5MzUwOQ==&mid=200334404&idx=2&sn=921908647bf115821d1e1b0759d283c7#rd',
                         r'http://mp.weixin.qq.com/s?__biz=MzA4NjI5MzUwOQ==&mid=200334404&idx=3&sn=b7681de23b778761ea99dd4d64bb0dae#rd',
                         r'http://mp.weixin.qq.com/s?__biz=MzA4NjI5MzUwOQ==&mid=200334404&idx=4&sn=57f567bce5ab1a8728d3298ef957f816#rd',
                        ]
                    
                    for j in xrange(4):
                        parsed.append(parseNewsUrl(url[j]))
                    
                    return self.render.reply_multinews(fromUser,toUser,int(time.time()),parsed)
                
                else:
                    return self.render.reply_text(fromUser,toUser,int(time.time()),menuText_clip)
                
                           

def parseNewsUrl(url):
    parsed = []
    req = urllib2.Request(url)
    urlstr = urllib2.urlopen(req).read() 
    pretitle = re.findall(r"var msg_title = \"(.+?)\";",urlstr)    
    predes = re.findall(r"var msg_desc = \"(.+?)\";",urlstr)
    prepicurl = re.findall(r"var msg_cdn_url = \"(.+?)\";",urlstr)
    title = pretitle[0].decode('UTF-8').replace('&nbsp;',' ').replace('<br/>','\n') 
    #print title
    parsed.append(title)
    description = predes[0].decode('UTF-8').replace('&nbsp;',' ').replace('<br/>','\n') 
    parsed.append(description)
    #print description
    picurl= prepicurl[0].decode('UTF-8') 
    parsed.append(picurl)
    parsed.append(url)
    return parsed

                
                
                
                
def youdao(word):
    qword = urllib2.quote(word)
    baseurl = r'http://fanyi.youdao.com/openapi.do?keyfrom=tftwechat&key=1541116392&type=data&doctype=json&version=1.1&q='
    url = baseurl+qword
    resp = urllib2.urlopen(url)
    fanyi = json.loads(resp.read())
    #根据json是否返回一个“basic”的key来判断是不是翻译成功
    if fanyi['errorCode'] == 0:    
        if 'basic' in fanyi.keys():
            trans = u'%s:\n%s\n%s\n%s\n网络释义：\n%s'%(fanyi['query'],' '.join(fanyi['translation']),''.join('/'+fanyi['basic']['phonetic']+'/'),' '.join(fanyi['basic']['explains']),' '.join(fanyi['web'][0]['value']))
            return trans
        else:
            trans =u'%s:\n基本翻译:%s\n'%(fanyi['query'],''.join(fanyi['translation']))
            return trans
    elif fanyi['errorCode'] == 20:
            return u'那个。。。你输入的东西太长了。。。'
    elif fanyi['errorCode'] == 30:
            return u'这个。。。我不知道怎么翻译诶。。。'
    elif fanyi['errorCode'] == 40:
            return u'呵呵。。。我不懂这门语言诶。。。'
    else:
            return u'呵呵。。。请检查%s的拼写。。。'% word

def tulingRobot(ask):
    ask = ask.encode('UTF-8')
    enask = urllib2.quote(ask)
    # cookie might not be used here
    baseurl = r'http://www.tuling123.com/openapi/api?key=558f57aa6802cafb055480e7a863af72&info='
    url = baseurl+enask
    #print url
    req = urllib2.Request(url)
    resp = urllib2.urlopen(req)
    reson = json.loads(resp.read())
    return reson
    
        
        
def xiaohuangji(ask):
    ask = ask.encode('UTF-8')
    enask = urllib2.quote(ask)
    send_headers = {
    'Cookie':'''
    simsimi_uid=62374867; isFirst=1; Filtering=0.0; selected_nc=ch; __utma=119922954.208332177.1405308539.1405650542.1405650542.4; __utmb=119922954.36.9.1405659126012; __utmc=119922954; __utmz=119922954.1405308539.1.1.utmcsr=(direct)|utmccn=(direct)|utmcmd=(none)     
'''}
    
    baseurl = r'http://www.simsimi.com/func/reqN?lc=zh&ft=0.0&req='
    url = baseurl+enask
    #print 'url',url
    req = urllib2.Request(url,headers=send_headers)
    #print "req",req
    resp = urllib2.urlopen(req)
    reson = json.loads(resp.read())
    return reson


        
def easyRobot(ask):
    ask = ask.encode('UTF-8')
    enask = urllib2.quote(ask)
    # cookie might not be used here
    baseurl = r'http://api.yun2d.com/robot/ask?api_robot=452&api_token=03deb0c101411e16405ef788a924d75410b98770&question='
    url = baseurl+enask
    req = urllib2.Request(url)
    resp = urllib2.urlopen(req)
    reson = json.loads(resp.read())
    return reson

        
        
        
     