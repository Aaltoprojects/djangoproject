import urllib.request
import urllib.parse
import re

# a tutorial for the parse methods used:
# https://www.youtube.com/watch?v=K8L6KVGG-7o

def haetiedot(nimi, ytunnus):

	nimi = nimi.replace(' ', '-').replace('ö', 'o').replace('ä', 'a')
	ytunnus = ytunnus.replace('-', '')

	info = {}

	urltalous = 'https://www.asiakastieto.fi/yritykset/fi/' + nimi + '/' + ytunnus + '/taloustiedot'
	urlrekisteri = 'https://www.asiakastieto.fi/yritykset/fi/' + nimi + '/' + ytunnus + '/rekisteritiedot'

	request = urllib.request.urlopen(urltalous)
	responseData = str(request.read())

	# revenue (1000€), evolution of revenue (%), EBIT (1000€),EBIT (%), personnel (#)
	pattern1 = re.compile(r'<td>[0-9 ,%-]+</td>')
	matches1 = pattern1.findall(responseData)
	# equity ratio (%)
	pattern2 = re.compile(r'<span>[0-9 ,-]+%</span>')
	matches2 = pattern2.findall(responseData)

	request = urllib.request.urlopen(urlrekisteri)
	responseData = str(request.read())

	# register dates: kaupparekisteri, etc.
	pattern3 = re.compile(r'<td>[0-9.]+</td>')
	matches3 = pattern3.findall(responseData)

	basic = []
	for match in matches1:
		cleanmatch = float(str(match).strip('<td>').strip('</td>').strip('%').replace(' ', '').replace(',','.'))
		basic.append(cleanmatch)
	info['financials'] = basic

	basic = []
	for match in matches2:
		cleanmatch = float(str(match).strip('<span>').strip('</span>').strip('%').replace(' ', ''))
		basic.append(cleanmatch)
	info['equityratio'] = basic

	basic = []
	for match in matches3:
		cleanmatch = str(match).strip('<td>').strip('</td>')
		basic.append(cleanmatch)
	info['register'] = basic

	return info


