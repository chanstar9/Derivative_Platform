BEGIN_FUNCTION_MAP
	.Func,e����˻�(�Ź���API��),t1857,attr,block,headtype=A;
	BEGIN_DATA_MAP
	t1857InBlock,In(*EMPTY*),input;
	begin
		�ǽð�����(0:��ȸ 1:�ǽð�), sRealFlag, sRealFlag, char, 1
		����˻�����(F:���� S:����), sSearchFlag, sSearchFlag, char, 1;
		����˻��Է°�, query_index, query_index, char, 256;
	end
	t1857OutBlock,Out(*EMPTY*),output;
	begin
		�˻������, result_count, result_count, long, 5;
		�����ð�, result_time, result_time, char, 6;
		�ǽð�Ű, AlertNum, AlertNum, char, 11;
	end
	t1857OutBlock1,Out(*EMPTY*),output,occurs;
	begin
		�����ڵ�, shcode, shcode, char, 7;
		�����, hname, hname, char, 40;
		���簡, price, price, long, 9;
		���ϴ�񱸺�, sign, sign, char, 1;
		���ϴ��, change, change, long, 9;
		�����, diff, diff, float, 6;
		�ŷ���, volume, volume, long, 12;
		�������(N:���� R:������ O:��Ż), JobFlag, JobFlag, char, 1;
	end
	END_DATA_MAP
END_FUNCTION_MAP
