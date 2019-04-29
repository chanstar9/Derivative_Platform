#res_parser.py
import os

def _readline_until_not_empty(f):
	line = f.readline().strip()
	while line == '':
		line = f.readline().strip()
	if line is None:
		raise EOFError('Unexpected EOF while reading an res file')
	return line

def _case_insensitive_compare(str0, str1):
	return str0.lower() == str1.lower()

def _clean_strip(line):
	return list(map(str.strip, line.strip(';').strip().split(',')))

def res_parser(filepath, include_human_readable_info = False):
	ret = dict()
	with open(filepath, 'r') as f:
		# find BEGIN_FUNCTION_MAP start point
		line = _readline_until_not_empty(f)
		while not _case_insensitive_compare(line, 'BEGIN_FUNCTION_MAP'):
			line = _readline_until_not_empty(f)

		# parse tr_code
		line = _readline_until_not_empty(f)
		contents = _clean_strip(line)

		#query or subscription
		is_query = _case_insensitive_compare(contents[0], '.Func')
		desc = contents[1]

		# tr_code
		#---------------
		# res 파일속의 tr코드와 파일이름의 tr코드가 다른경우가 있음
		# 추측컨데, 비슷한 tr코드를(ex: 'YS3' vs. 'Ys3', Ys3->Ys3_4ELW)을 개발자들이 헷갈리지 않도록 원래의 tr코드 그대로 사용치 않고 변화를 준 것 같음
		# 원래 TR코드보다는 res파일이름을 기준으로 tr_code 저장
		#---------------
		#tr_code from rest file
		#tr_code = contents[2]
		#tr_code from filename
		tr_code = os.path.split(filepath)[1].split('.')[0].strip()

		header = {'tr_code':tr_code, 'is_query':is_query}
		if include_human_readable_info:
			header.update({'desc':desc, 'path':filepath})

		ret.update({'header':header})

		#find BEGIN_DATA_MAP start point
		line = _readline_until_not_empty(f)
		while not _case_insensitive_compare(line, 'BEGIN_DATA_MAP'):
			line = _readline_until_not_empty(f)

		line = _readline_until_not_empty(f)
		block = []
		while not _case_insensitive_compare(line, 'END_DATA_MAP'):
			a_block = dict()
			# a_block name, input or output, occurs
			contents = _clean_strip(line)
			is_input = 'input' in contents
			is_occurs = 'occurs' in contents
			a_block.update({'bname':contents[0],'is_input':is_input,'is_occurs':is_occurs}) #-------- bname ...

			line = _readline_until_not_empty(f)
			while not _case_insensitive_compare(line, 'begin'):
				line = _readline_until_not_empty(f)

			line = _readline_until_not_empty(f)
			args = []
			while not _case_insensitive_compare(line, 'end'):
				contents = _clean_strip(line)
				arg = {'code':contents[1]}
				if include_human_readable_info:
					arg.update({'desc':contents[0], 'type':contents[3], 'length':contents[4]})
				args.append(arg)
				line = _readline_until_not_empty(f)
			a_block.update({'args':args})
			line = _readline_until_not_empty(f)
			block.append(a_block)
		ret.update({'block':block})
		return ret

def multi_res_parser(filepath_list, include_human_readable_info = False):
	code_set = set()
	ret = []
	for filepath in filepath_list:
		r = res_parser(filepath, include_human_readable_info)
		tr_code = r['header']['tr_code']
		if not tr_code in code_set:
			code_set.add(tr_code)
			ret.append(r)
	return ret

def res_parser2(filepath, include_human_readable_info = False):
	ret = dict()
	with open(filepath, 'r') as f:
		# find BEGIN_FUNCTION_MAP start point
		line = _readline_until_not_empty(f)
		while not _case_insensitive_compare(line, 'BEGIN_FUNCTION_MAP'):
			line = _readline_until_not_empty(f)

		# parse tr_code
		line = _readline_until_not_empty(f)
		contents = _clean_strip(line)

		#query or subscription
		is_query = _case_insensitive_compare(contents[0], '.Func')
		desc = contents[1]

		# tr_code
		#---------------
		# res 파일속의 tr코드와 파일이름의 tr코드가 다른경우가 있음
		# 추측컨데, 비슷한 tr코드를(ex: 'YS3' vs. 'Ys3', Ys3->Ys3_4ELW)을 개발자들이 헷갈리지 않도록 원래의 tr코드 그대로 사용치 않고 변화를 준 것 같음
		# 원래 TR코드보다는 res파일이름을 기준으로 tr_code 저장
		#---------------
		#tr_code from rest file
		#tr_code = contents[2]
		#tr_code from filename
		tr_code = os.path.split(filepath)[1].split('.')[0].strip()

		header = {'tr_code':tr_code, 'is_query':is_query}
		if include_human_readable_info:
			header.update({'desc':desc, 'path':filepath})

		ret.update({'header':header})

		#find BEGIN_DATA_MAP start point
		line = _readline_until_not_empty(f)
		while not _case_insensitive_compare(line, 'BEGIN_DATA_MAP'):
			line = _readline_until_not_empty(f)

		line = _readline_until_not_empty(f)
		block = []
		while not _case_insensitive_compare(line, 'END_DATA_MAP'):
			a_block = dict()
			# a_block name, input or output, occurs
			contents = _clean_strip(line)
			is_input = 'input' in contents
			is_occurs = 'occurs' in contents
			a_block.update({'bname':contents[0],'is_input':is_input,'is_occurs':is_occurs}) #-------- bname ...

			line = _readline_until_not_empty(f)
			while not _case_insensitive_compare(line, 'begin'):
				line = _readline_until_not_empty(f)

			line = _readline_until_not_empty(f)
			args = []
			while not _case_insensitive_compare(line, 'end'):
				contents = _clean_strip(line)
				arg = {'code':contents[1]}
				if include_human_readable_info:
					arg.update({'desc':contents[0], 'type':contents[3], 'length':contents[4]})
				args.append(arg)
				line = _readline_until_not_empty(f)
			a_block.update({'args':args})
			line = _readline_until_not_empty(f)
			block.append(a_block)
		ret.update({'block':block})
		return ret

#char=r['block'][1]['args'][1]['code']
#code=r['block'][1]['args'][1]['type']
#text="'{0}' : '{1}'".format(x,y)

def res_to_template(filepath, include_human_readable_info = True):
	ret=list()
	r=res_parser(filepath, include_human_readable_info)
	query_name=r['header']['tr_code']
	if r['header']['is_query']:
		third='query'
	else:
		third='subscription'
	description ="{0} {1}".format('#' , r['header']['desc'].split('-')[0])
	head_text="db_outblock_{0}_{1} = {2}".format(third,query_name,'{')
	master_text="{0}\n{1}".format(description,head_text)
	closing='}'

	for cnt  in range(1,(len(r['block']))):
		outblock_name= "'{0}' : {1}".format(r['block'][cnt]['bname'],'{')
		master_text="{0}\n\t{1}".format(master_text,outblock_name)
		counter=0
		for i in r['block'][cnt]['args']:
			code_name=i['code']
			type_name=i['type']
			counter=counter+1
			if len(r['block'][cnt]['args']) != counter:
				line_text="'{0}' : '{1}' ,".format(code_name,type_name)
			else:
				line_text="'{0}' : '{1}' ".format(code_name,type_name)
			master_text="{0}\n\t\t{1}".format(master_text,line_text)
		master_text="{0}\n\t{1}".format(master_text,closing)
	master_text="{0}\n{1}".format(master_text,closing)
	return master_text

def multi_res_to_template(filepath_list, include_human_readable_info = False):
	#code_set = set()
	ret = []
	for filepath in filepath_list:
		master_text = res_to_template(filepath, include_human_readable_info)
		text="{0}\n".format(master_text)
		ret.append(text)
		#final_str = '\n'.join(map(str, ret))
	return ret

path_list=["D:\Dropbox\pystock_0.0.4a\Res\o3101.res", "D:\Dropbox\pystock_0.0.4a\Res\o3103.res", "D:\Dropbox\pystock_0.0.4a\Res\o3104.res","D:\Dropbox\pystock_0.0.4a\Res\o3105.res",
		"D:\Dropbox\pystock_0.0.4a\Res\o3106.res","D:\Dropbox\pystock_0.0.4a\Res\o3107.res","D:\Dropbox\pystock_0.0.4a\Res\o3108.res","D:\Dropbox\pystock_0.0.4a\Res\o3116.res",
		"D:\Dropbox\pystock_0.0.4a\Res\o3121.res","D:\Dropbox\pystock_0.0.4a\Res\o3123.res","D:\Dropbox\pystock_0.0.4a\Res\o3125.res","D:\Dropbox\pystock_0.0.4a\Res\o3126.res",
		"D:\Dropbox\pystock_0.0.4a\Res\o3127.res","D:\Dropbox\pystock_0.0.4a\Res\o3128.res","D:\Dropbox\pystock_0.0.4a\Res\o3136.res","D:\Dropbox\pystock_0.0.4a\Res\o3137.res",
		"D:\Dropbox\pystock_0.0.4a\Res\OVC.res","D:\Dropbox\pystock_0.0.4a\Res\OVH.res","D:\Dropbox\pystock_0.0.4a\Res\TC1.res","D:\Dropbox\pystock_0.0.4a\Res\TC2.res",
		"D:\Dropbox\pystock_0.0.4a\Res\TC3.res","D:\Dropbox\pystock_0.0.4a\Res\WOC.res","D:\Dropbox\pystock_0.0.4a\Res\WOH.res","D:\Dropbox\pystock_0.0.4a\Res\CIDBQ01400.res",
		"D:\Dropbox\pystock_0.0.4a\Res\CIDBQ01500.res","D:\Dropbox\pystock_0.0.4a\Res\CIDBQ01800.res","D:\Dropbox\pystock_0.0.4a\Res\CIDBQ02400.res","D:\Dropbox\pystock_0.0.4a\Res\CIDBQ03000.res",
		"D:\Dropbox\pystock_0.0.4a\Res\CIDBQ05300.res","D:\Dropbox\pystock_0.0.4a\Res\CIDBT00100.res","D:\Dropbox\pystock_0.0.4a\Res\CIDBT00900.res","D:\Dropbox\pystock_0.0.4a\Res\CIDBT01000.res",
		"D:\Dropbox\pystock_0.0.4a\Res\CIDEQ00800.res"]

new_path=["D:\Dropbox\pystock_0.0.4a\Res\o3117.res","D:\Dropbox\pystock_0.0.4a\Res//t1410.res"]

#with open("outblock_tmp.txt", "w") as text_file:
#   text_file.write("%s" %zz)
# aa=multi_res_to_template(path_list,True)
## zz="".join(aa)