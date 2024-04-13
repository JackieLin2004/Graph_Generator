import matplotlib.pyplot as plt  # 导入用于绘图的matplotlib库
import jieba  # 导入用于中文分词的jieba库
import wordcloud  # 导入生成词云的wordcloud库


# 统计词频函数
def count_word_frequency(textual, topn):
    # jieba分词库进行中文分词
    words = jieba.lcut(textual.strip())
    # 创建一个空字典，用于存储词频统计结果
    counts = {}
    # 列表生成式获取停用词，停用词列表保存在名为'stop_words.txt'的文件中
    stopwords = [line.strip() for line in open('../WordClouds/stop_words.txt', 'r', encoding='utf-8').readlines()]
    # 用于生成词云的词语列表，避免重复分词,节约运行时间
    word_clear = []

    # 遍历分词后的结果
    for word in words:
        # 如果分词结果长度为1，跳过
        if len(word) == 1:
            continue
        # 如果分词结果不在停用词列表中
        elif word not in stopwords:
            # 将一些同义词替换为同一个词，如凤姐儿、凤姐等
            if word == "凤姐儿":
                word = "凤姐"
            elif word == "林黛玉" or word == "林妹妹" or word == "黛玉笑":
                word == "黛玉"
            elif word == "宝二爷":
                word == "宝玉"
            elif word == "袭人道":
                word == "袭人"
            # 将符合条件的词语添加到用于生成词云的词语列表中
            word_clear.append(word)
            counts[word] = counts.get(word, 0) + 1

    # 将词频统计结果转换为列表
    items = list(counts.items())
    # 按词频从高到低排序
    items.sort(key=lambda x: x[1], reverse=True)
    # 遍历前topn个高频词语
    for i in range(topn):
        word, count = items[i]
        print(f"{word}:{count}")
    # 返回用于生成词云的词语列表
    return word_clear


# 生成词云函数
def generate_word_clouds(txt):
    # 生成词云图，指定背景颜色为红色
    wcloud = wordcloud.WordCloud(font_path=r'../WordClouds/FontStyle.ttf', width=1000, max_words=500, height=1000,
                                 margin=2, background_color='red').generate(txt)
    # 将词云图保存为图片文件
    wcloud.to_file("HLM_word_cloud.png")
    # 显示词云图片
    plt.imshow(wcloud)
    plt.show()


# 读取文本文件内容
text = open('../version/HLM_FullText.txt', "r", encoding='utf-8').read()
# 调用count_word_frequency函数获取前20个高频词语
words_clear = count_word_frequency(text, 20)
# 调用generate_word_clouds函数生成词云图
generate_word_clouds(' '.join(words_clear))
