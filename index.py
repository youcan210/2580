# ジャンケンゲームについて

# ジャンケン始めます
# 名前を入力してください
# 次の中から選んでください、何を出しますか
# 0:グー、1:チョキ、2:パー
# 数字で入力してください
# コンピューターはパーを出しました
# 結果を勝ちました
import utils
import random

print('-------')
print('ジャンケンを始めます')
player_name = input('名前を入力してください')
print('何を出しますか（0: グー, 1: チョキ, 2: パー）')
playerHand = int(input('数字を入力してください：'))
if utils.validate(playerHand):
  # ランダムにグー、チョキ、パーを出す
  computerHand = random.randint(0,2)
  if player_name == '':
    utils.print_hand(playerHand)

  else:
    utils.print_hand(playerHand,player_name)

  utils.print_hand(computerHand,'コンピューター')

  result = utils.judge(playerHand,computerHand)
  print("結果は" + result + "でした")

else:
  print("正しい数値を入力してください")
