BEGIN_FUNCTION_MAP
	.Func,�ؿܼ��� ���¿�Ź�ڻ���ȸ,CIDBQ05300,SERVICE=CIDBQ05300,headtype=B,CREATOR=��ȣ��,CREDATE=2015/06/22 19:42:57;
	BEGIN_DATA_MAP
	CIDBQ05300InBlock1,In(*EMPTY*),input;
	begin
		���ڵ尹��, RecCnt, RecCnt, long, 5
		�ؿܰ��±����ڵ�, OvrsAcntTpCode, OvrsAcntTpCode, char, 1;
		FCM���¹�ȣ, FcmAcntNo, FcmAcntNo, char, 20;
		���¹�ȣ, AcntNo, AcntNo, char, 20;
		���º�й�ȣ, AcntPwd, AcntPwd, char, 8;
		��ȭ�ڵ�, CrcyCode, CrcyCode, char, 3;
	end
	CIDBQ05300OutBlock1,In(*EMPTY*),output;
	begin
		���ڵ尹��, RecCnt, RecCnt, long, 5
		�ؿܰ��±����ڵ�, OvrsAcntTpCode, OvrsAcntTpCode, char, 1;
		FCM���¹�ȣ, FcmAcntNo, FcmAcntNo, char, 20;
		���¹�ȣ, AcntNo, AcntNo, char, 20;
		���º�й�ȣ, AcntPwd, AcntPwd, char, 8;
		��ȭ�ڵ�, CrcyCode, CrcyCode, char, 3;
	end
	CIDBQ05300OutBlock2,Out(*EMPTY*),output,occurs;
	begin
		���¹�ȣ, AcntNo, AcntNo, char, 20;
		��ȭ�ڵ�, CrcyCode, CrcyCode, char, 3;
		�ؿܼ���������, OvrsFutsDps, OvrsFutsDps, double, 23.2;
		�ؿܼ�����Ź���űݾ�, AbrdFutsCsgnMgn, AbrdFutsCsgnMgn, double, 19.2;
		�ؿܼ����߰����ű�, OvrsFutsSplmMgn, OvrsFutsSplmMgn, double, 23.2;
		��û����ͱݾ�, CustmLpnlAmt, CustmLpnlAmt, double, 19.2;
		�ؿܼ����򰡼��ͱݾ�, AbrdFutsEvalPnlAmt, AbrdFutsEvalPnlAmt, double, 19.2;
		�ؿܼ���������ݾ�, AbrdFutsCmsnAmt, AbrdFutsCmsnAmt, double, 19.2;
		�ؿܼ����򰡿�Ź�ѱݾ�, AbrdFutsEvalDpstgTotAmt, AbrdFutsEvalDpstgTotAmt, double, 19.2;
		ȯ��, Xchrat, Xchrat, double, 15.4;
		��ȭ��ȯ���ݾ�, FcurrRealMxchgAmt, FcurrRealMxchgAmt, double, 19.2;
		�ؿܼ������Ⱑ�ɱݾ�, AbrdFutsWthdwAbleAmt, AbrdFutsWthdwAbleAmt, double, 19.2;
		�ؿܼ����ֹ����ɱݾ�, AbrdFutsOrdAbleAmt, AbrdFutsOrdAbleAmt, double, 19.2;
		��������̵���û����ͱݾ�, FutsDueNarrvLqdtPnlAmt, FutsDueNarrvLqdtPnlAmt, double, 19.2;
		��������̵���������, FutsDueNarrvCmsn, FutsDueNarrvCmsn, double, 19.2;
		�ؿܼ���û����ͱݾ�, AbrdFutsLqdtPnlAmt, AbrdFutsLqdtPnlAmt, double, 19.2;
		�ؿܼ������������, OvrsFutsDueCmsn, OvrsFutsDueCmsn, double, 19.2;
		�ؿܼ����ɼǸż��ݾ�, OvrsFutsOptBuyAmt, OvrsFutsOptBuyAmt, double, 23.2;
		�ؿܼ����ɼǸŵ��ݾ�, OvrsFutsOptSellAmt, OvrsFutsOptSellAmt, double, 23.2;
		�ɼǸż����尡ġ�ݾ�, OptBuyMktWrthAmt, OptBuyMktWrthAmt, double, 19.2;
		�ɼǸŵ����尡ġ�ݾ�, OptSellMktWrthAmt, OptSellMktWrthAmt, double, 19.2;
	end
	CIDBQ05300OutBlock3,SelOut(*EMPTY*),output;
	begin
		���ڵ尹��, RecCnt, RecCnt, long, 5
		�ؿܼ���������, OvrsFutsDps, OvrsFutsDps, double, 23.2;
		�ؿܼ���û����ͱݾ�, AbrdFutsLqdtPnlAmt, AbrdFutsLqdtPnlAmt, double, 19.2;
		��������̵���û����ͱݾ�, FutsDueNarrvLqdtPnlAmt, FutsDueNarrvLqdtPnlAmt, double, 19.2;
		�ؿܼ����򰡼��ͱݾ�, AbrdFutsEvalPnlAmt, AbrdFutsEvalPnlAmt, double, 19.2;
		�ؿܼ����򰡿�Ź�ѱݾ�, AbrdFutsEvalDpstgTotAmt, AbrdFutsEvalDpstgTotAmt, double, 19.2;
		��û����ͱݾ�, CustmLpnlAmt, CustmLpnlAmt, double, 19.2;
		�ؿܼ������������, OvrsFutsDueCmsn, OvrsFutsDueCmsn, double, 19.2;
		��ȭ��ȯ���ݾ�, FcurrRealMxchgAmt, FcurrRealMxchgAmt, double, 19.2;
		�ؿܼ���������ݾ�, AbrdFutsCmsnAmt, AbrdFutsCmsnAmt, double, 19.2;
		��������̵���������, FutsDueNarrvCmsn, FutsDueNarrvCmsn, double, 19.2;
		�ؿܼ�����Ź���űݾ�, AbrdFutsCsgnMgn, AbrdFutsCsgnMgn, double, 19.2;
		�ؿܼ����������ű�, OvrsFutsMaintMgn, OvrsFutsMaintMgn, double, 19.2;
		�ؿܼ����ɼǸż��ݾ�, OvrsFutsOptBuyAmt, OvrsFutsOptBuyAmt, double, 23.2;
		�ؿܼ����ɼǸŵ��ݾ�, OvrsFutsOptSellAmt, OvrsFutsOptSellAmt, double, 23.2;
		�ſ��ѵ��ݾ�, CtlmtAmt, CtlmtAmt, double, 23.2;
		�ؿܼ����߰����ű�, OvrsFutsSplmMgn, OvrsFutsSplmMgn, double, 23.2;
		��������, MgnclRat, MgnclRat, double, 27.10;
		�ؿܼ����ֹ����ɱݾ�, AbrdFutsOrdAbleAmt, AbrdFutsOrdAbleAmt, double, 19.2;
		�ؿܼ������Ⱑ�ɱݾ�, AbrdFutsWthdwAbleAmt, AbrdFutsWthdwAbleAmt, double, 19.2;
		�ɼǸż����尡ġ�ݾ�, OptBuyMktWrthAmt, OptBuyMktWrthAmt, double, 19.2;
		�ɼǸŵ����尡ġ�ݾ�, OptSellMktWrthAmt, OptSellMktWrthAmt, double, 19.2;
		�ؿܿɼǰ����ݾ�, OvrsOptSettAmt, OvrsOptSettAmt, double, 19.2;
		�ؿܿɼ��ܰ��򰡱ݾ�, OvrsOptBalEvalAmt, OvrsOptBalEvalAmt, double, 19.2;
	end
	END_DATA_MAP
END_FUNCTION_MAP
