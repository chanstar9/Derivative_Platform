BEGIN_FUNCTION_MAP
	.Func,�ֽ�������ȸ API��(t8436),t8436,block,headtype=A;
	BEGIN_DATA_MAP
	t8436InBlock,�⺻�Է�,input;
	begin
		����(0:��ü1:�ڽ���2:�ڽ���),gubun,gubun,char,1;
	end
	t8436OutBlock,���1,output,occurs;
	begin
		�����,hname,hname,char,20;
		�����ڵ�,shcode,shcode,char,6;
		Ȯ���ڵ�,expcode,expcode,char,12;
		ETF����(1:ETF2:ETN),etfgubun,etfgubun,char,1;
		���Ѱ�,uplmtprice,uplmtprice,long,8;
		���Ѱ�,dnlmtprice,dnlmtprice,long,8;
		���ϰ�,jnilclose,jnilclose,long,8;
		�ֹ���������,memedan,memedan,char,5;
		���ذ�,recprice,recprice,long,8;
		����(1:�ڽ���2:�ڽ���),gubun,gubun,char,1;
		���Ǳ׷�,bu12gubun,bu12gubun,char,2;
		����μ�����ȸ�翩��(Y/N),spac_gubun,spac_gubun,char,1;
		filler(�̻��),filler,filler,char,32;
	end
	END_DATA_MAP
END_FUNCTION_MAP

