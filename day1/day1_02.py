import datetime, time
import urllib.request

url = "http://www.agkdced.org/board/bbs/board.php?bo_table=16_17&wr_id=13"

f = urllib.request.urlopen(url)
data = f.read().decode('euc-kr') # or euc-kr


begin = data.find("친애하는")
end = data.find("바랍니다.")

end += len("바랍니다.")

print("total=", len(data))
print("begin=", begin)
print(data[begin:begin+100])
print(data[end-100:end])
print("length=", end-begin)

speech = data[begin:end]
speech = speech.replace("=","") # = 을 null로 치환
speech = speech.replace("<br/>","")
speech = speech.split()
#print(speech[:100])

analyze = {}
for word in speech:
    analyze[word] = analyze.get(word, 0) + 1 # get : dic 메소드
                                             # word 가 없으면 0을 return

flist = sorted(analyze.items(), key=lambda kv: kv[1], reverse=True)
print("number of words is ", len(flist))

cnt = 0
for k, v in flist:
    print(k, v)
    if cnt > 100: break
    cnt += 1