BEGIN_FUNCTION_MAP
	.Func,���ں� �̰��� �ܰ���,CIDEQ00800,SERVICE=CIDEQ00800,ENCRYPT,headtype=B,CREATOR=��ȣ��,CREDATE=2018/08/27 10:26:32;
	BEGIN_DATA_MAP
	CIDEQ00800InBlock1,In(*EMPTY*),input;
	begin
		���ڵ尹��, RecCnt, RecCnt, long, 5
		���¹�ȣ, AcntNo, AcntNo, char, 20;
		���º�й�ȣ, AcntPwd, AcntPwd, char, 8;
		�ŷ�����, TrdDt, TrdDt, char, 8;
	end
	CIDEQ00800OutBlock1,In(*EMPTY*),output;
	begin
		���ڵ尹��, RecCnt, RecCnt, long, 5
		���¹�ȣ, AcntNo, AcntNo, char, 20;
		���º�й�ȣ, AcntPwd, AcntPwd, char, 8;
		�ŷ�����, TrdDt, TrdDt, char, 8;
	end
	CIDEQ00800OutBlock2,Out(*EMPTY*),output,occurs;
	begin
		���¹�ȣ, AcntNo, AcntNo, char, 20;
		�ŷ�����, TrdDt, TrdDt, char, 8;
		�����ڵ尪, IsuCodeVal, IsuCodeVal, char, 18;
		�Ÿű��и�, BnsTpNm, BnsTpNm, char, 10;
		�ܰ����, BalQty, BalQty, long, 16;
		û�갡�ɼ���, LqdtAbleQty, LqdtAbleQty, long, 16;
		���԰���, PchsPrc, PchsPrc, double, 30.11;
		�ؿ��Ļ����簡, OvrsDrvtNowPrc, OvrsDrvtNowPrc, double, 30.11;
		�ؿܼ����򰡼��ͱݾ�, AbrdFutsEvalPnlAmt, AbrdFutsEvalPnlAmt, double, 19.2;
		���ܰ�ݾ�, CustmBalAmt, CustmBalAmt, double, 19.2;
		��ȭ�򰡱ݾ�, FcurrEvalAmt, FcurrEvalAmt, double, 21.4;
		�����, IsuNm, IsuNm, char, 50;
		��ȭ�ڵ尪, CrcyCodeVal, CrcyCodeVal, char, 3;
		�ؿ��Ļ���ǰ�ڵ�, OvrsDrvtPrdtCode, OvrsDrvtPrdtCode, char, 10;
		��������, DueDt, DueDt, char, 8;
		����ݾ�, PrcntrAmt, PrcntrAmt, double, 19.2;
		��ȭ�򰡼��ͱݾ�, FcurrEvalPnlAmt, FcurrEvalPnlAmt, double, 21.4;
	end
	END_DATA_MAP
END_FUNCTION_MAP
