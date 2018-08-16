# encoding=utf-8
import jieba,os

seg_list = jieba.cut("网易智造N520除螨吸尘器", cut_all=True)
print("Full Mode: " + "/ ".join(seg_list))  # 全模式

seg_list = jieba.cut("宇宙沙盘控温被 薄被", cut_all=False)
print("Default Mode: " + "/ ".join(seg_list))  # 精确模式

seg_list = jieba.cut("他来到了网易杭研大厦")  # 默认是精确模式
print(", ".join(seg_list))

seg_list = jieba.cut_for_search("心想智能胶囊咖啡机")  # 搜索引擎模式
for seg in seg_list:
    print(seg)

# 自定义关键词库
jieba.load_userdict('./user_dict.txt')

jieba.add_word('石墨烯')
jieba.add_word('凱特琳')
jieba.del_word('自定义词')

test_sent = (
"李小福是创新办主任也是云计算方面的专家; 什么是八一双鹿\n"
"例如我输入一个带“韩玉赏鉴”的标题，宇宙沙盘控温被 薄被在自定宇宙沙盘控温被 薄被此词为N类\n"
"「台中」正確應該网易智造N520除螨吸尘器不會被切開。mac上可分出「石墨烯」；此時又可以分出來凱特琳了。"
)
words = jieba.lcut('心想智能胶囊咖啡机',cut_all=False)
for word in words:
    if word in jieba.user_word_tag_tab:
        print(word)
print(jieba.user_word_tag_tab.__contains__('薄被'))


# 将所有的产品名进行分词，按词频进行排序并统计，词频较高的作为分类关键词