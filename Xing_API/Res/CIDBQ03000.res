BEGIN_FUNCTION_MAP
	.Func,�ؿܼ��� ������/�ܰ���Ȳ,CIDBQ03000,SERVICE=CIDBQ03000,headtype=B,CREATOR=��ȣ��,CREDATE=2015/06/25 09:12:31;
	BEGIN_DATA_MAP
	CIDBQ03000InBlock1,In(*EMPTY*),input;
	begin
		���ڵ尹��, RecCnt, RecCnt, long, 5
		���±����ڵ�, AcntTpCode, AcntTpCode, char, 1;
		���¹�ȣ, AcntNo, AcntNo, char, 20;
		���º�й�ȣ, AcntPwd, AcntPwd, char, 8;
		�ŷ�����, TrdDt, TrdDt, char, 8;
	end
	CIDBQ03000OutBlock1,In(*EMPTY*),output;
	begin
		���ڵ尹��, RecCnt, RecCnt, long, 5
		���±����ڵ�, AcntTpCode, AcntTpCode, char, 1;
		���¹�ȣ, AcntNo, AcntNo, char, 20;
		���º�й�ȣ, AcntPwd, AcntPwd, char, 8;
		�ŷ�����, TrdDt, TrdDt, char, 8;
	end
	CIDBQ03000OutBlock2,Out(*EMPTY*),output,occurs;
	begin
		���¹�ȣ, AcntNo, AcntNo, char, 20;
		�ŷ�����, TrdDt, TrdDt, char, 8;
		��ȭ����ڵ�, CrcyObjCode, CrcyObjCode, char, 12;
		�ؿܼ���������, OvrsFutsDps, OvrsFutsDps, double, 23.2;
		������ݱݾ�, CustmMnyioAmt, CustmMnyioAmt, double, 19.2;
		�ؿܼ���û����ͱݾ�, AbrdFutsLqdtPnlAmt, AbrdFutsLqdtPnlAmt, double, 19.2;
		�ؿܼ���������ݾ�, AbrdFutsCmsnAmt, AbrdFutsCmsnAmt, double, 19.2;
		��ȯ��������, PrexchDps, PrexchDps, double, 19.2;
		���ڻ�ݾ�, EvalAssetAmt, EvalAssetAmt, double, 19.2;
		�ؿܼ�����Ź���űݾ�, AbrdFutsCsgnMgn, AbrdFutsCsgnMgn, double, 19.2;
		�ؿܼ����߰����űݾ�, AbrdFutsAddMgn, AbrdFutsAddMgn, double, 19.2;
		�ؿܼ������Ⱑ�ɱݾ�, AbrdFutsWthdwAbleAmt, AbrdFutsWthdwAbleAmt, double, 19.2;
		�ؿܼ����ֹ����ɱݾ�, AbrdFutsOrdAbleAmt, AbrdFutsOrdAbleAmt, double, 19.2;
		�ؿܼ����򰡼��ͱݾ�, AbrdFutsEvalPnlAmt, AbrdFutsEvalPnlAmt, double, 19.2;
		�����������ͱݾ�, LastSettPnlAmt, LastSettPnlAmt, double, 19.2;
		�ؿܿɼǰ����ݾ�, OvrsOptSettAmt, OvrsOptSettAmt, double, 19.2;
		�ؿܿɼ��ܰ��򰡱ݾ�, OvrsOptBalEvalAmt, OvrsOptBalEvalAmt, double, 19.2;
	end
	END_DATA_MAP
END_FUNCTION_MAP
