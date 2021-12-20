import streamlit as st
import pandas as pd
from datetime import datetime
from PIL import Image

# st.title('占いアプリ')
img_title = Image.open(f'images/title.png')
st.image(img_title, use_column_width=True)

st.write('AIであなたと気になるひとを占ってみよう')

st.subheader('あなたを占います')

years = st.text_input("あなたの生まれた年を西暦で入力してください（1974年→1974）", 1974)
months = st.text_input('あなたの生まれた月を入力してください。（4月→4）', 4)
days = st.text_input('あなたの生まれた日を入力してください。（2日→2）', 2)
sex = st.radio('あなたの性別は？', ['男', '女', 'どちらでもない'])

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

#相性診断
st.subheader('相性診断')
p_years = st.text_input("相性を知りたい方の生まれた年を西暦で入力してください（1974年→1975）", 1975)
p_months = st.text_input('相性を知りたい方の生まれた月を入力してください。（7月→7）', 7)
p_days = st.text_input('相性を知りたい方の生まれた日を入力してください。（9日→9）', 9)
p_sex = st.radio('相性を知りたい方の性別は？', ['男', '女', 'どちらでもない'])

def p_uranai_start():
	#自分を再取得
	global years
	years = int(years)
	global months
	global days
	df = pd.read_csv(f'data/{years}.csv')
	# st.write(df)
	days = int(days)
	months = int(months)
	meisu = df.iloc[days - 1, months]
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

	#パートナーのデータ読み込み
	global p_years
	global p_months
	global p_days
	p_months = int(p_months)
	p_days = int(p_days)
	p_df = pd.read_csv(f'data/{p_years}.csv')
	p_meisu = p_df.iloc[p_days-1, p_months]
	p_meisu = p_meisu.replace('-', '')
	p_years = int(p_years)
	current = datetime.now()
	current_year = current.year
	current_year = int(current_year)
	if (p_years % 2) == 0:
		p_even_odd = '金'
	else:
		p_even_odd = '銀'
	p_years = int(p_years)
	p_age = current_year - p_years
	global p_yourType
	global p_Type
	# 壮年期（命数３を採用）
	if p_age > 60:
		if p_meisu[0:2] < '11':
			print(f'相性を知りたい方は{p_even_odd}の羅針盤型です。')
			p_yourType = f'{p_even_odd}の羅針盤{p_meisu[0:2]}'

		elif p_meisu[0:2] < '21':
			print(f'相性を知りたい方は{p_even_odd}のインディアン型です')
			p_yourType = f'{p_even_odd}のインディアン{p_meisu[0:2]}'

		elif p_meisu[0:2] < '31':
			print(f'相性を知りたい方は{p_even_odd}の鳳凰型です')
			p_yourType = f'{p_even_odd}の鳳凰{p_meisu[0:2]}'

		elif p_meisu[0:2] < '41':
			print(f'相性を知りたい方は{p_even_odd}の時計型です')
			p_yourType = f'{p_even_odd}の時計{p_meisu[0:2]}'

		elif p_meisu[0:2] < '51':
			print(f'相性を知りたい方は{p_even_odd}のカメレオン型です')
			p_yourType = f'{p_even_odd}のカメレオン{p_meisu[0:2]}'

		elif p_meisu[0:2] < '61':
			print(f'相性を知りたい方は{p_even_odd}のイルカ型です')
			p_yourType = f'{p_even_odd}のイルカ{p_meisu[0:2]}'
		else:
			print('その他')

	# 青年期（命数２を採用）
	elif p_age > 30:
		if p_meisu[2:4] < '11':
			print(f'相性を知りたい方は{p_even_odd}の羅針盤型です。')
			p_yourType = f'{p_even_odd}の羅針盤{p_meisu[2:4]}'

		elif p_meisu[2:4] < '21':
			print(f'相性を知りたい方は{p_even_odd}のインディアン型です')
			p_yourType = f'{p_even_odd}のインディアン{p_meisu[2:4]}'

		elif p_meisu[2:4] < '31':
			print(f'相性を知りたい方は{p_even_odd}の鳳凰型です')
			p_yourType = f'{p_even_odd}の鳳凰{p_meisu[2:4]}'

		elif p_meisu[2:4] < '41':
			print(f'相性を知りたい方は{p_even_odd}の時計型です')
			p_yourType = f'{p_even_odd}の時計{p_meisu[2:4]}'

		elif p_meisu[2:4] < '51':
			print(f'相性を知りたい方は{p_even_odd}のカメレオン型です')
			p_yourType = f'{p_even_odd}のカメレオン{p_meisu[2:4]}'

		elif p_meisu[2:4] < '61':
			print(f'相性を知りたい方は{p_even_odd}のイルカ型です')
			p_yourType = f'{p_even_odd}のイルカ{p_meisu[2:4]}'
		else:
			print('その他')

	# 幼年期（命数１を採用）
	elif p_age > 0:
		if p_meisu[4:6] < '11':
			print(f'相性を知りたい方は{p_even_odd}の羅針盤型です。')
			p_yourType = f'{p_even_odd}の羅針盤{p_meisu[4:6]}'

		elif p_meisu[4:6] < '21':
			print(f'相性を知りたい方は{p_even_odd}のインディアン型です')
			p_yourType = f'{p_even_odd}のインディアン{p_meisu[4:6]}'

		elif p_meisu[4:6] < '31':
			print(f'相性を知りたい方は{p_even_odd}の鳳凰型です')
			p_yourType = f'{p_even_odd}の鳳凰{p_meisu[4:6]}'

		elif p_meisu[4:6] < '41':
			print(f'相性を知りたい方は{p_even_odd}の時計型です')
			p_yourType = f'{p_even_odd}の時計{p_meisu[4:6]}'

		elif p_meisu[4:6] < '51':
			print(f'相性を知りたい方は{p_even_odd}のカメレオン型です')
			p_yourType = f'{p_even_odd}のカメレオン{p_meisu[4:6]}'

		elif p_meisu[4:6] < '61':
			print(f'相性を知りたい方は{p_even_odd}のイルカ型です')
			p_yourType = f'{p_even_odd}のイルカ{p_meisu[4:6]}'
		else:
			print('その他')
	else:
		pass

	p_Type = p_yourType[0:-2]
	p_img = Image.open(f'images/{p_yourType[0:-2]}.png')
	st.image(p_img, use_column_width=True)


	if yourType[0:-2] == '金の羅針盤':
		if p_Type == '金の羅針盤':
			with open(f'p_Type/{yourType[0:-2]}/{p_Type}.txt', 'r', encoding='utf-8') as f:
				st.write(f.read())
		elif p_Type == '銀の羅針盤':
			with open(f'p_Type/{yourType[0:-2]}/{p_Type}.txt', 'r', encoding='utf-8') as f:
				st.write(f.read())
		elif p_Type == '金のインディアン':
			with open(f'p_Type/{yourType[0:-2]}/{p_Type}.txt', 'r', encoding='utf-8') as f:
				st.write(f.read())
		elif p_Type == '銀のインディアン':
			with open(f'p_Type/{yourType[0:-2]}/{p_Type}.txt', 'r', encoding='utf-8') as f:
				st.write(f.read())
		elif p_Type == '金の鳳凰':
			with open(f'p_Type/{yourType[0:-2]}/{p_Type}.txt', 'r', encoding='utf-8') as f:
				st.write(f.read())
		elif p_Type == '銀の鳳凰':
			with open(f'p_Type/{yourType[0:-2]}/{p_Type}.txt', 'r', encoding='utf-8') as f:
				st.write(f.read())
		elif p_Type == '金の時計':
			with open(f'p_Type/{yourType[0:-2]}/{p_Type}.txt', 'r', encoding='utf-8') as f:
				st.write(f.read())
		elif p_Type == '銀の時計':
			with open(f'p_Type/{yourType[0:-2]}/{p_Type}.txt', 'r', encoding='utf-8') as f:
				st.write(f.read())
		elif p_Type == '金のカメレオン':
			with open(f'p_Type/{yourType[0:-2]}/{p_Type}.txt', 'r', encoding='utf-8') as f:
				st.write(f.read())
		elif p_Type == '銀のカメレオン':
			with open(f'p_Type/{yourType[0:-2]}/{p_Type}.txt', 'r', encoding='utf-8') as f:
				st.write(f.read())
		elif p_Type == '金のイルカ':
			with open(f'p_Type/{yourType[0:-2]}/{p_Type}.txt', 'r', encoding='utf-8') as f:
				st.write(f.read())
		elif p_Type == '銀のイルカ':
			with open(f'p_Type/{yourType[0:-2]}/{p_Type}.txt', 'r', encoding='utf-8') as f:
				st.write(f.read())
	elif yourType[0:-2] == '銀の羅針盤':
		if p_Type == '金の羅針盤':
			with open(f'p_Type/{yourType[0:-2]}/{p_Type}.txt', 'r', encoding='utf-8') as f:
				st.write(f.read())
		elif p_Type == '銀の羅針盤':
			with open(f'p_Type/{yourType[0:-2]}/{p_Type}.txt', 'r', encoding='utf-8') as f:
				st.write(f.read())
		elif p_Type == '金のインディアン':
			with open(f'p_Type/{yourType[0:-2]}/{p_Type}.txt', 'r', encoding='utf-8') as f:
				st.write(f.read())
		elif p_Type == '銀のインディアン':
			with open(f'p_Type/{yourType[0:-2]}/{p_Type}.txt', 'r', encoding='utf-8') as f:
				st.write(f.read())
		elif p_Type == '金の鳳凰':
			with open(f'p_Type/{yourType[0:-2]}/{p_Type}.txt', 'r', encoding='utf-8') as f:
				st.write(f.read())
		elif p_Type == '銀の鳳凰':
			with open(f'p_Type/{yourType[0:-2]}/{p_Type}.txt', 'r', encoding='utf-8') as f:
				st.write(f.read())
		elif p_Type == '金の時計':
			with open(f'p_Type/{yourType[0:-2]}/{p_Type}.txt', 'r', encoding='utf-8') as f:
				st.write(f.read())
		elif p_Type == '銀の時計':
			with open(f'p_Type/{yourType[0:-2]}/{p_Type}.txt', 'r', encoding='utf-8') as f:
				st.write(f.read())
		elif p_Type == '金のカメレオン':
			with open(f'p_Type/{yourType[0:-2]}/{p_Type}.txt', 'r', encoding='utf-8') as f:
				st.write(f.read())
		elif p_Type == '銀のカメレオン':
			with open(f'p_Type/{yourType[0:-2]}/{p_Type}.txt', 'r', encoding='utf-8') as f:
				st.write(f.read())
		elif p_Type == '金のイルカ':
			with open(f'p_Type/{yourType[0:-2]}/{p_Type}.txt', 'r', encoding='utf-8') as f:
				st.write(f.read())
		elif p_Type == '銀のイルカ':
			with open(f'p_Type/{yourType[0:-2]}/{p_Type}.txt', 'r', encoding='utf-8') as f:
				st.write(f.read())
	elif yourType[0:-2] == '金のインディアン':
		if p_Type == '金の羅針盤':
			with open(f'p_Type/{yourType[0:-2]}/{p_Type}.txt', 'r', encoding='utf-8') as f:
				st.write(f.read())
		elif p_Type == '銀の羅針盤':
			with open(f'p_Type/{yourType[0:-2]}/{p_Type}.txt', 'r', encoding='utf-8') as f:
				st.write(f.read())
		elif p_Type == '金のインディアン':
			with open(f'p_Type/{yourType[0:-2]}/{p_Type}.txt', 'r', encoding='utf-8') as f:
				st.write(f.read())
		elif p_Type == '銀のインディアン':
			with open(f'p_Type/{yourType[0:-2]}/{p_Type}.txt', 'r', encoding='utf-8') as f:
				st.write(f.read())
		elif p_Type == '金の鳳凰':
			with open(f'p_Type/{yourType[0:-2]}/{p_Type}.txt', 'r', encoding='utf-8') as f:
				st.write(f.read())
		elif p_Type == '銀の鳳凰':
			with open(f'p_Type/{yourType[0:-2]}/{p_Type}.txt', 'r', encoding='utf-8') as f:
				st.write(f.read())
		elif p_Type == '金の時計':
			with open(f'p_Type/{yourType[0:-2]}/{p_Type}.txt', 'r', encoding='utf-8') as f:
				st.write(f.read())
		elif p_Type == '銀の時計':
			with open(f'p_Type/{yourType[0:-2]}/{p_Type}.txt', 'r', encoding='utf-8') as f:
				st.write(f.read())
		elif p_Type == '金のカメレオン':
			with open(f'p_Type/{yourType[0:-2]}/{p_Type}.txt', 'r', encoding='utf-8') as f:
				st.write(f.read())
		elif p_Type == '銀のカメレオン':
			with open(f'p_Type/{yourType[0:-2]}/{p_Type}.txt', 'r', encoding='utf-8') as f:
				st.write(f.read())
		elif p_Type == '金のイルカ':
			with open(f'p_Type/{yourType[0:-2]}/{p_Type}.txt', 'r', encoding='utf-8') as f:
				st.write(f.read())
		elif p_Type == '銀のイルカ':
			with open(f'p_Type/{yourType[0:-2]}/{p_Type}.txt', 'r', encoding='utf-8') as f:
				st.write(f.read())
	elif yourType[0:-2] == '銀のインディアン':
		if p_Type == '金の羅針盤':
			with open(f'p_Type/{yourType[0:-2]}/{p_Type}.txt', 'r', encoding='utf-8') as f:
				st.write(f.read())
		elif p_Type == '銀の羅針盤':
			with open(f'p_Type/{yourType[0:-2]}/{p_Type}.txt', 'r', encoding='utf-8') as f:
				st.write(f.read())
		elif p_Type == '金のインディアン':
			with open(f'p_Type/{yourType[0:-2]}/{p_Type}.txt', 'r', encoding='utf-8') as f:
				st.write(f.read())
		elif p_Type == '銀のインディアン':
			with open(f'p_Type/{yourType[0:-2]}/{p_Type}.txt', 'r', encoding='utf-8') as f:
				st.write(f.read())
		elif p_Type == '金の鳳凰':
			with open(f'p_Type/{yourType[0:-2]}/{p_Type}.txt', 'r', encoding='utf-8') as f:
				st.write(f.read())
		elif p_Type == '銀の鳳凰':
			with open(f'p_Type/{yourType[0:-2]}/{p_Type}.txt', 'r', encoding='utf-8') as f:
				st.write(f.read())
		elif p_Type == '金の時計':
			with open(f'p_Type/{yourType[0:-2]}/{p_Type}.txt', 'r', encoding='utf-8') as f:
				st.write(f.read())
		elif p_Type == '銀の時計':
			with open(f'p_Type/{yourType[0:-2]}/{p_Type}.txt', 'r', encoding='utf-8') as f:
				st.write(f.read())
		elif p_Type == '金のカメレオン':
			with open(f'p_Type/{yourType[0:-2]}/{p_Type}.txt', 'r', encoding='utf-8') as f:
				st.write(f.read())
		elif p_Type == '銀のカメレオン':
			with open(f'p_Type/{yourType[0:-2]}/{p_Type}.txt', 'r', encoding='utf-8') as f:
				st.write(f.read())
		elif p_Type == '金のイルカ':
			with open(f'p_Type/{yourType[0:-2]}/{p_Type}.txt', 'r', encoding='utf-8') as f:
				st.write(f.read())
		elif p_Type == '銀のイルカ':
			with open(f'p_Type/{yourType[0:-2]}/{p_Type}.txt', 'r', encoding='utf-8') as f:
				st.write(f.read())
	elif yourType[0:-2] == '金の鳳凰':
		if p_Type == '金の羅針盤':
			with open(f'p_Type/{yourType[0:-2]}/{p_Type}.txt', 'r', encoding='utf-8') as f:
				st.write(f.read())
		elif p_Type == '銀の羅針盤':
			with open(f'p_Type/{yourType[0:-2]}/{p_Type}.txt', 'r', encoding='utf-8') as f:
				st.write(f.read())
		elif p_Type == '金のインディアン':
			with open(f'p_Type/{yourType[0:-2]}/{p_Type}.txt', 'r', encoding='utf-8') as f:
				st.write(f.read())
		elif p_Type == '銀のインディアン':
			with open(f'p_Type/{yourType[0:-2]}/{p_Type}.txt', 'r', encoding='utf-8') as f:
				st.write(f.read())
		elif p_Type == '金の鳳凰':
			with open(f'p_Type/{yourType[0:-2]}/{p_Type}.txt', 'r', encoding='utf-8') as f:
				st.write(f.read())
		elif p_Type == '銀の鳳凰':
			with open(f'p_Type/{yourType[0:-2]}/{p_Type}.txt', 'r', encoding='utf-8') as f:
				st.write(f.read())
		elif p_Type == '金の時計':
			with open(f'p_Type/{yourType[0:-2]}/{p_Type}.txt', 'r', encoding='utf-8') as f:
				st.write(f.read())
		elif p_Type == '銀の時計':
			with open(f'p_Type/{yourType[0:-2]}/{p_Type}.txt', 'r', encoding='utf-8') as f:
				st.write(f.read())
		elif p_Type == '金のカメレオン':
			with open(f'p_Type/{yourType[0:-2]}/{p_Type}.txt', 'r', encoding='utf-8') as f:
				st.write(f.read())
		elif p_Type == '銀のカメレオン':
			with open(f'p_Type/{yourType[0:-2]}/{p_Type}.txt', 'r', encoding='utf-8') as f:
				st.write(f.read())
		elif p_Type == '金のイルカ':
			with open(f'p_Type/{yourType[0:-2]}/{p_Type}.txt', 'r', encoding='utf-8') as f:
				st.write(f.read())
		elif p_Type == '銀のイルカ':
			with open(f'p_Type/{yourType[0:-2]}/{p_Type}.txt', 'r', encoding='utf-8') as f:
				st.write(f.read())
	elif yourType[0:-2] == '銀の鳳凰':
		if p_Type == '金の羅針盤':
			with open(f'p_Type/{yourType[0:-2]}/{p_Type}.txt', 'r', encoding='utf-8') as f:
				st.write(f.read())
		elif p_Type == '銀の羅針盤':
			with open(f'p_Type/{yourType[0:-2]}/{p_Type}.txt', 'r', encoding='utf-8') as f:
				st.write(f.read())
		elif p_Type == '金のインディアン':
			with open(f'p_Type/{yourType[0:-2]}/{p_Type}.txt', 'r', encoding='utf-8') as f:
				st.write(f.read())
		elif p_Type == '銀のインディアン':
			with open(f'p_Type/{yourType[0:-2]}/{p_Type}.txt', 'r', encoding='utf-8') as f:
				st.write(f.read())
		elif p_Type == '金の鳳凰':
			with open(f'p_Type/{yourType[0:-2]}/{p_Type}.txt', 'r', encoding='utf-8') as f:
				st.write(f.read())
		elif p_Type == '銀の鳳凰':
			with open(f'p_Type/{yourType[0:-2]}/{p_Type}.txt', 'r', encoding='utf-8') as f:
				st.write(f.read())
		elif p_Type == '金の時計':
			with open(f'p_Type/{yourType[0:-2]}/{p_Type}.txt', 'r', encoding='utf-8') as f:
				st.write(f.read())
		elif p_Type == '銀の時計':
			with open(f'p_Type/{yourType[0:-2]}/{p_Type}.txt', 'r', encoding='utf-8') as f:
				st.write(f.read())
		elif p_Type == '金のカメレオン':
			with open(f'p_Type/{yourType[0:-2]}/{p_Type}.txt', 'r', encoding='utf-8') as f:
				st.write(f.read())
		elif p_Type == '銀のカメレオン':
			with open(f'p_Type/{yourType[0:-2]}/{p_Type}.txt', 'r', encoding='utf-8') as f:
				st.write(f.read())
		elif p_Type == '金のイルカ':
			with open(f'p_Type/{yourType[0:-2]}/{p_Type}.txt', 'r', encoding='utf-8') as f:
				st.write(f.read())
		elif p_Type == '銀のイルカ':
			with open(f'p_Type/{yourType[0:-2]}/{p_Type}.txt', 'r', encoding='utf-8') as f:
				st.write(f.read())
	elif yourType[0:-2] == '金の時計':
		if p_Type == '金の羅針盤':
			with open(f'p_Type/{yourType[0:-2]}/{p_Type}.txt', 'r', encoding='utf-8') as f:
				st.write(f.read())
		elif p_Type == '銀の羅針盤':
			with open(f'p_Type/{yourType[0:-2]}/{p_Type}.txt', 'r', encoding='utf-8') as f:
				st.write(f.read())
		elif p_Type == '金のインディアン':
			with open(f'p_Type/{yourType[0:-2]}/{p_Type}.txt', 'r', encoding='utf-8') as f:
				st.write(f.read())
		elif p_Type == '銀のインディアン':
			with open(f'p_Type/{yourType[0:-2]}/{p_Type}.txt', 'r', encoding='utf-8') as f:
				st.write(f.read())
		elif p_Type == '金の鳳凰':
			with open(f'p_Type/{yourType[0:-2]}/{p_Type}.txt', 'r', encoding='utf-8') as f:
				st.write(f.read())
		elif p_Type == '銀の鳳凰':
			with open(f'p_Type/{yourType[0:-2]}/{p_Type}.txt', 'r', encoding='utf-8') as f:
				st.write(f.read())
		elif p_Type == '金の時計':
			with open(f'p_Type/{yourType[0:-2]}/{p_Type}.txt', 'r', encoding='utf-8') as f:
				st.write(f.read())
		elif p_Type == '銀の時計':
			with open(f'p_Type/{yourType[0:-2]}/{p_Type}.txt', 'r', encoding='utf-8') as f:
				st.write(f.read())
		elif p_Type == '金のカメレオン':
			with open(f'p_Type/{yourType[0:-2]}/{p_Type}.txt', 'r', encoding='utf-8') as f:
				st.write(f.read())
		elif p_Type == '銀のカメレオン':
			with open(f'p_Type/{yourType[0:-2]}/{p_Type}.txt', 'r', encoding='utf-8') as f:
				st.write(f.read())
		elif p_Type == '金のイルカ':
			with open(f'p_Type/{yourType[0:-2]}/{p_Type}.txt', 'r', encoding='utf-8') as f:
				st.write(f.read())
		elif p_Type == '銀のイルカ':
			with open(f'p_Type/{yourType[0:-2]}/{p_Type}.txt', 'r', encoding='utf-8') as f:
				st.write(f.read())
	elif yourType[0:-2] == '銀の時計':
		if p_Type == '金の羅針盤':
			with open(f'p_Type/{yourType[0:-2]}/{p_Type}.txt', 'r', encoding='utf-8') as f:
				st.write(f.read())
		elif p_Type == '銀の羅針盤':
			with open(f'p_Type/{yourType[0:-2]}/{p_Type}.txt', 'r', encoding='utf-8') as f:
				st.write(f.read())
		elif p_Type == '金のインディアン':
			with open(f'p_Type/{yourType[0:-2]}/{p_Type}.txt', 'r', encoding='utf-8') as f:
				st.write(f.read())
		elif p_Type == '銀のインディアン':
			with open(f'p_Type/{yourType[0:-2]}/{p_Type}.txt', 'r', encoding='utf-8') as f:
				st.write(f.read())
		elif p_Type == '金の鳳凰':
			with open(f'p_Type/{yourType[0:-2]}/{p_Type}.txt', 'r', encoding='utf-8') as f:
				st.write(f.read())
		elif p_Type == '銀の鳳凰':
			with open(f'p_Type/{yourType[0:-2]}/{p_Type}.txt', 'r', encoding='utf-8') as f:
				st.write(f.read())
		elif p_Type == '金の時計':
			with open(f'p_Type/{yourType[0:-2]}/{p_Type}.txt', 'r', encoding='utf-8') as f:
				st.write(f.read())
		elif p_Type == '銀の時計':
			with open(f'p_Type/{yourType[0:-2]}/{p_Type}.txt', 'r', encoding='utf-8') as f:
				st.write(f.read())
		elif p_Type == '金のカメレオン':
			with open(f'p_Type/{yourType[0:-2]}/{p_Type}.txt', 'r', encoding='utf-8') as f:
				st.write(f.read())
		elif p_Type == '銀のカメレオン':
			with open(f'p_Type/{yourType[0:-2]}/{p_Type}.txt', 'r', encoding='utf-8') as f:
				st.write(f.read())
		elif p_Type == '金のイルカ':
			with open(f'p_Type/{yourType[0:-2]}/{p_Type}.txt', 'r', encoding='utf-8') as f:
				st.write(f.read())
		elif p_Type == '銀のイルカ':
			with open(f'p_Type/{yourType[0:-2]}/{p_Type}.txt', 'r', encoding='utf-8') as f:
				st.write(f.read())
	elif yourType[0:-2] == '金のカメレオン':
		if p_Type == '金の羅針盤':
			with open(f'p_Type/{yourType[0:-2]}/{p_Type}.txt', 'r', encoding='utf-8') as f:
				st.write(f.read())
		elif p_Type == '銀の羅針盤':
			with open(f'p_Type/{yourType[0:-2]}/{p_Type}.txt', 'r', encoding='utf-8') as f:
				st.write(f.read())
		elif p_Type == '金のインディアン':
			with open(f'p_Type/{yourType[0:-2]}/{p_Type}.txt', 'r', encoding='utf-8') as f:
				st.write(f.read())
		elif p_Type == '銀のインディアン':
			with open(f'p_Type/{yourType[0:-2]}/{p_Type}.txt', 'r', encoding='utf-8') as f:
				st.write(f.read())
		elif p_Type == '金の鳳凰':
			with open(f'p_Type/{yourType[0:-2]}/{p_Type}.txt', 'r', encoding='utf-8') as f:
				st.write(f.read())
		elif p_Type == '銀の鳳凰':
			with open(f'p_Type/{yourType[0:-2]}/{p_Type}.txt', 'r', encoding='utf-8') as f:
				st.write(f.read())
		elif p_Type == '金の時計':
			with open(f'p_Type/{yourType[0:-2]}/{p_Type}.txt', 'r', encoding='utf-8') as f:
				st.write(f.read())
		elif p_Type == '銀の時計':
			with open(f'p_Type/{yourType[0:-2]}/{p_Type}.txt', 'r', encoding='utf-8') as f:
				st.write(f.read())
		elif p_Type == '金のカメレオン':
			with open(f'p_Type/{yourType[0:-2]}/{p_Type}.txt', 'r', encoding='utf-8') as f:
				st.write(f.read())
		elif p_Type == '銀のカメレオン':
			with open(f'p_Type/{yourType[0:-2]}/{p_Type}.txt', 'r', encoding='utf-8') as f:
				st.write(f.read())
		elif p_Type == '金のイルカ':
			with open(f'p_Type/{yourType[0:-2]}/{p_Type}.txt', 'r', encoding='utf-8') as f:
				st.write(f.read())
		elif p_Type == '銀のイルカ':
			with open(f'p_Type/{yourType[0:-2]}/{p_Type}.txt', 'r', encoding='utf-8') as f:
				st.write(f.read())
	elif yourType[0:-2] == '銀のカメレオン':
		if p_Type == '金の羅針盤':
			with open(f'p_Type/{yourType[0:-2]}/{p_Type}.txt', 'r', encoding='utf-8') as f:
				st.write(f.read())
		elif p_Type == '銀の羅針盤':
			with open(f'p_Type/{yourType[0:-2]}/{p_Type}.txt', 'r', encoding='utf-8') as f:
				st.write(f.read())
		elif p_Type == '金のインディアン':
			with open(f'p_Type/{yourType[0:-2]}/{p_Type}.txt', 'r', encoding='utf-8') as f:
				st.write(f.read())
		elif p_Type == '銀のインディアン':
			with open(f'p_Type/{yourType[0:-2]}/{p_Type}.txt', 'r', encoding='utf-8') as f:
				st.write(f.read())
		elif p_Type == '金の鳳凰':
			with open(f'p_Type/{yourType[0:-2]}/{p_Type}.txt', 'r', encoding='utf-8') as f:
				st.write(f.read())
		elif p_Type == '銀の鳳凰':
			with open(f'p_Type/{yourType[0:-2]}/{p_Type}.txt', 'r', encoding='utf-8') as f:
				st.write(f.read())
		elif p_Type == '金の時計':
			with open(f'p_Type/{yourType[0:-2]}/{p_Type}.txt', 'r', encoding='utf-8') as f:
				st.write(f.read())
		elif p_Type == '銀の時計':
			with open(f'p_Type/{yourType[0:-2]}/{p_Type}.txt', 'r', encoding='utf-8') as f:
				st.write(f.read())
		elif p_Type == '金のカメレオン':
			with open(f'p_Type/{yourType[0:-2]}/{p_Type}.txt', 'r', encoding='utf-8') as f:
				st.write(f.read())
		elif p_Type == '銀のカメレオン':
			with open(f'p_Type/{yourType[0:-2]}/{p_Type}.txt', 'r', encoding='utf-8') as f:
				st.write(f.read())
		elif p_Type == '金のイルカ':
			with open(f'p_Type/{yourType[0:-2]}/{p_Type}.txt', 'r', encoding='utf-8') as f:
				st.write(f.read())
		elif p_Type == '銀のイルカ':
			with open(f'p_Type/{yourType[0:-2]}/{p_Type}.txt', 'r', encoding='utf-8') as f:
				st.write(f.read())
	elif yourType[0:-2] == '金のイルカ':
		if p_Type == '金の羅針盤':
			with open(f'p_Type/{yourType[0:-2]}/{p_Type}.txt', 'r', encoding='utf-8') as f:
				st.write(f.read())
		elif p_Type == '銀の羅針盤':
			with open(f'p_Type/{yourType[0:-2]}/{p_Type}.txt', 'r', encoding='utf-8') as f:
				st.write(f.read())
		elif p_Type == '金のインディアン':
			with open(f'p_Type/{yourType[0:-2]}/{p_Type}.txt', 'r', encoding='utf-8') as f:
				st.write(f.read())
		elif p_Type == '銀のインディアン':
			with open(f'p_Type/{yourType[0:-2]}/{p_Type}.txt', 'r', encoding='utf-8') as f:
				st.write(f.read())
		elif p_Type == '金の鳳凰':
			with open(f'p_Type/{yourType[0:-2]}/{p_Type}.txt', 'r', encoding='utf-8') as f:
				st.write(f.read())
		elif p_Type == '銀の鳳凰':
			with open(f'p_Type/{yourType[0:-2]}/{p_Type}.txt', 'r', encoding='utf-8') as f:
				st.write(f.read())
		elif p_Type == '金の時計':
			with open(f'p_Type/{yourType[0:-2]}/{p_Type}.txt', 'r', encoding='utf-8') as f:
				st.write(f.read())
		elif p_Type == '銀の時計':
			with open(f'p_Type/{yourType[0:-2]}/{p_Type}.txt', 'r', encoding='utf-8') as f:
				st.write(f.read())
		elif p_Type == '金のカメレオン':
			with open(f'p_Type/{yourType[0:-2]}/{p_Type}.txt', 'r', encoding='utf-8') as f:
				st.write(f.read())
		elif p_Type == '銀のカメレオン':
			with open(f'p_Type/{yourType[0:-2]}/{p_Type}.txt', 'r', encoding='utf-8') as f:
				st.write(f.read())
		elif p_Type == '金のイルカ':
			with open(f'p_Type/{yourType[0:-2]}/{p_Type}.txt', 'r', encoding='utf-8') as f:
				st.write(f.read())
		elif p_Type == '銀のイルカ':
			with open(f'p_Type/{yourType[0:-2]}/{p_Type}.txt', 'r', encoding='utf-8') as f:
				st.write(f.read())
	elif yourType[0:-2] == '銀のイルカ':
		if p_Type == '金の羅針盤':
			with open(f'p_Type/{yourType[0:-2]}/{p_Type}.txt', 'r', encoding='utf-8') as f:
				st.write(f.read())
		elif p_Type == '銀の羅針盤':
			with open(f'p_Type/{yourType[0:-2]}/{p_Type}.txt', 'r', encoding='utf-8') as f:
				st.write(f.read())
		elif p_Type == '金のインディアン':
			with open(f'p_Type/{yourType[0:-2]}/{p_Type}.txt', 'r', encoding='utf-8') as f:
				st.write(f.read())
		elif p_Type == '銀のインディアン':
			with open(f'p_Type/{yourType[0:-2]}/{p_Type}.txt', 'r', encoding='utf-8') as f:
				st.write(f.read())
		elif p_Type == '金の鳳凰':
			with open(f'p_Type/{yourType[0:-2]}/{p_Type}.txt', 'r', encoding='utf-8') as f:
				st.write(f.read())
		elif p_Type == '銀の鳳凰':
			with open(f'p_Type/{yourType[0:-2]}/{p_Type}.txt', 'r', encoding='utf-8') as f:
				st.write(f.read())
		elif p_Type == '金の時計':
			with open(f'p_Type/{yourType[0:-2]}/{p_Type}.txt', 'r', encoding='utf-8') as f:
				st.write(f.read())
		elif p_Type == '銀の時計':
			with open(f'p_Type/{yourType[0:-2]}/{p_Type}.txt', 'r', encoding='utf-8') as f:
				st.write(f.read())
		elif p_Type == '金のカメレオン':
			with open(f'p_Type/{yourType[0:-2]}/{p_Type}.txt', 'r', encoding='utf-8') as f:
				st.write(f.read())
		elif p_Type == '銀のカメレオン':
			with open(f'p_Type/{yourType[0:-2]}/{p_Type}.txt', 'r', encoding='utf-8') as f:
				st.write(f.read())
		elif p_Type == '金のイルカ':
			with open(f'p_Type/{yourType[0:-2]}/{p_Type}.txt', 'r', encoding='utf-8') as f:
				st.write(f.read())
		elif p_Type == '銀のイルカ':
			with open(f'p_Type/{yourType[0:-2]}/{p_Type}.txt', 'r', encoding='utf-8') as f:
				st.write(f.read())
	else:
		pass

if st.button('お相手との相性を占う'):
	p_uranai_start()

st.write('Copyright © 2021 Tomoyuki Yoshikawa. All Rights Reserved.')
