""" 番种类型总表，从上至下依次为：
一般高 老少副 【平和ok】 喜相逢 四归一 连六 三色三同顺 一色三节高 一色三步高 
一色四步高 一色四节高 碰碰和 全双刻 幺九刻 双暗刻 三暗刻 双同刻 三同刻 
暗杠 明杠 双暗杠 三杠子 【清一色ok】 混一色 绿一色 五门齐 【七对子ok 大七星 连七对】
【无字ok】 箭刻 门风刻 圈风刻 大于五 小于五 全大 全中 全小 清龙 花龙 组合龙
全带五 全带幺 全不靠 七星不靠 缺一门 断幺 混幺九 全求人 不求人 推不倒
【门前清ok】 妙手回春 杠上开花 海底捞月 坎张 边张 单钓 和绝张 自摸 清幺九
【十三幺 字一色 大四喜 大三元ok】 小四喜 小三元 四暗刻 【四杠子 九莲宝灯ok】
"""

class Score():
    top = 88
    b = 64
    c = 48
    d = 32
    high = 24
    f = 16
    g = 12
    normal = 8
    i = 6
    j = 4
    k = 2
    basic = 1


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

color_list = []
color_list.append(color_WAN)
color_list.append(color_TIAO)
color_list.append(color_TONG)

owned = []
cards = []

''' 牌型总列表 '''
orphans = ['🀐', '🀘', '🀇', '🀏', '🀙', '🀡', '🀀', '🀁', '🀂', '🀃', '🀄', '🀅', '🀆']
latern = [['🀇', '🀇', '🀇', '🀈', '🀉', '🀊', '🀋', '🀌', '🀍', '🀎', '🀏', '🀏', '🀏'],
          ['🀐', '🀐', '🀐', '🀑', '🀒', '🀓', '🀔', '🀕', '🀖', '🀗', '🀘', '🀘', '🀘'],
          ['🀙', '🀙', '🀙', '🀚', '🀛', '🀜', '🀝', '🀞', '🀟', '🀠', '🀡', '🀡', '🀡']]
green = ['🀑', '🀒', '🀓', '🀕', '🀗']
orphan_number = ['🀐', '🀘', '🀇', '🀏', '🀙', '🀡']

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


# 这一部分代码是为了重新安排Java程序中生成的字符串列表，mahjong_data.txt内的格式如下：
#
# 第一行：原手牌
# 第二行：被agariBackTrack.java 组织之后的呈标准雀头-刻子-顺子序列的手牌
# 第三行：是否自摸
# 第四行：是否海底捞月
# 第五行：是否妙手回春
# 第六行：是否杠上开花。
f = open("mahjong_data.txt", encoding="utf-8")
scripts = []
for line in f:
    scripts.append(line.strip("\n"))
f.close()

owned = eval(scripts[0])
cards = eval(scripts[1])
is_zimo = eval(scripts[2])
is_salavge = eval(scripts[3])
is_toSpring = eval((scripts[4]))
is_bloomed = eval(scripts[5])


# 注意：七对和不靠等大牌需要优先进行判定，这里暂时跳过这一步，直接计算雀头、刻子和顺子
# 以及各种花色中所含牌类的数量：
doublets.append(cards[0])

cards_copy = cards.copy()
del cards_copy[0]

for each in cards_copy:
    for i in range(len(each)):
        if each[i] == each[i+1]:
            triplets.append(each)
            break
        if ord(each[i]) == ord(each[i+1]) - 1:
            flush.append(each)
            break


for each in cards:
    if each[0] in color_WAN:
        all_WANs.append(each)

    if each[0] in color_TIAO:
        all_TIAOs.append(each)

    if each[0] in color_TONG:
        all_TONGs.append(each)

    if each[0] in cha_WIND:
        all_WINDs.append(each)

    if each[0] in cha_ARROW:
        all_ARROWs.append(each)

''' 排列组合总列表  '''
# all_groups 用作 normal() 函数手牌数量判定
all_CHARs = []
all_groups = []
all_groups += triplets + flush + pengs + gangs + doublets

colors = color_WAN + color_TIAO + color_TONG
characters = cha_WIND + cha_ARROW
mahjongs = colors + characters

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

    def seven_doublets(self, owned):
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
                if chr(ord(doublets[i][0]) + i + 1) in doublets:
                    self.flushed += 1
                else:
                    break
            if self.flushed == 6:
                self.isflush = True
            else:
                pass


class SingleColor:
    victory = False
    is_tiao = True
    is_tong = True
    num = 0
    score = 24

    def single_colored(self, owned):
        """这里是清一色和牌判定，判断 all_groups 列表里面的所有单个字符均属于
        同一花色，返回清一色判定。"""
        for i in range(len(owned)):
            if owned[i] in color_WAN:
                self.num += 1
                self.is_tong = False
                self.is_tiao = False
            if owned[i] in color_TONG and self.is_tong:
                self.num += 1
                self.is_tiao = False
            if owned[i] in color_TIAO and self.is_tiao:
                self.num += 1

        if self.num == 14:
            self.victory = True
            print("清一色 \t24番")
            return self.score
        else:
            return 0


# 所有1番和部分2番的牌型判断：
class Normal:
    v_char_less = False
    v_hexa_flush = False
    victory_reunion = False
    victory_quadra = False
    victory_clear = False

    victory_ordinary = False
    v_missing_orphan = False
    v_orphan_flush = False
    v_missing_color = False

    index = []
    is_orphan = True
    num = 0
    color_count = 0
    score = 1
    score2 = 2

    def char_less(self, owned):
        """无字和牌判定，遍历手牌列表，如果元素不属于字牌则数量加一，如果数量等于手牌长度则判定通过。"""
        for each in owned:
            if each not in characters:
                self.num += 1

        if self.num == 14:
            print("无字 \t1番")
            self.v_char_less = True
            return self.score
        else:
            return 0

    def hexa_flush(self, flushes):
        """连六的判定，传入玩家的手牌组合列表cards。查找一种花色是否是索引值相连的六张牌。
        """
        for i in range(len(flushes)):
            if len(flushes) > 1 and ord(flushes[i][0]) + 3 == ord(flushes[i+1][0]):
                self.v_hexa_flush = True
                print("连六 \t1番")
                return self.score
            else:
                break

        if not self.v_hexa_flush:
            return 0

    def reunite(self, flushes):
        """喜相逢的判定: 查找两种花色的手牌在花色列表里的索引值，完全相同则判定为真"""
        for each in flushes:
            if each[0] in color_WAN:
                self.index.append(color_WAN.index(each[0]))

            elif each[0] in color_TIAO:
                self.index.append(color_TIAO.index(each[0]))

            elif each[0] in color_TONG:
                self.index.append(color_TONG.index(each[0]))

        for j in self.index:
            if self.index.count(j) >= 2:
                self.victory_reunion = True
                print("喜相逢 \t1番")
                return self.score

        if not self.victory_reunion:
            return 0

    def quadra_cards(self, input_owned):
        """四归一的判断，需要传入玩家原手牌，如果有四张牌且玩家未鸣杠则判定有效"""
        for each in input_owned:
            if input_owned.count(each) == 4:
                self.victory_quadra = True
                print("四归一 \t1番")
                return self.score

            else:
                return 0

    def clearing(self):
        """门前清的判断代码，检测碰牌列表和杠牌列表内的元素个数。"""
        if len(pengs) == 0 and len(gangs) == 0:
            self.victory_clear = True
            print("门前清 \t2番")
            return self.score2
        else:
            return 0

    def get_ordinary(self):
        """平和的判定类以及判定函数，检测flush内元素的个数，同时将牌对子不能是字牌。"""
        if len(flush) == 4 and doublets[0] not in characters:
            self.victory_ordinary = True
            print("平和 \t2番")
            return self.score2
        else:
            return 0

    def missing_orphan(self, owned):
        """断幺的类型，传入玩家原手牌，手牌中没有来自【orphans】——幺九牌列表里的元素"""
        for i in owned:
            for j in i:
                if j in orphans:
                    self.is_orphan = False
                    break
                else:
                    self.is_orphan = True
                    continue

        if self.is_orphan is True:
            self.v_missing_orphan = True
            print("断幺喵！\t2番")
            return self.score2
        else:
            return 0

    def orphan_tiles(self, input_flush):
        """老少副的牌型，传入玩家手牌组合。查找手牌中是否有索引值为012或678的顺子。"""
        for each in input_flush:
            for e in orphan_number:
                if len(each) > 2:
                    if each[0] == e or each[2] == e:
                        self.v_orphan_flush = True
                        print("老少副 \t1番")
                        return self.score

        if not self.v_orphan_flush:
            return 0

    def missing_color(self, input_cards):
        """缺一门"""
        for each in input_cards:
            if each[0] in color_WAN:
                self.color_count += 1
            if each[0] in color_TIAO:
                self.color_count += 1
            if each[0] in color_TONG:
                self.color_count += 1

        if self.color_count <= 2:
            self.v_missing_color = True
            print("缺一门 \t2番")
            return self.score
        else:
            return 0

class NormalTiles:
    two = False
    three = False
    four = False
    score = 1
    score3 = 24
    score4 = 48

    def normal_height(self, tiles):
        """一般高的和牌判定函数，直接在normal()函数调用后检测顺子中相同元素的个数。"""
        for each in tiles:
            if tiles.count(each) == 2:
                self.two = True
                print("一般高 \t2番")
                return self.score

        if not self.two:
            return 0

    def three_flushes(self, tiles):
        """一色三同顺的判定，需要三幅（花色和序数）完全相同的顺子。"""
        for each in tiles:
            if tiles.count(each) == 3:
                self.three = True
                print("一色三同顺 \t24番")
                return self.score3
        if not self.three:
            return 0

    def four_flushes(self, tiles):
        """一色四同顺需要四副完全相同的顺子。"""
        for each in tiles:
            if tiles.count(each) == 4:
                self.four = True
                print("一色四同顺 \t48番")
                return self.score4
        if not self.four:
            return 0


class OrphanTriplets:
    """
    这里是判断幺九牌 + 刻子类的牌型，有 1番的幺九刻，32番的混幺九和 64番的清幺九。
    """
    victory_o = False
    victory_f = False
    victory_m = False
    orphan_count = 0
    score = 1
    mixed_score = 32
    full_score = 64

    def full_orphan_triplets(self, input_cards):
        """清幺九牌型，传入玩家所有手牌的面子组合cards，判断手牌中是否全部由orphan_number
        列表里面的元素组成的刻子和对子。"""
        self.orphan_count = 0
        for each in input_cards:
            if each[0] in orphan_number:
                self.orphan_count += 1

        if self.orphan_count == 5:
            self.victory_m = True
            print("清幺九 \t64番")
            return self.full_score
        else:
            return 0

    def mixed_orphan_triplets(self, input_cards):
        """混幺九的牌型，除了判断的列表从orphan_numbers变成了orphans之外没有其它变化。
        所以混幺九的成形张数比清幺九要多。"""
        self.orphan_count = 0
        for each in input_cards:
            if each[0] in orphans:
                self.orphan_count += 1

        if self.orphan_count == 5:
            self.victory_m = True
            print("混幺九 \t32番")
            return self.mixed_score
        else:
            return 0

    def orphan_triplets(self, triplet_list):
        """幺九刻的和牌型，传入triplets这个刻子列表，查找刻子列表中是否有和orphan_number
        列表中相同的元素，只要有一个便判定此番种有效。"""
        for each in triplet_list:
            if each[0] in orphan_number:
                self.victory_o = True
                print("幺九刻 \t1番")
                return self.score

        if not self.victory_o:
            return 0


class WindAndArrow:
    victory_f_wind = False
    victory_s_wind = False
    victory_arrow = False
    score = 1

    def field_wind(self, field):
        """圈风刻和牌判定，如果面子列表中存在着一个长度为 3 的字符串，如果每个
        字符 == mahjong.fieldWind 则返回圈风刻判定。"""
        for b in all_WINDs:
            if b == field:
                self.victory = True

    def side_wind(self, side_e, side_s, side_w, side_n):
        """门风刻和牌判定，如果面子列表中存在着一个长度为 3 的字符串，如果每个
        字符 == banker.sideWind 则返回门风刻判定。"""

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


class NumberTriplets:
    two = False
    three = False
    four = False
    same = False
    index = []
    score = 2
    score2 = 4
    score3 = 16
    score4 = 64

    def double_triplets(self, triplet):
        """双暗刻，检测 triplets列表的长度。"""
        if len(triplet) == 2:
            self.two = True
            print("双暗刻 \t2番")
            return self.score
        else:
            return 0

    def triple_triplets(self, triplet):
        """三暗刻，同上，只是分数不一样"""
        if len(triplet) == 3:
            self.three = True
            print("三暗刻 \t16番")
            return self.score3
        else:
            return 0

    def quadra_triplets(self, input_triplet):
        """四暗刻，同上，不过是役满。"""
        if len(input_triplet) == 4:
            self.four = True
            print("四暗刻 \t64番")
            self.three = False
            return self.score4
        else:
            return 0

    def same_triplets(self, triplet):
        """双同刻，逻辑与喜相逢类似，只不过索引的列表变成了triplet"""
        for each in triplet:
            if each[0] in color_WAN:
                self.index.append(color_WAN.index(each[0]))

            elif each[0] in color_TIAO:
                self.index.append(color_TIAO.index(each[0]))

            elif each[0] in color_TONG:
                self.index.append(color_TONG.index(each[0]))

        for j in self.index:
            if self.index.count(j) == 2:
                self.two = True
                print("双同刻 \t2番")
                return self.score

        if not self.two:
            return 0



class FullTiles:
    v_orphan = False
    v_mixed = False
    v_fives = False
    count = 0
    orphan_count = 0
    score_mixed = 2
    score_orphan = 4
    score_five = 16

    def mixed_orphan_tiles(self,input_owned):
        """混全带幺九：日麻特有的混合番种，只是将第二个嵌套的迭代循环(便乘)orphans即可。(确信)"""
        for each in input_owned:
            for e in orphans:
                if each[0] == e or each[2] == e:
                    self.v_mixed = True
                    print("混全带幺九 \t4番")
                    return self.score_mixed

        if not self.v_mixed:
            return 0

    def full_orphan_tiles(self, input_owned):
        """全带幺：传入玩家手牌组合【cards】列表。查找刻子、顺子、对子中是否均存在索引
        值为0或者8的牌。"""
        for each in input_owned:
            if len(each) == 1:
                for e in orphan_number:
                    if each == e:
                        self.orphan_count += 1
            for i in each:
                if len(each) > 1:
                    for e in orphan_number:
                        if i == e:
                            self.orphan_count += 1

        if self.orphan_count == 5:
            print("纯全带幺九 \t4番")
            return self.score_orphan
        else:
            return 0

    def all_five(self, input_owned):
        """全带五在这里进行判断，需要传入玩家的手牌面子组合。判断当cards列表元素的长度为 1
        的时候，这时这个元素是手牌的面子，接着查找colors里面的第4、第13和第21个索引的元素，
        即五万、五条和五饼是否与其相同。刻子类似，但是顺子比较复杂，我们需要再去迭代每个组合
        内部的元素，如果这些组合中都存在五万、五条和五饼，那么才算判断有效。"""
        for each in input_owned:
            if len(each) == 1:
                if each == colors[4] or each == colors[13] or each == colors[21]:
                    self.count += 1
            for i in each:
                if len(each) > 1:
                    if i == colors[4] or i == colors[13] or i == colors[21]:
                        self.count += 1

        if self.count == 5:
            self.v_fives = True
            print("全带五 \t16番")
            return self.score_five
        else:
            return 0

class PengPeng:
    victory = False
    score = 2

    def peng_peng(self):
        """碰碰和和牌判定，如果玩家曾鸣牌食碰，食杠或食和，且刻子列表和碰牌列表
        的总长度为 4 则返回碰碰和判定。"""
        if len(pengs) + len(triplets) == 4:
            self.victory = True
            print("碰碰和 \t6番")
            return self.score
        else:
            return 0


class SteppingFlush:
    v_three_steps = False
    v_single_triple_steps = False
    v_single_quadra_steps = False
    score1 = 6
    score2 = 16
    score3 = 48

    def three_steps(self, input_flush):
        """三色三步高（国标版断幺）：查找三种花色的手牌顺子的第一张在花色列表里的索引值，
        三张牌索引值相连则为真"""
        for i in range(len(input_flush)):
            if input_flush[i+1] in input_flush and input_flush[i+2] in \
                    input_flush and ord(input_flush[i]) + 1 == ord(input_flush[i+1]) \
                    == ord(input_flush[i+2]) - 1:
                self.v_three_steps = True
                print("三色三步高 \t6番")
                return self.score1

            elif input_flush[i+2] in input_flush and input_flush[i+4] in \
                    input_flush and ord(input_flush[i]) + 1 == ord(input_flush[i+1]) \
                    == ord(input_flush[i+2]) - 1:
                self.v_three_steps = True
                print("三色三步高 \t6番")
                return self.score1

        if not self.v_three_steps:
            return 0


'''def all_evens():
    if len(triplets) + len(pengs) + len(gangs) == 4:
        for i in all_groups:
            for j in range(10):
                if all_groups[i]:'''


class PureStraight():
    victory = False
    count = 0
    score = 16

    def dragon(self, owned):
        for each in color_list:
            for i in each:
                for j in owned:
                    if i == j:
                        self.count += 1
        if self.count == 9:
            self.victory = True


class Dependence:
    victory = False
    score = 2
    independence = False

    def dependence(self, banging=None):
        """不求人和牌方法，如果玩家在没有任何碰牌或杠牌的情况下自摸和牌算不求人，
        如果玩家在碰、杠四次的情况下放炮点和，则算作全求人。"""
        if len(pengs) == 0 and len(gangs) == 0 and banging == None:
            self.victory = True
        elif len(pengs) + len(gangs) == 4 and not banging:
            self.independence = True


def get_gang():
    if len(gangs):
        _gang = True
        return _gang


class FiveVarieties:
    count = 0
    victory = False
    is_character = True
    is_bamboo = True
    is_dot = True
    is_wind = True
    is_dragon = True
    score = 6

    def five_varies(self,input_card):
        """五门齐，跟清一色反过来的判定。"""
        for i in input_card:
            if i[0] in color_WAN and self.is_character:
                self.count += 1
                self.is_character = False

            if i[0] in color_TIAO and self.is_bamboo:
                self.count += 1
                self.is_bamboo = False

            if i[0] in color_TONG and self.is_dot:
                self.count += 1
                self.is_dot = False

            if i[0] in cha_WIND and self.is_wind:
                self.count += 1
                self.is_wind = False

            if i[0] in cha_ARROW and self.is_dragon:
                self.count += 1
                self.is_dragon = False

        if self.count == 5:
            self.victory = True
            print("五门齐 \t6番")
            return self.score
        else:
            return 0


def mixing_Color(owned):
    for i in owned:
        if i in colors:
            continue
        if i in characters:
            break
    one_minxed_color = True
    return one_minxed_color


def get_all_big():
    for i in all_groups:
        if i[0] > 1:  # 需要一个变量存储手牌序数
            pass


class Thirteen_Alones:
    score = 88
    num = 0
    victory = False

    def thirteen_Alones(self, owned):
        if len(owned) == 14:
            orphans.sort()
            for i in orphans:
                if 1 <= owned.count(i) <= 2:
                    self.num += 1

            if self.num == 13:
                self.victory = True


class LotusLantern:
    """九莲宝灯的判定代码。对于传入的手牌 owned，循环九莲宝灯列表 lantern 内的各元素，向列表内的列表
    追加各花色内 1~9 的序数牌，然后将其与手牌进行比对，完全匹配即返回 True，否则返回 False。"""
    victory = False
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
                    self.victory = True
                else:
                    if each[0] in color_WAN:
                        each.remove(color_WAN[i])

                    elif each[0] in color_TONG:
                        each.remove(color_TONG[i])

                    elif each[0] in color_TIAO:
                        each.remove(color_TIAO[i])
                    continue


class GreatTriplets:
    """大三元的判定"""
    score = 88
    victory = False

    def the_Great_Triplets(self, owned):
        if owned.count(cha_ARROW[0]) >= 3 and owned.count(cha_ARROW[1]) >= 3 and \
                owned.count(cha_ARROW[2]) >= 3:
            self.victory = True


class GreatQuadrilets:
    score = 88
    count = 0
    victory = False

    def the_Great_Quadrilets(self, owned):
        for i in cha_WIND:
            if i in owned and owned.count(i) >= 3:
                self.count += 1
        if self.count == 4:
            self.victory = True

    def the_Little_Quadrilets(self):
        if owned.count(cha_WIND[0]) == 2 or owned.count(cha_WIND[1]) == 2 or \
                owned.count(cha_WIND[2]) == 2 or owned.count(cha_WIND[3]) == 2:

            if owned.count(cha_WIND[0]) >= 3 and owned.count(cha_WIND[1]) >= 3 and \
                    owned.count(cha_WIND[2]) >= 3:
                self.score = 64
                self.victory = True

            elif owned.count(cha_WIND[0]) >= 3 and owned.count(cha_WIND[2]) >= 3 and \
                    owned.count(cha_WIND[3]) >= 3:
                self.score = 64
                self.victory = True

            elif owned.count(cha_WIND[1]) >= 3 and owned.count(cha_WIND[2]) >= 3 and \
                    owned.count(cha_WIND[3]) >= 3:
                self.score = 64
                self.victory = True


class ColorCharacters:
    victory = False
    num = 0
    score = 64

    def character_Colors(self, owned):
        for each in owned:
            if each in characters:
                self.num += 1

            if self.num == 14:
                self.victory = True


def four_Gangs():
    if len(gangs) == 4:
        return True


triplets += pengs + gangs
doubles = 0
normal = Normal()
nt = NormalTiles()
num_tri = NumberTriplets()
ft = FullTiles()
or_tri = OrphanTriplets()
lotus = LotusLantern()
seven = SevenDoublets()
sc = SingleColor()
fv = FiveVarieties()

doubles += normal.char_less(owned)
doubles += normal.hexa_flush(flush)
doubles += normal.orphan_tiles(cards)
doubles += normal.quadra_cards(owned)
doubles += normal.reunite(flush)

doubles += or_tri.orphan_triplets(triplets)
doubles += or_tri.mixed_orphan_triplets(triplets)
doubles += or_tri.full_orphan_triplets(triplets)

doubles += normal.clearing()
doubles += normal.get_ordinary()
doubles += normal.missing_orphan(owned)
doubles += normal.missing_color(cards)

doubles += nt.normal_height(flush)
doubles += nt.three_flushes(flush)
doubles += nt.four_flushes(flush)

doubles += num_tri.same_triplets(triplets)
doubles += num_tri.triple_triplets(triplets)
doubles += num_tri.quadra_triplets(triplets)

doubles += ft.full_orphan_tiles(cards)
doubles += ft.all_five(cards)

doubles += fv.five_varies(cards)
doubles += sc.single_colored(owned)

print(doubles)
