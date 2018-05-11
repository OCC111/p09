import time
renwu = 1
job = 1
caoyao = 1
turn = 1
bug = 1
baoshi = 1
cat = 1
while renwu <=1:
    renwu = renwu+1
    print ("亲爱的，快去签到哦!")
    time.sleep(2)
while job <=1:
    print ("二嘎子，师傅叫你上山采草药")
    job = job+1
    time.sleep(2)
while caoyao <=10:
    print ("二嘎子正在采药中.....第%d个" % caoyao)
    caoyao = caoyao+1
    time.sleep(2)

while turn <=1:
    print ("师傅我回来啦！")
    turn = turn+1
    time.sleep(2)

while bug <=1:
    print ("二嘎子快给为师收集碎片！")
    bug = bug+1
    time.sleep(2)

while baoshi <=1000:
    print ("正在刷取T3创世之神合成碎片......第%d个" % baoshi)
    baoshi = baoshi+1
    time.sleep(0.5)

while cat <=1000:
    print ("正在刷取A车融合材料......第%d个" % cat)
    cat = cat+1
    time.sleep(0.5)
