import random

n = ['伤心的','悲伤的','开心的','欢快的','痛苦的','激动的']
x = ['小明','蜜蜂','猫','狗','小仓鼠','隔壁老王']
m = ['在操场上的','在卫生间里的','在屋顶上的','在教室里的','在泳池里的','在餐馆里的','在公园里的','在垃圾堆里的','图书馆里的']
y = ['篮球架上','讲台上','饭桌前','花洒旁','化石旁','马桶上','乒乓球桌前','兵马俑前','棺材里','船上','床上','电脑前']
z = ['睡觉','唱歌','跳芭蕾舞','跳踢踏舞','跳街舞','打乒乓球','洗澡','游泳','看电视','玩毛线球','采蜜','跑步','翻墙','飞来飞去','演讲']  #建造列表
x = random.choice(x)
m = random.choice(m)
n = random.choice(n)
y = random.choice(y)
z = random.choice(z)    
print("\r\n笑话：" + x + m + y + n + z) 
    
    
