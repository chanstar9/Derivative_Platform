BEGIN_FUNCTION_MAP
	.Func,�ؿܼ��� �̰��� �ܰ���,CIDBQ01500,SERVICE=CIDBQ01500,ENCRYPT,headtype=B,CREATOR=��ȣ��,CREDATE=2018/08/28 09:14:25;
	BEGIN_DATA_MAP
	CIDBQ01500InBlock1,In(*EMPTY*),input;
	begin
		���ڵ尹��, RecCnt, RecCnt, long, 5
		���±����ڵ�, AcntTpCode, AcntTpCode, char, 1;
		���¹�ȣ, AcntNo, AcntNo, char, 20;
		FCM���¹�ȣ, FcmAcntNo, FcmAcntNo, char, 20;
		��й�ȣ, Pwd, Pwd, char, 8;
		��ȸ����, QryDt, QryDt, char, 8;
		�ܰ����ڵ�, BalTpCode, BalTpCode, char, 1;
	end
	CIDBQ01500OutBlock1,In(*EMPTY*),output;
	begin
		���ڵ尹��, RecCnt, RecCnt, long, 5
		���±����ڵ�, AcntTpCode, AcntTpCode, char, 1;
		���¹�ȣ, AcntNo, AcntNo, char, 20;
		FCM���¹�ȣ, FcmAcntNo, FcmAcntNo, char, 20;
		��й�ȣ, Pwd, Pwd, char, 8;
		��ȸ����, QryDt, QryDt, char, 8;
		�ܰ����ڵ�, BalTpCode, BalTpCode, char, 1;
	end
	CIDBQ01500OutBlock2,Out(*EMPTY*),output,occurs;
	begin
		��������, BaseDt, BaseDt, char, 8;
		������, Dps, Dps, long, 16;
		û����ͱݾ�, LpnlAmt, LpnlAmt, double, 19.2;
		����������û����ͱݾ�, FutsDueBfLpnlAmt, FutsDueBfLpnlAmt, double, 23.2;
		����������������, FutsDueBfCmsn, FutsDueBfCmsn, double, 23.2;
		��Ź���űݾ�, CsgnMgn, CsgnMgn, long, 16;
		�������ű�, MaintMgn, MaintMgn, long, 16;
		�ſ��ѵ��ݾ�, CtlmtAmt, CtlmtAmt, double, 23.2;
		�߰����űݾ�, AddMgn, AddMgn, long, 16;
		��������, MgnclRat, MgnclRat, double, 27.10;
		�ֹ����ɱݾ�, OrdAbleAmt, OrdAbleAmt, long, 16;
		���Ⱑ�ɱݾ�, WthdwAbleAmt, WthdwAbleAmt, long, 16;
		���¹�ȣ, AcntNo, AcntNo, char, 20;
		�����ڵ尪, IsuCodeVal, IsuCodeVal, char, 18;
		�����, IsuNm, IsuNm, char, 50;
		��ȭ�ڵ尪, CrcyCodeVal, CrcyCodeVal, char, 3;
		�ؿ��Ļ���ǰ�ڵ�, OvrsDrvtPrdtCode, OvrsDrvtPrdtCode, char, 10;
		�ؿ��Ļ��ɼǱ����ڵ�, OvrsDrvtOptTpCode, OvrsDrvtOptTpCode, char, 1;
		��������, DueDt, DueDt, char, 8;
		�ؿ��Ļ���簡��, OvrsDrvtXrcPrc, OvrsDrvtXrcPrc, double, 30.11;
		�Ÿű����ڵ�, BnsTpCode, BnsTpCode, char, 1;
		�����ڵ��, CmnCodeNm, CmnCodeNm, char, 100;
		�����ڵ��, TpCodeNm, TpCodeNm, char, 50;
		�ܰ����, BalQty, BalQty, long, 16;
		���԰���, PchsPrc, PchsPrc, double, 30.11;
		�ؿ��Ļ����簡, OvrsDrvtNowPrc, OvrsDrvtNowPrc, double, 30.11;
		�ؿܼ����򰡼��ͱݾ�, AbrdFutsEvalPnlAmt, AbrdFutsEvalPnlAmt, double, 19.2;
		��Ź������, CsgnCmsn, CsgnCmsn, double, 19.2;
		�����ǹ�ȣ, PosNo, PosNo, char, 13;
		�ŷ��Һ��1������ݾ�, EufOneCmsnAmt, EufOneCmsnAmt, double, 19.2;
		�ŷ��Һ��2������ݾ�, EufTwoCmsnAmt, EufTwoCmsnAmt, double, 19.2;
	end
	END_DATA_MAP
END_FUNCTION_MAP
