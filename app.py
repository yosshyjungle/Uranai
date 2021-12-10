import streamlit as st
import pandas as pd
from datetime import datetime
from PIL import Image

st.title('占いアプリ')
st.write('AIであなたと気になるひとを占ってみよう')

years = st.text_input("あなたの生まれた年を西暦で入力してください（1974年→1974）", 1974)
months = st.text_input('あなたの生まれた月を入力してください。（4月→4）', 4)
days = st.text_input('あなたの生まれた日を入力してください。（2日→2）', 2)


def uranai_start():
	global years
	years = int(years)
	global months
	global days
	df = pd.read_csv(f'data/{years}.csv')
	# st.write(df)
	days = int(days)
	months = int(months)
	meisu = df.iloc[days-1, months]
	meisu = meisu.replace('-', '')
	# st.write(meisu)
	current = datetime.now()
	current_year = current.year
	current_year = int(current_year)

	if (years % 2) == 0:
		even_odd = '金'
	else:
		even_odd = '銀'
	# st.write(even_odd)
	years = int(years)
	age = current_year - years
	# st.write(age)
	global yourType
	# 壮年期（命数３を採用）
	if age > 60:
		if meisu[0:2] < '11':
			print(f'あなたは{even_odd}の羅針盤型です。')
			yourType = f'{even_odd}の羅針盤{meisu[0:2]}'

		elif meisu[0:2] < '21':
			print(f'あなたは{even_odd}のインディアン型です')
			yourType = f'{even_odd}のインディアン{meisu[0:2]}'

		elif meisu[0:2] < '31':
			print(f'あなたは{even_odd}の鳳凰型です')
			yourType = f'{even_odd}の鳳凰{meisu[0:2]}'

		elif meisu[0:2] < '41':
			print(f'あなたは{even_odd}の時計型です')
			yourType = f'{even_odd}の時計{meisu[0:2]}'

		elif meisu[0:2] < '51':
			print(f'あなたは{even_odd}のカメレオン型です')
			yourType = f'{even_odd}のカメレオン{meisu[0:2]}'

		elif meisu[0:2] < '61':
			print(f'あなたは{even_odd}のイルカ型です')
			yourType = f'{even_odd}のイルカ{meisu[0:2]}'
		else:
			print('その他')


	# 青年期（命数２を採用）
	elif age > 30:
		if meisu[2:4] < '11':
			print(f'あなたは{even_odd}の羅針盤型です。')
			yourType = f'{even_odd}の羅針盤{meisu[2:4]}'

		elif meisu[2:4] < '21':
			print(f'あなたは{even_odd}のインディアン型です')
			yourType = f'{even_odd}のインディアン{meisu[2:4]}'

		elif meisu[2:4] < '31':
			print(f'あなたは{even_odd}の鳳凰型です')
			yourType = f'{even_odd}の鳳凰{meisu[2:4]}'

		elif meisu[2:4] < '41':
			print(f'あなたは{even_odd}の時計型です')
			yourType = f'{even_odd}の時計{meisu[2:4]}'

		elif meisu[2:4] < '51':
			print(f'あなたは{even_odd}のカメレオン型です')
			yourType = f'{even_odd}のカメレオン{meisu[2:4]}'

		elif meisu[2:4] < '61':
			print(f'あなたは{even_odd}のイルカ型です')
			yourType = f'{even_odd}のイルカ{meisu[2:4]}'
		else:
			print('その他')

	# 幼年期（命数１を採用）
	elif age > 0:
		if meisu[4:6] < '11':
			print(f'あなたは{even_odd}の羅針盤型です。')
			yourType = f'{even_odd}の羅針盤{meisu[4:6]}'

		elif meisu[4:6] < '21':
			print(f'あなたは{even_odd}のインディアン型です')
			yourType = f'{even_odd}のインディアン{meisu[4:6]}'

		elif meisu[4:6] < '31':
			print(f'あなたは{even_odd}の鳳凰型です')
			yourType = f'{even_odd}の鳳凰{meisu[4:6]}'

		elif meisu[4:6] < '41':
			print(f'あなたは{even_odd}の時計型です')
			yourType = f'{even_odd}の時計{meisu[4:6]}'

		elif meisu[4:6] < '51':
			print(f'あなたは{even_odd}のカメレオン型です')
			yourType = f'{even_odd}のカメレオン{meisu[4:6]}'

		elif meisu[4:6] < '61':
			print(f'あなたは{even_odd}のイルカ型です')
			yourType = f'{even_odd}のイルカ{meisu[4:6]}'
		else:
			print('その他')
	else:
		pass



	img = Image.open(f'images/{yourType[0:-2]}.png')
	st.image(img, use_column_width=True)

	# 羅針盤
	if yourType == '金の羅針盤01':
		with open(f'result/{yourType}.txt', 'r', encoding='utf-8') as f:
			st.write(f.read())
	elif yourType == '金の羅針盤02':
		with open(f'result/{yourType}.txt', 'r', encoding='utf-8') as f:
			st.write(f.read())
	elif yourType == '金の羅針盤03':
		with open(f'result/{yourType}.txt', 'r', encoding='utf-8') as f:
			st.write(f.read())
	elif yourType == '金の羅針盤04':
		with open(f'result/{yourType}.txt', 'r', encoding='utf-8') as f:
			st.write(f.read())
	elif yourType == '金の羅針盤05':
		with open(f'result/{yourType}.txt', 'r', encoding='utf-8') as f:
			st.write(f.read())
	elif yourType == '金の羅針盤06':
		with open(f'result/{yourType}.txt', 'r', encoding='utf-8') as f:
			st.write(f.read())
	elif yourType == '金の羅針盤07':
		with open(f'result/{yourType}.txt', 'r', encoding='utf-8') as f:
			st.write(f.read())
	elif yourType == '金の羅針盤08':
		with open(f'result/{yourType}.txt', 'r', encoding='utf-8') as f:
			st.write(f.read())
	elif yourType == '金の羅針盤09':
		with open(f'result/{yourType}.txt', 'r', encoding='utf-8') as f:
			st.write(f.read())
	elif yourType == '金の羅針盤10':
		with open(f'result/{yourType}.txt', 'r', encoding='utf-8') as f:
			st.write(f.read())

	elif yourType == '銀の羅針盤01':
		with open(f'result/{yourType}.txt', 'r', encoding='utf-8') as f:
			st.write(f.read())
	elif yourType == '銀の羅針盤02':
		with open(f'result/{yourType}.txt', 'r', encoding='utf-8') as f:
			st.write(f.read())
	elif yourType == '銀の羅針盤03':
		with open(f'result/{yourType}.txt', 'r', encoding='utf-8') as f:
			st.write(f.read())
	elif yourType == '銀の羅針盤04':
		with open(f'result/{yourType}.txt', 'r', encoding='utf-8') as f:
			st.write(f.read())
	elif yourType == '銀の羅針盤05':
		with open(f'result/{yourType}.txt', 'r', encoding='utf-8') as f:
			st.write(f.read())
	elif yourType == '銀の羅針盤06':
		with open(f'result/{yourType}.txt', 'r', encoding='utf-8') as f:
			st.write(f.read())
	elif yourType == '銀の羅針盤07':
		with open(f'result/{yourType}.txt', 'r', encoding='utf-8') as f:
			st.write(f.read())
	elif yourType == '銀の羅針盤08':
		with open(f'result/{yourType}.txt', 'r', encoding='utf-8') as f:
			st.write(f.read())
	elif yourType == '銀の羅針盤09':
		with open(f'result/{yourType}.txt', 'r', encoding='utf-8') as f:
			st.write(f.read())
	elif yourType == '銀の羅針盤10':
		with open(f'result/{yourType}.txt', 'r', encoding='utf-8') as f:
			st.write(f.read())

	# 　インディアン
	elif yourType == '金のインディアン11':
		with open(f'result/{yourType}.txt', 'r', encoding='utf-8') as f:
			st.write(f.read())
	elif yourType == '金のインディアン12':
		with open(f'result/{yourType}.txt', 'r', encoding='utf-8') as f:
			st.write(f.read())
	elif yourType == '金のインディアン13':
		with open(f'result/{yourType}.txt', 'r', encoding='utf-8') as f:
			st.write(f.read())
	elif yourType == '金のインディアン14':
		with open(f'result/{yourType}.txt', 'r', encoding='utf-8') as f:
			st.write(f.read())
	elif yourType == '金のインディアン15':
		with open(f'result/{yourType}.txt', 'r', encoding='utf-8') as f:
			st.write(f.read())
	elif yourType == '金のインディアン16':
		with open(f'result/{yourType}.txt', 'r', encoding='utf-8') as f:
			st.write(f.read())
	elif yourType == '金のインディアン17':
		with open(f'result/{yourType}.txt', 'r', encoding='utf-8') as f:
			st.write(f.read())
	elif yourType == '金のインディアン18':
		with open(f'result/{yourType}.txt', 'r', encoding='utf-8') as f:
			st.write(f.read())
	elif yourType == '金のインディアン19':
		with open(f'result/{yourType}.txt', 'r', encoding='utf-8') as f:
			st.write(f.read())
	elif yourType == '金のインディアン20':
		with open(f'result/{yourType}.txt', 'r', encoding='utf-8') as f:
			st.write(f.read())

	elif yourType == '銀のインディアン11':
		with open(f'result/{yourType}.txt', 'r', encoding='utf-8') as f:
			st.write(f.read())
	elif yourType == '銀のインディアン12':
		with open(f'result/{yourType}.txt', 'r', encoding='utf-8') as f:
			st.write(f.read())
	elif yourType == '銀のインディアン13':
		with open(f'result/{yourType}.txt', 'r', encoding='utf-8') as f:
			st.write(f.read())
	elif yourType == '銀のインディアン14':
		with open(f'result/{yourType}.txt', 'r', encoding='utf-8') as f:
			st.write(f.read())
	elif yourType == '銀のインディアン15':
		with open(f'result/{yourType}.txt', 'r', encoding='utf-8') as f:
			st.write(f.read())
	elif yourType == '銀のインディアン16':
		with open(f'result/{yourType}.txt', 'r', encoding='utf-8') as f:
			st.write(f.read())
	elif yourType == '銀のインディアン17':
		with open(f'result/{yourType}.txt', 'r', encoding='utf-8') as f:
			st.write(f.read())
	elif yourType == '銀のインディアン18':
		with open(f'result/{yourType}.txt', 'r', encoding='utf-8') as f:
			st.write(f.read())
	elif yourType == '銀のインディアン19':
		with open(f'result/{yourType}.txt', 'r', encoding='utf-8') as f:
			st.write(f.read())
	elif yourType == '銀のインディアン20':
		with open(f'result/{yourType}.txt', 'r', encoding='utf-8') as f:
			st.write(f.read())

	# 　鳳凰
	elif yourType == '金の鳳凰21':
		with open(f'result/{yourType}.txt', 'r', encoding='utf-8') as f:
			st.write(f.read())
	elif yourType == '金の鳳凰22':
		with open(f'result/{yourType}.txt', 'r', encoding='utf-8') as f:
			st.write(f.read())
	elif yourType == '金の鳳凰23':
		with open(f'result/{yourType}.txt', 'r', encoding='utf-8') as f:
			st.write(f.read())
	elif yourType == '金の鳳凰24':
		with open(f'result/{yourType}.txt', 'r', encoding='utf-8') as f:
			st.write(f.read())
	elif yourType == '金の鳳凰25':
		with open(f'result/{yourType}.txt', 'r', encoding='utf-8') as f:
			st.write(f.read())
	elif yourType == '金の鳳凰26':
		with open(f'result/{yourType}.txt', 'r', encoding='utf-8') as f:
			st.write(f.read())
	elif yourType == '金の鳳凰27':
		with open(f'result/{yourType}.txt', 'r', encoding='utf-8') as f:
			st.write(f.read())
	elif yourType == '金の鳳凰28':
		with open(f'result/{yourType}.txt', 'r', encoding='utf-8') as f:
			st.write(f.read())
	elif yourType == '金の鳳凰29':
		with open(f'result/{yourType}.txt', 'r', encoding='utf-8') as f:
			st.write(f.read())
	elif yourType == '金の鳳凰30':
		with open(f'result/{yourType}.txt', 'r', encoding='utf-8') as f:
			st.write(f.read())

	elif yourType == '銀の鳳凰21':
		with open(f'result/{yourType}.txt', 'r', encoding='utf-8') as f:
			st.write(f.read())
	elif yourType == '銀の鳳凰22':
		with open(f'result/{yourType}.txt', 'r', encoding='utf-8') as f:
			st.write(f.read())
	elif yourType == '銀の鳳凰23':
		with open(f'result/{yourType}.txt', 'r', encoding='utf-8') as f:
			st.write(f.read())
	elif yourType == '銀の鳳凰24':
		with open(f'result/{yourType}.txt', 'r', encoding='utf-8') as f:
			st.write(f.read())
	elif yourType == '銀の鳳凰25':
		with open(f'result/{yourType}.txt', 'r', encoding='utf-8') as f:
			st.write(f.read())
	elif yourType == '銀の鳳凰26':
		with open(f'result/{yourType}.txt', 'r', encoding='utf-8') as f:
			st.write(f.read())
	elif yourType == '銀の鳳凰27':
		with open(f'result/{yourType}.txt', 'r', encoding='utf-8') as f:
			st.write(f.read())
	elif yourType == '銀の鳳凰28':
		with open(f'result/{yourType}.txt', 'r', encoding='utf-8') as f:
			st.write(f.read())
	elif yourType == '銀の鳳凰29':
		with open(f'result/{yourType}.txt', 'r', encoding='utf-8') as f:
			st.write(f.read())
	elif yourType == '銀の鳳凰30':
		with open(f'result/{yourType}.txt', 'r', encoding='utf-8') as f:
			st.write(f.read())


	# 　時計
	elif yourType == '金の時計31':
		with open(f'result/{yourType}.txt', 'r', encoding='utf-8') as f:
			st.write(f.read())
	elif yourType == '金の時計32':
		with open(f'result/{yourType}.txt', 'r', encoding='utf-8') as f:
			st.write(f.read())
	elif yourType == '金の時計33':
		with open(f'result/{yourType}.txt', 'r', encoding='utf-8') as f:
			st.write(f.read())
	elif yourType == '金の時計34':
		with open(f'result/{yourType}.txt', 'r', encoding='utf-8') as f:
			st.write(f.read())
	elif yourType == '金の時計35':
		with open(f'result/{yourType}.txt', 'r', encoding='utf-8') as f:
			st.write(f.read())
	elif yourType == '金の時計36':
		with open(f'result/{yourType}.txt', 'r', encoding='utf-8') as f:
			st.write(f.read())
	elif yourType == '金の時計37':
		with open(f'result/{yourType}.txt', 'r', encoding='utf-8') as f:
			st.write(f.read())
	elif yourType == '金の時計38':
		with open(f'result/{yourType}.txt', 'r', encoding='utf-8') as f:
			st.write(f.read())
	elif yourType == '金の時計39':
		with open(f'result/{yourType}.txt', 'r', encoding='utf-8') as f:
			st.write(f.read())
	elif yourType == '金の時計40':
		with open(f'result/{yourType}.txt', 'r', encoding='utf-8') as f:
			st.write(f.read())

	elif yourType == '銀の時計31':
		with open(f'result/{yourType}.txt', 'r', encoding='utf-8') as f:
			st.write(f.read())
	elif yourType == '銀の時計32':
		with open(f'result/{yourType}.txt', 'r', encoding='utf-8') as f:
			st.write(f.read())
	elif yourType == '銀の時計33':
		with open(f'result/{yourType}.txt', 'r', encoding='utf-8') as f:
			st.write(f.read())
	elif yourType == '銀の時計34':
		with open(f'result/{yourType}.txt', 'r', encoding='utf-8') as f:
			st.write(f.read())
	elif yourType == '銀の時計35':
		with open(f'result/{yourType}.txt', 'r', encoding='utf-8') as f:
			st.write(f.read())
	elif yourType == '銀の時計36':
		with open(f'result/{yourType}.txt', 'r', encoding='utf-8') as f:
			st.write(f.read())
	elif yourType == '銀の時計37':
		with open(f'result/{yourType}.txt', 'r', encoding='utf-8') as f:
			st.write(f.read())
	elif yourType == '銀の時計38':
		with open(f'result/{yourType}.txt', 'r', encoding='utf-8') as f:
			st.write(f.read())
	elif yourType == '銀の時計39':
		with open(f'result/{yourType}.txt', 'r', encoding='utf-8') as f:
			st.write(f.read())
	elif yourType == '銀の時計40':
		with open(f'result/{yourType}.txt', 'r', encoding='utf-8') as f:
			st.write(f.read())

	# カメレオン
	elif yourType == '金のカメレオン41':
		with open(f'result/{yourType}.txt', 'r', encoding='utf-8') as f:
			st.write(f.read())
	elif yourType == '金のカメレオン42':
		with open(f'result/{yourType}.txt', 'r', encoding='utf-8') as f:
			st.write(f.read())
	elif yourType == '金のカメレオン43':
		with open(f'result/{yourType}.txt', 'r', encoding='utf-8') as f:
			st.write(f.read())
	elif yourType == '金のカメレオン44':
		with open(f'result/{yourType}.txt', 'r', encoding='utf-8') as f:
			st.write(f.read())
	elif yourType == '金のカメレオン45':
		with open(f'result/{yourType}.txt', 'r', encoding='utf-8') as f:
			st.write(f.read())
	elif yourType == '金のカメレオン46':
		with open(f'result/{yourType}.txt', 'r', encoding='utf-8') as f:
			st.write(f.read())
	elif yourType == '金のカメレオン47':
		with open(f'result/{yourType}.txt', 'r', encoding='utf-8') as f:
			st.write(f.read())
	elif yourType == '金のカメレオン48':
		with open(f'result/{yourType}.txt', 'r', encoding='utf-8') as f:
			st.write(f.read())
	elif yourType == '金のカメレオン49':
		with open(f'result/{yourType}.txt', 'r', encoding='utf-8') as f:
			st.write(f.read())
	elif yourType == '金のカメレオン50':
		with open(f'result/{yourType}.txt', 'r', encoding='utf-8') as f:
			st.write(f.read())

	elif yourType == '銀のカメレオン41':
		with open(f'result/{yourType}.txt', 'r', encoding='utf-8') as f:
			st.write(f.read())
	elif yourType == '銀のカメレオン42':
		with open(f'result/{yourType}.txt', 'r', encoding='utf-8') as f:
			st.write(f.read())
	elif yourType == '銀のカメレオン43':
		with open(f'result/{yourType}.txt', 'r', encoding='utf-8') as f:
			st.write(f.read())
	elif yourType == '銀のカメレオン44':
		with open(f'result/{yourType}.txt', 'r', encoding='utf-8') as f:
			st.write(f.read())
	elif yourType == '銀のカメレオン45':
		with open(f'result/{yourType}.txt', 'r', encoding='utf-8') as f:
			st.write(f.read())
	elif yourType == '銀のカメレオン46':
		with open(f'result/{yourType}.txt', 'r', encoding='utf-8') as f:
			st.write(f.read())
	elif yourType == '銀のカメレオン47':
		with open(f'result/{yourType}.txt', 'r', encoding='utf-8') as f:
			st.write(f.read())
	elif yourType == '銀のカメレオン48':
		with open(f'result/{yourType}.txt', 'r', encoding='utf-8') as f:
			st.write(f.read())
	elif yourType == '銀のカメレオン49':
		with open(f'result/{yourType}.txt', 'r', encoding='utf-8') as f:
			st.write(f.read())
	elif yourType == '銀のカメレオン50':
		with open(f'result/{yourType}.txt', 'r', encoding='utf-8') as f:
			st.write(f.read())

	# イルカ
	elif yourType == '金のイルカ51':
		with open(f'result/{yourType}.txt', 'r', encoding='utf-8') as f:
			st.write(f.read())
	elif yourType == '金のイルカ52':
		with open(f'result/{yourType}.txt', 'r', encoding='utf-8') as f:
			st.write(f.read())
	elif yourType == '金のイルカ53':
		with open(f'result/{yourType}.txt', 'r', encoding='utf-8') as f:
			st.write(f.read())
	elif yourType == '金のイルカ54':
		with open(f'result/{yourType}.txt', 'r', encoding='utf-8') as f:
			st.write(f.read())
	elif yourType == '金のイルカ55':
		with open(f'result/{yourType}.txt', 'r', encoding='utf-8') as f:
			st.write(f.read())
	elif yourType == '金のイルカ56':
		with open(f'result/{yourType}.txt', 'r', encoding='utf-8') as f:
			st.write(f.read())
	elif yourType == '金のイルカ57':
		with open(f'result/{yourType}.txt', 'r', encoding='utf-8') as f:
			st.write(f.read())
	elif yourType == '金のイルカ58':
		with open(f'result/{yourType}.txt', 'r', encoding='utf-8') as f:
			st.write(f.read())
	elif yourType == '金のイルカ59':
		with open(f'result/{yourType}.txt', 'r', encoding='utf-8') as f:
			st.write(f.read())
	elif yourType == '金のイルカ60':
		with open(f'result/{yourType}.txt', 'r', encoding='utf-8') as f:
			st.write(f.read())

	elif yourType == '銀のイルカ51':
		with open(f'result/{yourType}.txt', 'r', encoding='utf-8') as f:
			st.write(f.read())
	elif yourType == '銀のイルカ52':
		with open(f'result/{yourType}.txt', 'r', encoding='utf-8') as f:
			st.write(f.read())
	elif yourType == '銀のイルカ53':
		with open(f'result/{yourType}.txt', 'r', encoding='utf-8') as f:
			st.write(f.read())
	elif yourType == '銀のイルカ54':
		with open(f'result/{yourType}.txt', 'r', encoding='utf-8') as f:
			st.write(f.read())
	elif yourType == '銀のイルカ55':
		with open(f'result/{yourType}.txt', 'r', encoding='utf-8') as f:
			st.write(f.read())
	elif yourType == '銀のイルカ56':
		with open(f'result/{yourType}.txt', 'r', encoding='utf-8') as f:
			st.write(f.read())
	elif yourType == '銀のイルカ57':
		with open(f'result/{yourType}.txt', 'r', encoding='utf-8') as f:
			st.write(f.read())
	elif yourType == '銀のイルカ58':
		with open(f'result/{yourType}.txt', 'r', encoding='utf-8') as f:
			st.write(f.read())
	elif yourType == '銀のイルカ59':
		with open(f'result/{yourType}.txt', 'r', encoding='utf-8') as f:
			st.write(f.read())
	elif yourType == '銀のイルカ60':
		with open(f'result/{yourType}.txt', 'r', encoding='utf-8') as f:
			st.write(f.read())
	else:
		pass


if st.button('あなたを占う'):
	uranai_start()
