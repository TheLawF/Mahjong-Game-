#-*- coding:utf-8 -*-
# 自编麻将游戏 @The_law_F
import random as r
import pygame as p
import rules
import sys

class NumWan:
    def __init__(self):
    # 定义麻将的序数和花色
        self.printName = ['🀇','🀈','🀉','🀊','🀋','🀌','🀍','🀎','🀏'] * 4
        self.triplet = True
        self.doublet = True
        self.shunZi = True
        self.chi = False
        self.pong = False
        self.gang = False
        self.color ='萬'


class NumSuo(NumWan):
    def __init__(self):
        self.printName = ['🀐','🀑','🀒','🀓','🀔','🀕','🀖','🀗','🀘'] * 4
        self.color = '条'

class NumTong(NumWan):
    def __init__(self):
        self.printName = ['🀙','🀚','🀛','🀜','🀝','🀞','🀟','🀠','🀡'] * 4
        self.color = '筒'

class Wind(NumWan):
    def __init__(self):
        self.printName = ['🀀','🀁','🀂','🀃'] *4
        self.color = '风'

class Arrow(Wind):
    def __init__(self):
        self.printName = ['🀄','🀅','🀆'] * 4
        self.color = '箭'

class Characters(NumWan):
    def __init__(self):
        self.wind = Wind()
        self.arrow = Arrow()
        self.printName = self.wind.printName + self.arrow.printName
        self.color = '字'
        
class Mahjong:
    def __init__(self):
        self.w = NumWan()
        self.s = NumSuo()
        self.t = NumTong()
        self.c = Characters()
        self.b = Banker(3)
                        
        self.fieldWind_E = '🀀'
        self.fieldWind_S = '🀁'
        self.fieldWind_W = '🀂'
        self.fieldWind_N = '🀃'

        self.blank = []

class Banker:
    def __init__(self, double):
        self.player_name = '庄家'
        self.score = 100
        self.double = double
        # 这里写入麻将牌的代号，当输入下面这个列表里的字符串时可以出老千
        # self.ascii的数值加上列表的序列号就是麻将字符对应的ASCII码
        self.code = ['e','s','w','n','z','f','b','w1','w2','w3','w4','w5','w6','w7','w8','w9',\
                's1','s2','s3','s4','s5','s6','s7','s8','s9','t1','t2','t3','t4','t5','t6','t7','t8','t9']
        self.result = []
        self.unicode = 126976
        self.an__Gang = 0
        self.victory = False
        
        self.isBanker = True
        self.isSouth = False
        self.isWest = False
        self.isNorth = False
        self.isAI = False
        
        self.owned = []
        self.peng = []
        self.gang = []
        self.abandoned = []
        self.abandon_area = []

    def printCard(self):
        cards = open('E:\\messup\\mahjong\\'+str(self.player_name)+'.txt',mode='wt',encoding='utf-8')

        cards.write(str(self.owned)+'\n')
        cards.write(str(self.peng)+'\n')
        cards.write(str(self.gang))
        cards.close()

    def getCard(self, walls):
        ''' 这个函数是从自摸墙上摸牌的函数，没有参数，有一个返回值'''
        self.get = walls[0]
        self.owned.append(self.get)
        return self.owned

    def abandonCard(self, num, walls, rounds):
        ''' 这个函数是从手牌内弃牌的函数，没有参数和返回值'''
        
        print('第'+str(rounds)+'轮，自摸墙上剩余：'+str(len(walls))+'张')
        self.abandon_area.append(self.owned[int(num)])
        print('弃牌堆：'+str(self.abandon_area))
        del self.owned[int(num)]
        self.owned.sort()

    def gang_pai(self, wall, abandon=None):
        ''' 杠牌的三种情况：
            1. 摸到一张新牌，与自己的手牌组成四张杠牌
            2. 摸到一张新牌，与自己已有的碰牌组成四张杠牌
            3. 某家打出一张牌，与自己已有的手牌组成四张杠牌

| -------------------------------------------------------------------------------------- |
            杠牌函数的实现：

            **********************************************************************************

            1. 杠牌：

            在其余几家出牌的阶段，如果其余几家的弃牌与玩家的手牌构成四张杠牌型则会
            进行一次判断，如果玩家在此时输入g则会调用本函数，并且将其余几家的弃牌作为本函数
            参数传入。玩家的杠牌列表中会被加入一个由四张相同手牌构成的字符串，同时，玩家
            手牌中的这些牌将被移除。
            
            **********************************************************************************

            2. 加杠：

            如果游戏主循环中的玩家进张变量 banker_get 和玩家碰牌列表中的字符串构成
            杠牌牌型则会调用本函数，玩家进张 banker_get 将会作为本函数的 get 参数传入。如果
            玩家在此时输入g则会将玩家碰牌列表中的对应元素移除，然后在玩家的杠牌列表中加入
            一个由对应四张相同手牌构成的字符串。

            **********************************************************************************

            3. 暗杠：

            如果玩家的手牌中原先就存在着三张相同的刻子牌型，这个时候玩家进张变量 banker_get
            和这一副刻子构成杠牌牌型则会调用本函数，玩家进张 banker_get 将会作为本函数的
            get 参数传入。如果玩家在此时输入g则会将玩家手牌列表中的对应元素移除，然后在玩家
            的杠牌列表中加入一个由对应四张相同手牌构成的字符串。

            **********************************************************************************
           | -------------------------------------------------------------------------------------- |
'''

        if abandon != None:
            self.gang.append(abandon * 4)
            for i in range(3):
                self.owned.remove(abandon)
            print(self.owned)
            self.an__Gang = 0
            return self.an__Gang

        else:
            for each in self.peng:
                for e in each:
                    if abandon == e:
                        self.ang = input('输入g加杠，输入p或者回车跳过：')
                        if self.ang == 'g':
                            self.g = abandon * 4
                            self.gang.append(self.g)
                            for i in range(4):
                                self.owned.remove(abandon)
                            for each in self.peng:
                                if abandon == each[0]:
                                    self.peng.remove(each)
                            self.getCard(wall)
                            print(self.owned)
                            self.an__Gang = 1
                            return self.an__Gang

            for each in self.owned:
                if self.owned.count(each) == 4:
                    self.ang = input('输入g暗杠，输入p或者回车跳过：')
                    if self.ang == 'g':
                        self.an_gang = each * 4
                        self.gang.append(self.an_gang)
                        for i in range(4):
                            self.owned.remove(each)
                        self.an__Gang = 2
                        self.getCard(wall)
                        print(self.owned)
                        return self.an__Gang
                    else:
                        pass
                break

    def chi(self):
        pass

    def score_account(self, winDoub=0):
        # 0番鸡和采取的分数结算形式，算分方法为役种番数乘以得分倍数
        if winDoub == 0:
            self.score += 1 * self.double
            return True

    def cheat(self):
        """ | -------------------------------------------------------------------------------------- |
            作弊函数包含三个部分【仅用作程序员测试，正式游戏PK请勿(必)使用（doge）】
            **************************************************************************

            1. 替换玩家的单张手牌，玩家可在出牌代码提示后输入"c"进入到本函数之中，当看到 ”请
            输入你想要替换的手牌代码：“ 时可键入伪代码选择你想替换的牌 (伪代码请在self.code
            查询) 。然后，程序会提示 ”请输入你想替换的手牌序列号【0~13】：”，这个时候输入
            对应的序列号后，手牌中的原麻将字符将会被替换为新的。【注意：0~13只是最大取值，
            碰牌后手牌长度将会缩短】
            
            **************************************************************************
            
            2. 替换玩家的进张，玩家在看到 ”请输入你想要替换的手牌代码:“ 之后输入 "g" 将会
            进入本函数的另外一支中，同样输入伪代码将手牌进行替换，与第一部分不同的是，这
            一支会让鸣牌循环继续进行而不是回到开头。

            **************************************************************************
            
            3. 替换玩家的全部手牌，玩家在看到 “请输入你想要替换的手牌代码：”之后输入 “l” 将会
            进入本函数的最后一支中，输入一串以英文逗号分隔的伪代码，然后使用.split(',')方法
            以英文逗号为分隔符分隔字符串，返回列表 ls，遍历列表 ls，如果里面的每个字符串存在于
            self.code 伪代码中则将 ls中的元素全部添加至self.result列表，最后让手牌self.owned
            等于self.result 便完成了全部手牌的替换。
            | -------------------------------------------------------------------------------------- |
            """
        # 在输入self.code中的值之后，玩家的手牌将会被替换为self.unicode中对应的麻将字符
        word = input('请输入你想要替换的手牌代码：')
        if word in self.code:
            try:
                seq = eval(input('请输入你想替换的手牌序列号【0~13】：'))
                for i in range(len(self.code)):
                    if word == self.code[i]:
                        self.owned[seq] = chr(self.unicode + i) # 序列号加126976为每个麻将的Unicode码
                        print(self.owned)

            except NameError:
                print("输入不合法，不许你作弊 >_< ")
                pass

            except IndexError:
                print("数据太大了，才不会允许你作弊呢")
                pass
                    
        # 在输入self.code中的值之后，直接调用杠牌函数
        elif word == 'g':
            get_gang = input('请输入你想要替换的进张手牌代码：')
            if get_gang in self.code:
                for i in range(len(self.code)):
                    if get_gang == self.code[i]:
                        self.gang_pai(chr(self.unicode + i))

        elif word == 'l':
            string = str(input('请输入一个手牌列表，以英文逗号分隔：'))
            ls = string.split(',')

            if len(ls) != len(self.owned):  # 输入的数据需要等于原手牌长度
                print('你不能作弊！！！')
                pass
            else:
                for each in ls:
                    if each not in self.code:
                        print('你不能作弊！！！')  # 伪代码也必须是self.code内给出的那些值
                        pass

                    else:
                        self.result.append(chr((self.code.index(each) + self.unicode)))
                self.owned = self.result
                self.owned.sort()
                print(self.owned)

        else:
            pass

  
class South(Banker):
    def __init__(self):
        self.player_name = '南家'
        self.isSouth = True
        self.isAI = True
        self.peng = []
        self.gang = []
        self.abandon_area = []
        self.score = 100

class West(Banker):
    def __init__(self):
        self.player_name = '西家'
        self.isWest = True
        self.isAI = True
        self.peng = []
        self.gang = {}
        self.abandon_area = []
        self.score = 100

class North(Banker):
    def __init__(self):
        self.player_name = '北家'
        self.isNorth = True
        self.isAI = True
        self.peng = []
        self.gang = {}
        self.abandon_area = []
        self.score = 100

class Players:
    def __init__(self):
        self.banker = Banker(3)
        self.south = South()
        self.west = West()
        self.north = North()
        self.ai_dict = {"s": True, "w": True, "n": True}

        # 这里是定义门风刻的牌
        self.sideCard_E = '🀀'
        self.sideCard_S = '🀁'
        self.sideCard_W = '🀂'
        self.sideCard_N = '🀃'
        
        self.peng = []
        self.gang = {}
        self.abandon_area = []
        self.score = 100

    def is_ai(self):
        if self.south.isAI is False:
            self.ai_dict["s"] = False
        if self.west.isAI is False:
            self.ai_dict["w"] = False
        if self.north.isAI is False:
            self.ai_dict["n"] = False

def main():
    # 实例化庄家和闲家
    global south_abandon, west_abandon, north_abandon
    loop = True
    banker = Banker(3)
    south = South()
    west = West()
    north = North()
    # 实例化序数牌和字牌，调用内置列表用于随机排序
    w = NumWan()
    s = NumSuo()
    t = NumTong()
    c = Characters()
    mahjong = Mahjong()
    players = Players()
    arrange1 = w.printName
    arrange2 = s.printName
    arrange3 = t.printName
    arrange4 = c.printName
    arrange = arrange1 + arrange2 + arrange3 + arrange4

    # 游戏开始界面（程序处理端）
    print('欢迎来到全字符麻将小游戏。本游戏基于python。')
    print('作者：哔哩哔哩@定律F，bug报告邮箱：975523839@qq.com')

    # 游戏开始界面(用户图形界面端)
    """size = width, height = 1000, 600
    bg = (50, 50, 50)
    screen = p.display.set_mode(size)
    screen.fill(bg)
    p.display.set_caption("全字符麻将游戏_Ver_Unfinished-04.exe")"""

    # 游戏设置界面
    """title = 'config'
    background = (0, 0, 0)
    color = [int, int, int]
    home_pic = None
    scoring = 3"""
    
    banker.name = input('请输入东家的名字，或按回车键开始游戏：')

    # 开始洗牌配牌，庄家先手获得14张麻将牌，并按unicode码顺序排列
    r.shuffle(arrange)
    walls = arrange
    banker_card = walls[:13]
    banker_card.sort()
    banker.owned = banker_card
    banker.printCard()

    #  闲家开始配牌
    south_card = walls[13:26]
    south_card.sort()
    south.owned = south_card
    south.printCard()

    west_card = walls[26:39]
    west_card.sort()
    west.owned = west_card
    west.printCard()

    north_card = walls[39:52]
    north_card.sort()
    north.owned = north_card
    north.printCard()
    del walls[:56]
    rounds = 1

    # 这里定义庄家是否胜利的判断条件，在和牌判定的最后调用
    isWin = True

    playing = True
    while True:
        if not len(walls):
            print('第%d轮，自摸墙上剩余：%d张。游戏结束，本次流局' % (rounds,int(len(walls))))
            break

        if not playing:
            break
        # 庄家回合开始，摸得一张牌后输入0~13即可将对应位置的手牌打出（出牌循环）
        else:
            banker_get = walls[0]
            banker.owned.append(banker_get)
            banker.printCard()
            print(banker.owned)

            del walls[0]
            # 开始进入鸣牌循环，根据麻将鸣牌规则，当庄家鸣牌后将回到这一行打出一张牌
            while playing:
                # ----------------------------------------------------------------------------- #
                # 如果杠牌函数 banker.gang_pai() 存在返回值则跳出本次循环                        #
                # 如果杠牌函数 banker.gang_pai() 不存在返回值则继续执行下面的代码           #
                # ----------------------------------------------------------------------------- #
                banker.gang_pai(walls)
                if banker.gang_pai(walls):
                    print(banker.owned)
                    break

                else:
                    pass

                banker_abandon = input('庄家请出牌：')

                ''' 注意，碰牌会删除列表元素从而缩短列表的长度，所以每次碰牌后，能够输入的弃牌
            索引上限会减去3，否则程序会直接报错停止运行。
                  【即：没有碰牌时，能够输入的弃牌索引值为0~13之间的整数；碰1次牌后，索引值为
            0~10；碰2次后，索引值为0~7；碰3次后，索引值为0~4；碰四次后，索引值为0~1】'''

                # 这几段是结束游戏，宣告胜利和作弊的代码
                if banker_abandon == '/endgame':
                    playing = False
                    loop = False
                    break

                elif banker_abandon == '/win':
                    playing = False
                    owned = banker.owned
                    break

                # 如果在这里输入c则会进入"开发者模式"(迫真)
                elif banker_abandon == 'c':
                    banker.cheat()
                    continue

                '''if eval(banker_abandon) < 0 or eval(banker_abandon) > len(banker.owned):
                    print("输入有误，请确认您输入的是0~{}的整数数值".format(len(banker.owned) - 1))
                    pass
                else:
                    pass'''
                try:
                    banker.abandonCard(banker_abandon, walls, rounds)
                    banker.printCard()
                    print(banker.owned)
                    print(banker.peng)
                except:
                    print("输入有误，请确认您输入的是0~{}的整数数值".format(len(banker.owned) - 1))
                    continue

                # 由于不会写出牌机器人，所以让其余几家随缘出牌，摸到什么打什么
                if not len(walls):
                    break
                else:
                    #  如果南家是AI，那么便执行这一部分的代码，其它家同理
                    if south.isAI == True:
                        south_get = walls[0]
                        south.owned.append(south_get)
                        south.printCard()
                        del walls[0]
                        south_abandon = south.owned[13]
                        south.abandon_area.append(str(south_abandon))
                        print('南家弃牌堆：'+str(south.abandon_area))
                        peng = []

                        # 南家碰牌和杠牌判定，南家的弃牌如果在手牌内且手牌内存在与这张弃牌相同的2~3张
                        # 即触发判定。
                        if south_abandon in banker.owned and banker.owned.count(south_abandon) == 2:
                            peng = input('输入p碰牌，输入其它键跳过：')
                        elif south_abandon in banker.owned and banker.owned.count(south_abandon) >= 2:
                            peng = input('输入p碰牌，输入g杠牌，输入其它键跳过：')
                        # 以下是大多数情况下，南家在弃牌后执行的代码

                        # 南家的碰牌检测，如果南家打出碰牌则告知庄家是否鸣碰
                        if peng == 'p':
                            rem = south_abandon
                            rest = south_abandon * 3
                            banker.peng.append(rest)
                            for i in south_abandon:
                                if i == south_abandon:
                                    banker.owned.remove(i)
                            banker.owned.remove(rem)
                            banker.printCard()
                            print(banker.owned)
                            continue

                        # 南家的杠牌检测，如果南家打出杠牌则告知庄家是否鸣杠
                        elif peng == 'g':
                            banker.gang_pai(walls,abandon=south_abandon)
                            break

                        else:
                            del south.owned[13]
                            south.owned.sort()
                            south.printCard()
                            print('南家已出牌')

                    #  如果不是AI，那么进入这一部分的代码块
                    else:
                        pass

                if not len(walls):
                    break
                else:
                    # 西家的碰牌检测，和南家一样
                    west_get = walls[0]
                    west.owned.append(west_get)
                    west.printCard()
                    del walls[0]
                    west_abandon = west.owned[13]
                    west.abandon_area.append(str(west_abandon))
                    print('西家弃牌堆：'+str(west.abandon_area))
                    peng = []

                    if west_abandon in banker.owned and banker.owned.count(west_abandon) == 2:
                        peng = input('输入p碰牌，输入其它键跳过：')
                    if west_abandon in banker.owned and banker.owned.count(west_abandon) > 2:
                        peng = input('输入p碰牌，输入g杠牌，输入其它键跳过：')

                    if peng == 'p':
                        rem = west_abandon
                        rest = west_abandon * 3
                        banker.peng.append(rest)
                        for i in west_abandon:
                            if i == west_abandon:
                                banker.owned.remove(i)
                        banker.owned.remove(rem)
                        banker.printCard()
                        print(banker.owned)
                        peng = True
                        continue

                    elif peng == 'g':
                        banker.gang_pai(walls, abandon=west_abandon)
                        break

                    else:
                        del west.owned[13]
                        west.owned.sort()
                        west.printCard()
                        print('西家已出牌')

                if not len(walls):
                    break
                else:
                    north_get = walls[0]
                    north.owned.append(north_get)
                    north.printCard()
                    del walls[0]
                    north_abandon = north.owned[13]
                    north.abandon_area.append(str(north_abandon))
                    print('北家弃牌堆：'+str(north.abandon_area))
                    peng = []

                    if north_abandon in banker.owned and banker.owned.count(north_abandon) == 2:
                        peng = input('输入p碰牌，输入其它键跳过：')
                    if north_abandon in banker.owned and banker.owned.count(north_abandon) > 2:
                        peng = input('输入p碰牌，输入g杠牌，输入其它键跳过：')

                    if peng == 'p':
                        rem = north_abandon
                        rest = north_abandon * 3
                        banker.peng.append(rest)
                        for i in north_abandon:
                            if i == north_abandon:
                                banker.owned.remove(i)
                        banker.owned.remove(rem)
                        banker.printCard()
                        print(banker.owned)
                        continue

                    elif peng == 'g':
                        banker.gang_pai(walls, abandon=north_abandon)
                        break

                    else:
                        del north.owned[13]
                        north.owned.sort()
                        north.printCard()
                        print('北家已出牌')
                        break

            #  mahjong.blank.append(south.abandon_area[-1])
            #  mahjong.blank.append(west.abandon_area[-1])
            #  mahjong.blank.append(north.abandon_area[-1])
            #  print(mahjong.blank)
            rounds += 1

    # 和牌函数判定循环，先向rules模块的normal函数中传入三个列表，然后调用score_Account
    # 函数，如果返回为真跳出游戏主循环，为庄家加分，闲家扣分并显示。

    # 九莲宝灯等大牌的判定会先行生效，所有的和牌类将会在此实例化
    normal = True
    ll = rules.LotusLantern()
    ll.lotus_Lantern(banker.owned)

    # 十三幺的实例化，然后调用内置牌判定函数，下同
    ta = rules.Thirteen_Alones()
    ta.thirteen_Alones(banker.owned)

    # 大三元实例化
    gt = rules.GreatTriplets()
    gt.the_Great_Triplets(banker.owned)

    # 字一色实例化
    cc = rules.ColorCharacters()
    cc.character_Colors(banker.owned)

    banker.owned.sort()

    while True:
        if loop is True:
            # 九莲宝灯判定
            if ll.win is True:
                print("和！纯正九莲宝灯，88番!")
                banker.score += ll.score * banker.double
                south.score -= ll.score * banker.double / 3
                west.score -= ll.score * banker.double / 3
                north.score -= ll.score * banker.double / 3
                break

            if ta.win is True:
                print("和！十三幺，88番")
                banker.score += ta.score * banker.double
                south.score -= ta.score * banker.double / 3
                west.score -= ta.score * banker.double / 3
                north.score -= ta.score * banker.double / 3
                break

            # 大三元的分数结算，可以与其它番种复合，所以此处可以使用pass关键字继续
            if gt.win is True:
                print("和！大三元，88番!")
                banker.score += gt.score * banker.double
                south.score -= gt.score * banker.double / 3
                west.score -= gt.score * banker.double / 3
                north.score -= gt.score * banker.double / 3
                pass

            if cc.win is True:
                print("和！字一色，64番!")
                banker.score += cc.score * banker.double
                south.score -= cc.score * banker.double / 3
                west.score -= cc.score * banker.double / 3
                north.score -= cc.score * banker.double / 3
                pass

            # 普通的和牌判定，可以选择是否允许屁胡
            normal = rules.normal(banker.owned, banker.gang, banker.peng)
            rules.all_groups = rules.chars + rules.triplets + rules.flush + rules.doublets + rules.pengs + rules.gangs


            # 平和判定
            od = rules.Ordinary()
            od.get_ordinary()
            if od.win is True:
                banker.score += od.score * banker.double
                south.score -= od.score * banker.double / 3
                west.score -= od.score * banker.double / 3
                north.score -= od.score * banker.double / 3

            # 门前清判定
            clear = rules.Clearing()
            clear.clearing()
            if normal is True and clear.win is True:
                banker.score += clear.score * banker.double
                south.score -= clear.score * banker.double / 3
                west.score -= clear.score * banker.double / 3
                north.score -= clear.score * banker.double / 3

            # 七对判定
            sd = rules.SevenDoublets()
            sd.seven_Doublets(banker.owned)

            if len(rules.all_groups) >= 5:
                banker.score_account()
                print("屁胡，一番")
                south.score -= banker.double / 3
                west.score -= banker.double / 3
                north.score -= banker.double / 3
                break

            elif len(rules.doublets) == 7:
                if sd.ischa is True:
                    print("和！大七星，188番!")
                    print('第' + str(rounds) + '轮，自摸墙上剩余：' + str(len(walls)) + '张。游戏结束，庄家胜利。')
                    banker.score += sd.s_star * banker.double
                    south.score -= sd.s_star * banker.double / 3
                    west.score -= sd.s_star * banker.double / 3
                    north.score -= sd.s_star * banker.double / 3
                    break

                elif sd.ischa is False:
                    print("和！七对，24番!")
                    banker.score += sd.score * banker.double
                    south.score -= sd.score * banker.double / 3
                    west.score -= sd.score * banker.double / 3
                    north.score -= sd.score * banker.double / 3
                    break

                elif sd.isflush is True:
                    print("和！连七对，88番")
                    banker.score += sd.s_flushing * banker.double
                    south.score -= sd.s_flushing * banker.double / 3
                    west.score -= sd.s_flushing * banker.double / 3
                    north.score -= sd.s_flushing * banker.double / 3
                    break

            elif len(rules.all_groups) != 5:
                banging = input("请问你想要胡哪家的牌，s代表南，w代表西，n代表北：")
                while True:
                    if banging == 's':
                        banker.owned[-1] = south.abandon_area[-1]
                        break

                    elif banging == 'w':
                        banker.owned[-1] = west.abandon_area[-1]
                        break

                    elif banging == 'n':
                        banker.owned[-1] = north.abandon_area[-1]
                        break

                    else:
                        print('输入不合法，请重新输入：')
                        continue
                break

            if len(rules.all_groups) != 5:
                print("你的牌型不满足和牌，将被扣除十分！")
                banker.score -= 10
                south.score += 3
                west.score += 3
                north.score += 3
                isWin = False

        else:
            print('第'+str(rounds) + '轮，自摸墙上剩余：' + str(len(walls)) + '张。游戏终止。')
            break

    if normal is True and isWin is True:
        print('第' + str(rounds) + '轮，自摸墙上剩余：' + str(len(walls)) + '张。游戏结束，庄家胜利。')
        print("庄家的分数：{}".format(banker.score))
        print("南家的分数：{:.1f}".format(south.score))
        print("西家的分数：{:.1f}".format(west.score))
        print("北家的分数：{:.1f}".format(north.score))

    elif normal is False:
        print('第' + str(rounds) + '轮，自摸墙上剩余：' + str(len(walls)) + '张。游戏结束，庄家诈胡。')
        print("庄家的分数：{}".format(banker.score))
        print("南家的分数：{:.1f}".format(south.score))
        print("西家的分数：{:.1f}".format(west.score))
        print("北家的分数：{:.1f}".format(north.score))


if __name__ == "__main__":
    main()
    print(rules.all_groups)
