owned = ['🀀', '🀃', '🀄', '🀈', '🀉', '🀏', '🀓', '🀔', '🀕', '🀕', '🀜', '🀟', '🀡', '🀠']
owned.sort()

uni_TIAO = []
uni_TONG = []
uni_WAN = []
uni_WIND = []
uni_ARROW = []
all_uni = []

color_WAN = ['🀇', '🀈', '🀉', '🀊', '🀋', '🀌', '🀍', '🀎', '🀏']
color_TIAO = ['🀐', '🀑', '🀒', '🀓', '🀔', '🀕', '🀖', '🀗', '🀘']
color_TONG = ['🀙', '🀚', '🀛', '🀜', '🀝', '🀞', '🀟', '🀠', '🀡']
cha_WIND = ['🀀', '🀁', '🀂', '🀃']
cha_ARROW = ['🀄', '🀅', '🀆']

colors = color_WAN + color_TIAO + color_TONG
characters = cha_WIND + cha_ARROW
majongs = colors + characters

''' 牌型总列表 '''
alones = ['🀐','🀘','🀇','🀏','🀙','🀡','🀀','🀁','🀂','🀃','🀄','🀅','🀆']
latern = [['🀇','🀇','🀇','🀈','🀉','🀊','🀋','🀌','🀍','🀎','🀏','🀏','🀏'],
          ['🀐','🀐','🀐','🀑','🀒','🀓','🀔','🀕','🀖','🀗','🀘','🀘','🀘'],
          ['🀙','🀙','🀙','🀚','🀛','🀜','🀝','🀞','🀟','🀠','🀡','🀡','🀡']]
green = ['🀑', '🀒', '🀓', '🀕', '🀗']


''' 排列组合分列表  '''
# 以下列表用于收集手牌的所有排列组合
doublets = []
flush = []
triplets = []
pengs = []
gangs = []
chars = []
flowers = []

''' 花色序数分列表  '''
# 以下列表用于normal函数中判断花色和序数组合
# all_WIND 和 all_ARROWs 用于 score.py 模块内的番种分数结算
all_WANs = []
all_TIAOs = []
all_TONGs = []
all_WINDs = []
all_ARROWs = []

''' 排列组合总列表  '''
# all_groups 用作 normal() 函数手牌数量判定
all_CHARs = []
all_groups = []
all_groups += triplets + flush + pengs + gangs + doublets

""" 番种类型总表，从上至下依次为：
一般高 老少副 平和 喜相逢 四归一 连六 三色三同顺 一色三节高 一色三步高 
一色四步高 一色四节高 碰碰和 全双刻 幺九刻 双暗刻 三暗刻 双同刻 三同刻 
暗杠 明杠 双暗杠 三杠子 清一色 混一色 绿一色 五门齐 七对子 大七星 连七对
无字 箭刻 门风刻 圈风刻 大于五 小于五 全大 全中 全小 清龙 花龙 组合龙
全带五 全带幺 全不靠 七星不靠 缺一门 断幺 混幺九 全求人 不求人 推不倒
门前清 妙手回春 杠上开花 海底捞月 坎张 边张 单钓 和绝张 自摸 清幺九
十三幺 字一色 大四喜 大三元 小四喜 小三元 四暗刻 四杠子 九莲宝灯
"""
''' 以下为顺子类和牌型：
一般高 老少副 平和 喜相逢 四归一 连六 三色三同顺 一色三节高 一色三步高 
一色四步高 一色四节高 '''
doubles = []
normal_height = False
flush_1_9 = False
ordinary = False
reunion = False
quadrilet = False
hexa_flush = False
flush_of_three = False
flush_of_one = False
three_steps_of_one = False
four_steps_of_one = False
four_triplets_of_one = False

'''以下为刻子类和牌型：
碰碰和 全双刻 幺九刻 双暗刻 三暗刻 双同刻 三同刻 
'''
peng_peng = False
even_triplets = False
triplets_1_9 = False
double_triplets = False
triple_triplets = False
same_two_triplets = False
same_three_triplets = False

'''以下为杠子类和牌型：
暗杠 明杠 双暗杠 三杠子
'''
an_gang = False
ming_gang = False
double_gangs = False
triple_gangs = False

'''以下为花色类和牌型：
清一色 混一色 绿一色 五门齐
'''
single_color = False
mixing_color = False
green_color = False
five_varies = False

'''以下为七对类和牌型：
七对子 大七星 连七对
'''
seven_doublets = False
hepta_stars = False
flush_doblets = False

'''以下为字牌类和牌型：
无字 箭刻 门风刻 圈风刻
'''
char_less = False
arrow_triplets = False
side_wind = False
field_wind = False
'''以下为组合类和牌型：
大于五 小于五 全大 全中 全小 清龙 花龙 组合龙
'''
bigger_than_5 = False
smaller_than_5 = False
all_big = False
all_middle = False
all_small = False
dragon = False
mixing_dragon = False
column_dragon = False

'''以下为全带和不靠类和牌型：
全带五 全带幺 全不靠 七星不靠 缺一门 断幺 混幺九
'''
taking_five = False
taking_alones = False
all_alones = False
hepta_alones = False
missing_vary = False
missing_1_9 = False
mixing_1_9 = False

'''以下为方式类和牌型：
全求人 不求人 推不倒 门前清 妙手回春 杠上开花 海底捞月 坎张 边张 单钓 
和绝张 自摸
'''
independence = False
dependence = False
symmetry = False
clear = False
back_to_spring = False
bloomed_gang = False
lunar_salvage = False
between = False
edge = False
fishing = False
only = False
zi_mo = False

'''以下为役满类和牌型：
清幺九 十三幺 字一色 大四喜 大三元 小四喜 小三元 四暗刻 四杠子 九莲宝灯 连七对 天和 地和 人和
'''
single_1_9 = False
thirteen_alones = False
character_colors = False
the_great_quadruple = False
the_great_triple = False
little_quadruple = False
little_triple = False
quadruple_triplets = False
quadruple_gangs = False
lotus_lantern = False
celestial = False
earthical = False
anthropal = False

doubles.append(normal_height)
def normal(owned, gang, peng):
    """ 麻将 ASCII 码从126976 ~ 127018
       排列顺序：东南西北，中发白，万条筒，春夏秋冬，梅兰竹菊

        1. 对原手牌先进行顺子（flush）判定：
        对于传入的手牌（owned），将所有万字的花色放入列表 color_WAN 里面，遍历 color_WAN 列表中的所有元素，如果列表中存在某个元素和它的两个后继元素，则向顺子列表（flush）中添加该元素以及它的后继。

        2. 接着对原手牌进行刻子（triplets）判定：
        遍历 color_WAN 列表中的所有元素，如果列表中存在三个相同元素，则向刻子列表（triplets）中添加该元素。

        3. 然后对原手牌进行对子（doublets）判定：
        遍历 color_WAN 列表中的所有元素，如果列表中存在两个相同元素，则向对子列表（doublets）中添加该元素。

        4. 最后进行手牌面子数判定：
        对于传入的碰牌（peng）和杠牌（gang）列表，如果这两个列表的长度加上顺子列表（flush），刻子列表（triplets）和对子列表（doublets）的总长度为 5 则返回和牌有效。

        """
    for a in owned:  # 传入手牌，获取三种花色的序数牌的Unicode值并放入列表
        if a in color_WAN:
            all_WANs.append(a)
            uni_WAN.append(ord(a))

        if a in color_TIAO:
            all_TIAOs.append(a)
            uni_TIAO.append(ord(a))
            # print(color_TIAO)

        if a in color_TONG:
            all_TONGs.append(a)
            uni_TONG.append(ord(a))
            # print(color_TONG)

        if a in cha_WIND:
            all_WINDs.append(a)

        if a in cha_ARROW:
            all_ARROWs.append(a)

    all_uni = uni_WAN + uni_TONG + uni_TIAO
    # 万字 Unicode 值在126983 ~ 126991间
    # 判断前三张牌是否是顺子，如果unicode中没有元素便跳出循环，如果仍有元素则
    # 继续无限循环。根据unicode内元素数量的不同，可分为以下两种情况：
    #
    # 1. 对unicode取3的余等于零，即该花色手牌有3，6，9，12张且没有对子的时候
    # 遍历unicode里的所有元素，取出其中相邻的三个元素放入flush列表中，再将这
    # 三个元素从unicode列表中移除。跳出迭代循环，此时如果unicode中仍有元素则
    # 继续按以上步骤再次循环。
    #
    # 2. 对unicode取3的余等于2，即该花色手牌中存在着对子。遍历unicode里的所有
    # 元素。之后的步骤和1.中的步骤完全一样，仅需在最后加上一个判断对子的代码块。
    for i in range(4):
        if len(uni_WAN) % 3 == 0:
            for a in uni_WAN:
                # 这里是判断手牌中刻子数量的代码，如果原手牌该花色中没有顺子则进入此处的迭代循环，
                # 不过在一色三同顺（或者叫一色三节高）牌型中存在着三副序数增添一位的刻子，所以
                # 在一色三同顺的分数结算代码中，只需要计算flush列表中存不存在着三副相同的元素即可。
                # ps：如果存在着四副相同的顺子便是一色四同顺，如果存在着四副序数依次增添一位
                # 的刻子便是一色四节高，如果存在着四副刻子则是64番四暗刻，注意：四暗刻只有在
                # 单钓将的时候才可以通过闲家的放炮成立，其它情况只能自摸，闲家放炮只计三暗刻。

                if uni_WAN.count(a) >= 3:
                    triplets.append(chr(a) * 3)
                    for b in range(3):
                        uni_WAN.remove(a)
                        owned.remove(chr(a))
                        print(owned)

            for i in uni_WAN:
                if i in uni_WAN and i + 1 in uni_WAN and i + 2 in uni_WAN:
                    res = chr(i) + chr(i + 1) + chr(i + 2)
                    uni_WAN.remove(i)
                    uni_WAN.remove(i + 1)
                    uni_WAN.remove(i + 2)
                    owned.remove(chr(i))
                    owned.remove(chr(i+1))
                    owned.remove(chr(i+2))
                    flush.append(res)
                    break
                else:
                    break

        elif len(uni_WAN) % 3 == 2:
            for i in uni_WAN:
                if i in uni_WAN and i + 1 in uni_WAN and i + 2 in uni_WAN:
                    res = chr(i) + chr(i + 1) + chr(i + 2)
                    uni_WAN.remove(i)
                    uni_WAN.remove(i + 1)
                    uni_WAN.remove(i + 2)
                    owned.remove(chr(i))
                    owned.remove(chr(i + 1))
                    owned.remove((chr(i + 2)))
                    flush.append(res)
                    break
                
                else:
                    break

            for a in uni_WAN:
                if uni_WAN.count(a) >= 3:
                    triplets.append(chr(a) * 3)
                    for b in range(3):
                        uni_WAN.remove(a)
                        owned.remove(chr(a))

            for a in uni_WAN:
                if uni_WAN.count(a) == 2:
                    doublets.append(chr(a) * 2)
                    uni_WAN.remove(a)
                    uni_WAN.remove(a)
                
                else:
                    break

        ''' 条字 Unicode 码从126992 ~ 127000'''
        if len(uni_TIAO) % 3 == 0:

            for a in uni_TIAO:
                if uni_TIAO.count(a) == 3:
                    triplets.append(chr(a) * 3)
                    for b in range(3):
                        uni_TIAO.remove(a)
                        owned.remove(chr(a))
                

            for i in uni_TIAO:
                if i in uni_TIAO and i + 1 in uni_TIAO and i + 2 in uni_TIAO:
                    res = chr(i) + chr(i + 1) + chr(i + 2)
                    uni_TIAO.remove(i)
                    uni_TIAO.remove(i + 1)
                    uni_TIAO.remove(i + 2)
                    owned.remove(chr(i))
                    owned.remove(chr(i + 1))
                    owned.remove((chr(i + 2)))
                    flush.append(res)
                    break
                
                else:
                    break

        elif len(uni_TIAO) % 3 == 2:
            for i in uni_TIAO:
                if i in uni_TIAO and i + 1 in uni_TIAO and i + 2 in uni_TIAO:
                    res = chr(i) + chr(i + 1) + chr(i + 2)
                    uni_TIAO.remove(i)
                    uni_TIAO.remove(i + 1)
                    uni_TIAO.remove(i + 2)
                    owned.remove(chr(i))
                    owned.remove(chr(i + 1))
                    owned.remove((chr(i + 2)))
                    flush.append(res)
                    break
                
                else:
                    break

            for a in uni_TIAO:
                if uni_TIAO.count(a) == 3:
                    triplets.append(chr(a) * 3)
                    for b in range(3):
                        uni_TIAO.remove(a)
                        owned.remove(chr(a))
                

            for a in uni_TIAO:
                if uni_TIAO.count(a) == 2:
                    doublets.append(chr(a) * 2)
                    uni_TIAO.remove(a)
                    uni_TIAO.remove(a)
                
                else:
                    break

        ''' 筒字 Unicode 码从127001 ~ 127009'''
        if len(uni_TONG) % 3 == 0:

            for a in uni_TONG:
                if uni_TONG.count(a) >= 3:
                    triplets.append(chr(a) * 3)
                    for b in range(3):
                        uni_TONG.remove(a)
                        owned.remove(chr(a))
                

            for i in uni_TONG:
                if i in uni_TONG and i + 1 in uni_TONG and i + 2 in uni_TONG:
                    res = chr(i) + chr(i + 1) + chr(i + 2)
                    uni_TONG.remove(i)
                    uni_TONG.remove(i + 1)
                    uni_TONG.remove(i + 2)
                    owned.remove(chr(i))
                    owned.remove(chr(i + 1))
                    owned.remove((chr(i + 2)))
                    flush.append(res)
                    break

        elif len(uni_TONG) % 3 == 2:
            for i in uni_TONG:
                if i in uni_TONG and i + 1 in uni_TONG and i + 2 in uni_TONG:
                    res = chr(i) + chr(i + 1) + chr(i + 2)
                    uni_TONG.remove(i)
                    uni_TONG.remove(i + 1)
                    uni_TONG.remove(i + 2)
                    flush.append(res)
                    break

                for a in uni_TONG:
                    if uni_TONG.count(a) >= 3:
                        triplets.append(chr(a) * 3)
                        for b in range(3):
                            uni_TONG.remove(a)
                            owned.remove(chr(a))

                for a in uni_TONG:
                    if uni_TONG.count(a) == 2:
                        doublets.append(chr(a) * 2)
                        uni_TONG.remove(a)
                        uni_TONG.remove(a)

        local_winds = []
        local_arrows = []
        ''' 风牌 Unicode 码从126976 ~ 126979'''
        for a in all_WINDs:
            if len(all_WINDs) % 3 == 0:
                if all_WINDs.count(a) == 3:
                    local_winds.append(a * 3)
                    chars.append(a * 3)
                    all_WINDs.remove(a)
                    all_WINDs.remove(a)

            else:
                if all_WINDs.count(a) == 3:
                    local_winds.append(a * 3)
                    chars.append(a * 3)
                    all_WINDs.remove(a)
                    all_WINDs.remove(a)
                    all_WINDs.remove(a)

                if all_WINDs.count(a) == 2:
                    doublets.append(a * 2)
                    all_WINDs.remove(a)
                    all_WINDs.remove(a)
                    break
                
                else:
                    break

        ''' 箭牌 Unicode 码从126980 ~ 126982'''
        for a in all_ARROWs:
            if len(all_ARROWs) % 3 == 0:
                if all_ARROWs.count(a) == 3:
                    local_arrows.append(a * 3)
                    chars.append(a * 3)
                    all_ARROWs.remove(a)
                    all_ARROWs.remove(a)

            else:
                if all_ARROWs.count(a) == 3:
                    local_arrows.append(a * 3)
                    chars.append(a * 3)
                    all_ARROWs.remove(a)
                    all_ARROWs.remove(a)
                    all_ARROWs.remove(a)

                if all_ARROWs.count(a) == 2:
                    doublets.append(a * 2)
                    all_ARROWs.remove(a)
                    all_ARROWs.remove(a)
                    break
                
                else:
                    break

    if peng != None:
        for each in peng:
            pengs.append(each)

    if gang != None:
        for each in gang:
            gangs.append(each)

    all_groups = doublets + triplets + flush + pengs + gangs + chars
    if len(all_groups) == 5:
        return True

    else:
        return False

class SevenDoublets:
    ischa = False
    isflush = False
    flushed = 0
    score = 24
    s_star = 166
    s_flushing = 88
    name_sd = "七对"
    name_stars = "大七星"
    name_flushed = "连七对"

    def seven_Doublets(self, owned):
        """这里是七对子的和牌判定，直接判断doublets列表里面是否有 7副对子。
        如果这些对子均为字牌，则返回大七星判定。如果这些对子彼此相连，且为同一花色
        则返回连七对判定。"""
        cha_true = 0

        if len(doublets) == 7:
            for i in doublets:
                if i in characters:
                    cha_true += 1
                else:
                    break

            if cha_true == 7:
                self.ischa = True

            for i in range(len(doublets)):
                if chr(ord(doublets[i][0])+i+1) in doublets:
                    self.flushed += 1
                else:
                    break
            if self.flushed == 6:
                self.isflush = True
            else:
                pass


class SingleColor:
    win = False
    num = 0
    score = 24

    def single_Colored(self, owned):
        """这里是清一色和牌判定，判断 all_groups 列表里面的所有单个字符均属于
        同一花色，返回清一色判定。"""
        for a in owned:
            if a in color_WAN or color_TIAO or color_TONG:
                self.num += 1

        if self.num == 14:
            self.win = True


class FieldWind:
    win = False

    def field_Wind(self, field):
        """圈风刻和牌判定，如果面子列表中存在着一个长度为 3 的字符串，如果每个
        字符 == mahjong.fieldWind 则返回圈风刻判定。"""
        for b in all_WINDs:
            if b == field:
                self.win = True


class SideWind:
    win = False
    score = 1

    def side_Wind(self, side_e, side_s, side_w, side_n):
        """门风刻和牌判定，如果面子列表中存在着一个长度为 3 的字符串，如果每个
        字符 == banker.sideWind 则返回门风刻判定。"""
        if normal:
           for b in chars:
                if b == side_e:
                    return side_e


class ArrowTriplets:
    win = False
    score = 1

    def arrow_Triplets(self):
        for each in triplets:
            if each in all_ARROWs:
                if len(each) == 1:
                    arrow_triplets = True
                    return arrow_triplets

                elif len(each) == 2:
                    double_arrows = True
                    return double_arrows
            # print(arrow_triplets)


class PengPeng():
    win = False
    score = 2

    def peng_Peng(self):
        '''碰碰和和牌判定，如果玩家曾鸣牌食碰，食杠或食和，且刻子列表和碰牌列表
        的总长度为 4 则返回碰碰和判定。'''
        if len(pengs):
            if len(pengs) + len(triplets) == 4 and zi_mo == False:
                peng_peng = True
                return peng_peng

'''def all_evens():
    if len(triplets) + len(pengs) + len(gangs) == 4:
        for i in all_groups:
            for j in range(10):
                if all_groups[i]:'''


class Missing_Alones():
    win = False
    isAlone = True
    score = 2

    def missing_alone(self, owned):
        for i in owned:
            for j in i:
                if j in alones:
                    self.isAlone = False
                    break
                else:
                    self.isAlone = True
                    continue

        if self.isAlone is True:
            self.win = True


def get_gang():
    if len(gangs):
        _gang = True
        return _gang


def five_Varies(owned):
    for i in owned:
        if i in color_WAN:
            continue
        if i in color_TIAO:
            continue
        if i in color_TONG:
            continue
        if i in cha_WIND:
            continue
        if i in cha_ARROW:
            break
    five_varies = True
    return five_varies


def mixing_Color(owned):
    for i in owned:
        if i in colors:
            continue
        if i in characters:
            break
    one_minxed_color = True
    return one_minxed_color


class Clearing():
    "门前清的判断代码，检测碰牌列表和杠牌列表内的元素个数。"
    win = False
    score = 2

    def clearing(self):
        if len(pengs) == 0 and len(gangs) == 0:
            self.win = True


class Ordinary():
    "平和的判定类以及判定函数，检测flush内元素的个数。"
    win = False
    score = 2

    def get_ordinary(self):
        if len(flush) == 4:
            self.win = True


def get_reunion():
    for each in all_groups:
        pass

def get_quadrilet(owned):
    for each in owned:
        if owned.count(each) == 4:
            return True

def hexa_Flush():
    for each in range(len(flush)):
        if ord(flush[each][2]) + 1 == ord(flush[each+1][0]):
            return True

def get_all_big():
    for i in all_groups:
        if i[0] > 1: # 需要一个变量存储手牌序数
            pass


class Thirteen_Alones:
    score = 88
    num = 0
    win = False
    def thirteen_Alones(self, owned):
        if len(owned) == 14:
            alones.sort()
            for i in alones:
                if 1 <= owned.count(i) <= 2:
                    self.num += 1

            if self.num == 13:
                self.win = True


class LotusLantern:
    """九莲宝灯的判定代码。对于传入的手牌 owned，循环九莲宝灯列表 lantern 内的各元素，向列表内的列表
    追加各花色内 1~9 的序数牌，然后将其与手牌进行比对，完全匹配即返回 True，否则返回 False。"""
    win = False
    score = 88
    def lotus_Lantern(self, owned):
        for each in latern:
            for i in range(9):
                self.each_one = each
                if each[0] in color_WAN:
                    each.append(color_WAN[i])

                elif each[0] in color_TONG:
                    each.append(color_TONG[i])

                elif each[0] in color_TIAO:
                    each.append(color_TIAO[i])
                each.sort()
                self.each_one = each
                if owned == self.each_one:
                    self.win = True
                else:
                    if each[0] in color_WAN:
                        each.remove(color_WAN[i])

                    elif each[0] in color_TONG:
                        each.remove(color_TONG[i])

                    elif each[0] in color_TIAO:
                        each.remove(color_TIAO[i])
                    continue
class GreatTriplets:
    score = 88
    win = False

    def the_Great_Triplets(self, owned):
        if owned.count(cha_ARROW[0]) >= 3 and owned.count(cha_ARROW[1]) >= 3 and \
            owned.count(cha_ARROW[2]) >= 3:
            self.win = True


class GreatQuadrilets:
    score = 88
    win = False

    def the_Great_Quadrilets(self, owned):
        if owned.count(cha_WIND[0]) >= 3 and owned.count(cha_WIND[1]) >= 3 and \
                owned.count(cha_WIND[2]) >= 3 and owned.count(cha_WIND[3]) >= 3:
            self.win = True

    def the_Little_Quadrilets(self):
        if owned.count(cha_WIND[0]) == 2 or owned.count(cha_WIND[1]) == 2 or \
                owned.count(cha_WIND[2]) == 2 or owned.count(cha_WIND[3]) == 2:

            if owned.count(cha_WIND[0]) >= 3 and owned.count(cha_WIND[1]) >= 3 and \
                    owned.count(cha_WIND[2]) >= 3:
                self.score = 64
                self.win = True

            elif owned.count(cha_WIND[0]) >= 3 and owned.count(cha_WIND[2]) >= 3 and \
                    owned.count(cha_WIND[3]) >= 3:
                self.score = 64
                self.win = True

            elif owned.count(cha_WIND[1]) >= 3 and owned.count(cha_WIND[2]) >= 3 and \
                    owned.count(cha_WIND[3]) >= 3:
                self.score = 64
                self.win = True

class ColorCharacters:
    win = False
    num = 0
    score = 64

    def character_Colors(self, owned):
        for each in owned:
            if each in characters:
                self.num += 1

            if self.num == 14:
                self.win = True


def four_Gangs():
    if len(gangs) == 4:
        return True


class Score:
    def __init__(self, b_score, s_score, w_score, n_score):
        self.b_score = b_score
        self.s_score = s_score
        self.w_score = w_score
        self.n_score = n_score

triplets += pengs + gangs
if __name__ == "__main__":
    
    normal(owned, None, None)
    
