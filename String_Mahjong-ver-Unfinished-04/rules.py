owned = ['๐', '๐', '๐', '๐', '๐', '๐', '๐', '๐', '๐', '๐', '๐', '๐', '๐ก', '๐ ']
owned.sort()

uni_TIAO = []
uni_TONG = []
uni_WAN = []
uni_WIND = []
uni_ARROW = []
all_uni = []

color_WAN = ['๐', '๐', '๐', '๐', '๐', '๐', '๐', '๐', '๐']
color_TIAO = ['๐', '๐', '๐', '๐', '๐', '๐', '๐', '๐', '๐']
color_TONG = ['๐', '๐', '๐', '๐', '๐', '๐', '๐', '๐ ', '๐ก']
cha_WIND = ['๐', '๐', '๐', '๐']
cha_ARROW = ['๐', '๐', '๐']

colors = color_WAN + color_TIAO + color_TONG
characters = cha_WIND + cha_ARROW
majongs = colors + characters

''' ็ๅๆปๅ่กจ '''
alones = ['๐','๐','๐','๐','๐','๐ก','๐','๐','๐','๐','๐','๐','๐']
latern = [['๐','๐','๐','๐','๐','๐','๐','๐','๐','๐','๐','๐','๐'],
          ['๐','๐','๐','๐','๐','๐','๐','๐','๐','๐','๐','๐','๐'],
          ['๐','๐','๐','๐','๐','๐','๐','๐','๐','๐ ','๐ก','๐ก','๐ก']]
green = ['๐', '๐', '๐', '๐', '๐']


''' ๆๅ็ปๅๅๅ่กจ  '''
# ไปฅไธๅ่กจ็จไบๆถ้ๆ็็ๆๆๆๅ็ปๅ
doublets = []
flush = []
triplets = []
pengs = []
gangs = []
chars = []
flowers = []

''' ่ฑ่ฒๅบๆฐๅๅ่กจ  '''
# ไปฅไธๅ่กจ็จไบnormalๅฝๆฐไธญๅคๆญ่ฑ่ฒๅๅบๆฐ็ปๅ
# all_WIND ๅ all_ARROWs ็จไบ score.py ๆจกๅๅ็็ช็งๅๆฐ็ป็ฎ
all_WANs = []
all_TIAOs = []
all_TONGs = []
all_WINDs = []
all_ARROWs = []

''' ๆๅ็ปๅๆปๅ่กจ  '''
# all_groups ็จไฝ normal() ๅฝๆฐๆ็ๆฐ้ๅคๅฎ
all_CHARs = []
all_groups = []
all_groups += triplets + flush + pengs + gangs + doublets

""" ็ช็ง็ฑปๅๆป่กจ๏ผไปไธ่ณไธไพๆฌกไธบ๏ผ
ไธ่ฌ้ซ ่ๅฐๅฏ ๅนณๅ ๅ็ธ้ข ๅๅฝไธ ่ฟๅญ ไธ่ฒไธๅ้กบ ไธ่ฒไธ่้ซ ไธ่ฒไธๆญฅ้ซ 
ไธ่ฒๅๆญฅ้ซ ไธ่ฒๅ่้ซ ็ขฐ็ขฐๅ ๅจๅๅป ๅนบไนๅป ๅๆๅป ไธๆๅป ๅๅๅป ไธๅๅป 
ๆๆ  ๆๆ  ๅๆๆ  ไธๆ ๅญ ๆธไธ่ฒ ๆททไธ่ฒ ็ปฟไธ่ฒ ไบ้จ้ฝ ไธๅฏนๅญ ๅคงไธๆ ่ฟไธๅฏน
ๆ ๅญ ็ฎญๅป ้จ้ฃๅป ๅ้ฃๅป ๅคงไบไบ ๅฐไบไบ ๅจๅคง ๅจไธญ ๅจๅฐ ๆธ้พ ่ฑ้พ ็ปๅ้พ
ๅจๅธฆไบ ๅจๅธฆๅนบ ๅจไธ้  ไธๆไธ้  ็ผบไธ้จ ๆญๅนบ ๆททๅนบไน ๅจๆฑไบบ ไธๆฑไบบ ๆจไธๅ
้จๅๆธ ๅฆๆๅๆฅ ๆ ไธๅผ่ฑ ๆตทๅบๆๆ ๅๅผ  ่พนๅผ  ๅ้ ๅ็ปๅผ  ่ชๆธ ๆธๅนบไน
ๅไธๅนบ ๅญไธ่ฒ ๅคงๅๅ ๅคงไธๅ ๅฐๅๅ ๅฐไธๅ ๅๆๅป ๅๆ ๅญ ไน่ฒๅฎ็ฏ
"""
''' ไปฅไธไธบ้กบๅญ็ฑปๅ็ๅ๏ผ
ไธ่ฌ้ซ ่ๅฐๅฏ ๅนณๅ ๅ็ธ้ข ๅๅฝไธ ่ฟๅญ ไธ่ฒไธๅ้กบ ไธ่ฒไธๅ้กบ ไธ่ฒไธ่้ซ ไธ่ฒไธๆญฅ้ซ 
ไธ่ฒๅๆญฅ้ซ ไธ่ฒๅ่้ซ ไธ่ฒๅๅ้กบ'''
doubles = []
normal_height = False
flush_1_9 = False
ordinary = False
reunion = False
quadrilet = False
hexa_flush = False                # ่ฟๅญ
flush_of_three = False            # ไธ่ฒไธๅ้กบ 8
higher_flush_of_Three = False     # ไธ่ฒไธ่้ซ 8
same_flushes_of_one = False       # ไธ่ฒไธๅ้กบ 24
three_steps_of_one = False        # ไธ่ฒไธๆญฅ้ซ 16
higher_flush_of_one = False       # ไธ่ฒไธ่้ซ 24
four_steps_of_one = False         # ไธ่ฒๅๆญฅ้ซ 32
four_triplets_of_one = False      # ไธ่ฒๅ่้ซ 48
four_flushes_of_one = False       # ไธ่ฒๅๅ้กบ 48

'''ไปฅไธไธบๅปๅญ็ฑปๅ็ๅ๏ผ
็ขฐ็ขฐๅ ๅจๅๅป ๅนบไนๅป ๅๆๅป ไธๆๅป ๅๅๅป ไธๅๅป 
'''
peng_peng = False
even_triplets = False
triplets_1_9 = False
double_triplets = False
triple_triplets = False
same_two_triplets = False
same_three_triplets = False

'''ไปฅไธไธบๆ ๅญ็ฑปๅ็ๅ๏ผ
ๆๆ  ๆๆ  ๅๆๆ  ไธๆ ๅญ
'''
an_gang = False
ming_gang = False
double_gangs = False
triple_gangs = False

'''ไปฅไธไธบ่ฑ่ฒ็ฑปๅ็ๅ๏ผ
ๆธไธ่ฒ ๆททไธ่ฒ ็ปฟไธ่ฒ ไบ้จ้ฝ
'''
single_color = False
mixing_color = False
green_color = False
five_varies = False

'''ไปฅไธไธบไธๅฏน็ฑปๅ็ๅ๏ผ
ไธๅฏนๅญ ๅคงไธๆ ่ฟไธๅฏน
'''
seven_doublets = False
hepta_stars = False
flush_doblets = False

'''ไปฅไธไธบๅญ็็ฑปๅ็ๅ๏ผ
ๆ ๅญ ็ฎญๅป ้จ้ฃๅป ๅ้ฃๅป
'''
char_less = False
arrow_triplets = False
side_wind = False
field_wind = False
'''ไปฅไธไธบ็ปๅ็ฑปๅ็ๅ๏ผ
ๅคงไบไบ ๅฐไบไบ ๅจๅคง ๅจไธญ ๅจๅฐ ๆธ้พ ่ฑ้พ ็ปๅ้พ
'''
bigger_than_5 = False
smaller_than_5 = False
all_big = False
all_middle = False
all_small = False
dragon = False
mixing_dragon = False
column_dragon = False

'''ไปฅไธไธบๅจๅธฆๅไธ้ ็ฑปๅ็ๅ๏ผ
ๅจๅธฆไบ ๅจๅธฆๅนบ ๅจไธ้  ไธๆไธ้  ็ผบไธ้จ ๆญๅนบ ๆททๅนบไน
'''
taking_five = False
taking_alones = False
all_alones = False
hepta_alones = False
missing_vary = False
missing_1_9 = False
mixing_1_9 = False

'''ไปฅไธไธบๆนๅผ็ฑปๅ็ๅ๏ผ
ๅจๆฑไบบ ไธๆฑไบบ ๆจไธๅ ้จๅๆธ ๅฆๆๅๆฅ ๆ ไธๅผ่ฑ ๆตทๅบๆๆ ๅๅผ  ่พนๅผ  ๅ้ 
ๅ็ปๅผ  ่ชๆธ
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

'''ไปฅไธไธบๅฝนๆปก็ฑปๅ็ๅ๏ผ
ๆธๅนบไน ๅไธๅนบ ๅญไธ่ฒ ๅคงๅๅ ๅคงไธๅ ๅฐๅๅ ๅฐไธๅ ๅๆๅป ๅๆ ๅญ ไน่ฒๅฎ็ฏ ่ฟไธๅฏน ๅคฉๅ ๅฐๅ ไบบๅ
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
    """ ้บปๅฐ ASCII ็ ไป126976 ~ 127018
       ๆๅ้กบๅบ๏ผไธๅ่ฅฟๅ๏ผไธญๅ็ฝ๏ผไธๆก็ญ๏ผๆฅๅค็งๅฌ๏ผๆขๅฐ็ซน่

        1. ๅฏนๅๆ็ๅ่ฟ่ก้กบๅญ๏ผflush๏ผๅคๅฎ๏ผ
        ๅฏนไบไผ ๅฅ็ๆ็๏ผowned๏ผ๏ผๅฐๆๆไธๅญ็่ฑ่ฒๆพๅฅๅ่กจ color_WAN ้้ข๏ผ้ๅ color_WAN ๅ่กจไธญ็ๆๆๅ็ด ๏ผๅฆๆๅ่กจไธญๅญๅจๆไธชๅ็ด ๅๅฎ็ไธคไธชๅ็ปงๅ็ด ๏ผๅๅ้กบๅญๅ่กจ๏ผflush๏ผไธญๆทปๅ ่ฏฅๅ็ด ไปฅๅๅฎ็ๅ็ปงใ

        2. ๆฅ็ๅฏนๅๆ็่ฟ่กๅปๅญ๏ผtriplets๏ผๅคๅฎ๏ผ
        ้ๅ color_WAN ๅ่กจไธญ็ๆๆๅ็ด ๏ผๅฆๆๅ่กจไธญๅญๅจไธไธช็ธๅๅ็ด ๏ผๅๅๅปๅญๅ่กจ๏ผtriplets๏ผไธญๆทปๅ ่ฏฅๅ็ด ใ

        3. ็ถๅๅฏนๅๆ็่ฟ่กๅฏนๅญ๏ผdoublets๏ผๅคๅฎ๏ผ
        ้ๅ color_WAN ๅ่กจไธญ็ๆๆๅ็ด ๏ผๅฆๆๅ่กจไธญๅญๅจไธคไธช็ธๅๅ็ด ๏ผๅๅๅฏนๅญๅ่กจ๏ผdoublets๏ผไธญๆทปๅ ่ฏฅๅ็ด ใ

        4. ๆๅ่ฟ่กๆ็้ขๅญๆฐๅคๅฎ๏ผ
        ๅฏนไบไผ ๅฅ็็ขฐ็๏ผpeng๏ผๅๆ ็๏ผgang๏ผๅ่กจ๏ผๅฆๆ่ฟไธคไธชๅ่กจ็้ฟๅบฆๅ ไธ้กบๅญๅ่กจ๏ผflush๏ผ๏ผๅปๅญๅ่กจ๏ผtriplets๏ผๅๅฏนๅญๅ่กจ๏ผdoublets๏ผ็ๆป้ฟๅบฆไธบ 5 ๅ่ฟๅๅ็ๆๆใ

        """
    for a in owned:  # ไผ ๅฅๆ็๏ผ่ทๅไธ็ง่ฑ่ฒ็ๅบๆฐ็็Unicodeๅผๅนถๆพๅฅๅ่กจ
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
    # ไธๅญ Unicode ๅผๅจ126983 ~ 126991้ด
    # ๅคๆญๅไธๅผ ็ๆฏๅฆๆฏ้กบๅญ๏ผๅฆๆunicodeไธญๆฒกๆๅ็ด ไพฟ่ทณๅบๅพช็ฏ๏ผๅฆๆไปๆๅ็ด ๅ
    # ็ปง็ปญๆ ้ๅพช็ฏใๆ นๆฎunicodeๅๅ็ด ๆฐ้็ไธๅ๏ผๅฏๅไธบไปฅไธไธค็งๆๅต๏ผ
    #
    # 1. ๅฏนunicodeๅ3็ไฝ็ญไบ้ถ๏ผๅณ่ฏฅ่ฑ่ฒๆ็ๆ3๏ผ6๏ผ9๏ผ12ๅผ ไธๆฒกๆๅฏนๅญ็ๆถๅ
    # ้ๅunicode้็ๆๆๅ็ด ๏ผๅๅบๅถไธญ็ธ้ป็ไธไธชๅ็ด ๆพๅฅflushๅ่กจไธญ๏ผๅๅฐ่ฟ
    # ไธไธชๅ็ด ไปunicodeๅ่กจไธญ็งป้คใ่ทณๅบ่ฟญไปฃๅพช็ฏ๏ผๆญคๆถๅฆๆunicodeไธญไปๆๅ็ด ๅ
    # ็ปง็ปญๆไปฅไธๆญฅ้ชคๅๆฌกๅพช็ฏใ
    #
    # 2. ๅฏนunicodeๅ3็ไฝ็ญไบ2๏ผๅณ่ฏฅ่ฑ่ฒๆ็ไธญๅญๅจ็ๅฏนๅญใ้ๅunicode้็ๆๆ
    # ๅ็ด ใไนๅ็ๆญฅ้ชคๅ1.ไธญ็ๆญฅ้ชคๅฎๅจไธๆ ท๏ผไป้ๅจๆๅๅ ไธไธไธชๅคๆญๅฏนๅญ็ไปฃ็ ๅใ
    for i in range(4):
        if len(uni_WAN) % 3 == 0:
            for a in uni_WAN:
                # ่ฟ้ๆฏๅคๆญๆ็ไธญๅปๅญๆฐ้็ไปฃ็ ๏ผๅฆๆๅๆ็่ฏฅ่ฑ่ฒไธญๆฒกๆ้กบๅญๅ่ฟๅฅๆญคๅค็่ฟญไปฃๅพช็ฏ๏ผ
                # ไธ่ฟๅจไธ่ฒไธๅ้กบ๏ผๆ่ๅซไธ่ฒไธ่้ซ๏ผ็ๅไธญๅญๅจ็ไธๅฏๅบๆฐๅขๆทปไธไฝ็ๅปๅญ๏ผๆไปฅ
                # ๅจไธ่ฒไธๅ้กบ็ๅๆฐ็ป็ฎไปฃ็ ไธญ๏ผๅช้่ฆ่ฎก็ฎflushๅ่กจไธญๅญไธๅญๅจ็ไธๅฏ็ธๅ็ๅ็ด ๅณๅฏใ
                # ps๏ผๅฆๆๅญๅจ็ๅๅฏ็ธๅ็้กบๅญไพฟๆฏไธ่ฒๅๅ้กบ๏ผๅฆๆๅญๅจ็ๅๅฏๅบๆฐไพๆฌกๅขๆทปไธไฝ
                # ็ๅปๅญไพฟๆฏไธ่ฒๅ่้ซ๏ผๅฆๆๅญๅจ็ๅๅฏๅปๅญๅๆฏ64็ชๅๆๅป๏ผๆณจๆ๏ผๅๆๅปๅชๆๅจ
                # ๅ้ๅฐ็ๆถๅๆๅฏไปฅ้่ฟ้ฒๅฎถ็ๆพ็ฎๆ็ซ๏ผๅถๅฎๆๅตๅช่ฝ่ชๆธ๏ผ้ฒๅฎถๆพ็ฎๅช่ฎกไธๆๅปใ

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

        ''' ๆกๅญ Unicode ็ ไป126992 ~ 127000'''
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

        ''' ็ญๅญ Unicode ็ ไป127001 ~ 127009'''
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
        ''' ้ฃ็ Unicode ็ ไป126976 ~ 126979'''
        for a in all_WINDs:
            if len(all_WINDs) % 3 == 0:
                if all_WINDs.count(a) == 3:
                    chars.append(a * 3)
                    all_WINDs.remove(a)
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

        ''' ็ฎญ็ Unicode ็ ไป126980 ~ 126982'''
        for a in all_ARROWs:
            if len(all_ARROWs) % 3 == 0:
                if all_ARROWs.count(a) == 3:
                    chars.append(a * 3)
                    all_ARROWs.remove(a)
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
    name_sd = "ไธๅฏน"
    name_stars = "ๅคงไธๆ"
    name_flushed = "่ฟไธๅฏน"

    def seven_Doublets(self, owned):
        """่ฟ้ๆฏไธๅฏนๅญ็ๅ็ๅคๅฎ๏ผ็ดๆฅๅคๆญdoubletsๅ่กจ้้ขๆฏๅฆๆ 7ๅฏๅฏนๅญใ
        ๅฆๆ่ฟไบๅฏนๅญๅไธบๅญ็๏ผๅ่ฟๅๅคงไธๆๅคๅฎใๅฆๆ่ฟไบๅฏนๅญๅฝผๆญค็ธ่ฟ๏ผไธไธบๅไธ่ฑ่ฒ
        ๅ่ฟๅ่ฟไธๅฏนๅคๅฎใ"""
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
        """่ฟ้ๆฏๆธไธ่ฒๅ็ๅคๅฎ๏ผๅคๆญ all_groups ๅ่กจ้้ข็ๆๆๅไธชๅญ็ฌฆๅๅฑไบ
        ๅไธ่ฑ่ฒ๏ผ่ฟๅๆธไธ่ฒๅคๅฎใ"""
        for a in owned:
            if a in color_WAN or color_TIAO or color_TONG:
                self.num += 1

        if self.num == 14:
            self.win = True


class CharLess:
    win = False
    num = 0
    score = 1

    def char_less(self, owned):
        """ๆ ๅญๅ็ๅคๅฎ๏ผ้ๅๆ็ๅ่กจ๏ผๅฆๆๅ็ด ไธๅฑไบๅญ็ๅๆฐ้ๅ ไธ๏ผๅฆๆๆฐ้็ญไบๆ็้ฟๅบฆๅๅคๅฎ้่ฟใ"""
        for each in owned:
            if each not in characters:
                self.num += 1

        if self.num == 14:
            self.win = True

class FieldWind:
    win = False
    score = 1

    def field_Wind(self, field):
        """ๅ้ฃๅปๅ็ๅคๅฎ๏ผๅฆๆ้ขๅญๅ่กจไธญๅญๅจ็ไธไธช้ฟๅบฆไธบ 3 ็ๅญ็ฌฆไธฒ๏ผๅฆๆๆฏไธช
        ๅญ็ฌฆ == mahjong.fieldWind ๅ่ฟๅๅ้ฃๅปๅคๅฎใ"""
        for b in all_WINDs:
            if b == field:
                self.win = True


class SideWind(FieldWind):

    def side_Wind(self, side_e, side_s, side_w, side_n):
        """้จ้ฃๅปๅ็ๅคๅฎ๏ผๅฆๆ้ขๅญๅ่กจไธญๅญๅจ็ไธไธช้ฟๅบฆไธบ 3 ็ๅญ็ฌฆไธฒ๏ผๅฆๆๆฏไธช
        ๅญ็ฌฆ == banker.sideWind ๅ่ฟๅ้จ้ฃๅปๅคๅฎใ"""
        if normal:
           for b in chars:
                if b == side_e:
                    return side_e


class ArrowTriplets(SideWind):

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
    def __init__(self):
        self.win = False

    three = False
    score2 = 4
    score3 = 16

    def double_triplets(self):
        """ๅๆๅป๏ผๆฃๆต tripletsๅ่กจ็้ฟๅบฆใ"""
        if len(triplets) == 2:
            self.win = True

    def triple_triplets(self):
        if len(triplets) == 2:
            self.three = False


class PengPeng():
    win = False
    score = 2

    def peng_Peng(self):
        '''็ขฐ็ขฐๅๅ็ๅคๅฎ๏ผๅฆๆ็ฉๅฎถๆพ้ธฃ็้ฃ็ขฐ๏ผ้ฃๆ ๆ้ฃๅ๏ผไธๅปๅญๅ่กจๅ็ขฐ็ๅ่กจ
        ็ๆป้ฟๅบฆไธบ 4 ๅ่ฟๅ็ขฐ็ขฐๅๅคๅฎใ'''
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


class NormalHeight(NumberTriplets):
    four = False
    score = 1
    score3 = 24
    score4 = 48

    def normal_height(self):
        """ไธ่ฌ้ซ็ๅ็ๅคๅฎๅฝๆฐ๏ผ็ดๆฅๅจnormal()ๅฝๆฐ่ฐ็จๅๆฃๆต้กบๅญไธญ็ธๅๅ็ด ็ไธชๆฐใ"""
        for each in flush:
            if flush.count(each) == 2:
                self.win = True

    def same_Flushes_of_One(self):
        """ไธ่ฒไธๅ้กบ็ๅคๅฎ๏ผ้่ฆไธๅน๏ผ่ฑ่ฒๅๅบๆฐ๏ผๅฎๅจ็ธๅ็้กบๅญใ"""
        for each in flush:
            if flush.count(each) == 3:
                self.three = True

    def four_Flushes_of_One(self):
        """ไธ่ฒๅๅ้กบ้่ฆๅๅฏๅฎๅจ็ธๅ็้กบๅญใ"""
        for each in flush:
            if flush.count(each) == 4:
                self.four = True

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
    """้จๅๆธ็ๅคๆญไปฃ็ ๏ผๆฃๆต็ขฐ็ๅ่กจๅๆ ็ๅ่กจๅ็ๅ็ด ไธชๆฐใ"""
    win = False
    score = 2

    def clearing(self):
        if len(pengs) == 0 and len(gangs) == 0:
            self.win = True


class Ordinary():
    """ๅนณๅ็ๅคๅฎ็ฑปไปฅๅๅคๅฎๅฝๆฐ๏ผๆฃๆตflushๅๅ็ด ็ไธชๆฐ๏ผๅๆถๅฐ็ๅฏนๅญไธ่ฝๆฏๅญ็ใ"""
    win = False
    score = 2

    def get_ordinary(self):
        if len(flush) == 4 and doublets[0] not in characters:
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
        if i[0] > 1: # ้่ฆไธไธชๅ้ๅญๅจๆ็ๅบๆฐ
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
    """ไน่ฒๅฎ็ฏ็ๅคๅฎไปฃ็ ใๅฏนไบไผ ๅฅ็ๆ็ owned๏ผๅพช็ฏไน่ฒๅฎ็ฏๅ่กจ lantern ๅ็ๅๅ็ด ๏ผๅๅ่กจๅ็ๅ่กจ
    ่ฟฝๅ ๅ่ฑ่ฒๅ 1~9 ็ๅบๆฐ็๏ผ็ถๅๅฐๅถไธๆ็่ฟ่กๆฏๅฏน๏ผๅฎๅจๅน้ๅณ่ฟๅ True๏ผๅฆๅ่ฟๅ Falseใ"""
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
    
