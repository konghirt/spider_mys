from enum import Enum

class SearchType(Enum):
    LATEST_REPLY =  1  # 最新回复
    LATEST_RELEASE =  2  # 最新发帖
    HOT = 'hot'  # 热门
    GOOD = 'good'  # 精华


class GameType(Enum):
    BH2 = 'https://bbs.mihoyo.com/bh2/home/40'
    BH3 = 'https://bbs.mihoyo.com/bh3/home/4'
    YS = 'https://bbs.mihoyo.com/ys/home/29'
    DBY = 'https://bbs.mihoyo.com/dby/home/39'