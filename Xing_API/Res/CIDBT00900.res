BEGIN_FUNCTION_MAP
	.Func,�ؿܼ��������ֹ�,CIDBT00900,SERVICE=CIDBT00900,ENCRYPT,SIGNATURE,headtype=B,CREATOR=��ȣ��,CREDATE=2018/08/28 16:29:03;
	BEGIN_DATA_MAP
	CIDBT00900InBlock1,In(*EMPTY*),input;
	begin
		���ڵ尹��, RecCnt, RecCnt, long, 5
		�ֹ�����, OrdDt, OrdDt, char, 8;
		���������ȣ, RegBrnNo, RegBrnNo, char, 3;
		���¹�ȣ, AcntNo, AcntNo, char, 20;
		��й�ȣ, Pwd, Pwd, char, 8;
		�ؿܼ������ֹ���ȣ, OvrsFutsOrgOrdNo, OvrsFutsOrgOrdNo, char, 10;
		�����ڵ尪, IsuCodeVal, IsuCodeVal, char, 18;
		�����ֹ������ڵ�, FutsOrdTpCode, FutsOrdTpCode, char, 1;
		�Ÿű����ڵ�, BnsTpCode, BnsTpCode, char, 1;
		�����ֹ������ڵ�, FutsOrdPtnCode, FutsOrdPtnCode, char, 1;
		��ȭ�ڵ尪, CrcyCodeVal, CrcyCodeVal, char, 3;
		�ؿ��Ļ��ֹ�����, OvrsDrvtOrdPrc, OvrsDrvtOrdPrc, double, 30.11;
		�����ֹ�����, CndiOrdPrc, CndiOrdPrc, double, 30.11;
		�ֹ�����, OrdQty, OrdQty, long, 16;
		�ؿ��Ļ���ǰ�ڵ�, OvrsDrvtPrdtCode, OvrsDrvtPrdtCode, char, 10;
		������, DueYymm, DueYymm, char, 6;
		�ŷ����ڵ�, ExchCode, ExchCode, char, 10;
	end
	CIDBT00900OutBlock1,In(*EMPTY*),output;
	begin
		���ڵ尹��, RecCnt, RecCnt, long, 5
		�ֹ�����, OrdDt, OrdDt, char, 8;
		���������ȣ, RegBrnNo, RegBrnNo, char, 3;
		���¹�ȣ, AcntNo, AcntNo, char, 20;
		��й�ȣ, Pwd, Pwd, char, 8;
		�ؿܼ������ֹ���ȣ, OvrsFutsOrgOrdNo, OvrsFutsOrgOrdNo, char, 10;
		�����ڵ尪, IsuCodeVal, IsuCodeVal, char, 18;
		�����ֹ������ڵ�, FutsOrdTpCode, FutsOrdTpCode, char, 1;
		�Ÿű����ڵ�, BnsTpCode, BnsTpCode, char, 1;
		�����ֹ������ڵ�, FutsOrdPtnCode, FutsOrdPtnCode, char, 1;
		��ȭ�ڵ尪, CrcyCodeVal, CrcyCodeVal, char, 3;
		�ؿ��Ļ��ֹ�����, OvrsDrvtOrdPrc, OvrsDrvtOrdPrc, double, 30.11;
		�����ֹ�����, CndiOrdPrc, CndiOrdPrc, double, 30.11;
		�ֹ�����, OrdQty, OrdQty, long, 16;
		�ؿ��Ļ���ǰ�ڵ�, OvrsDrvtPrdtCode, OvrsDrvtPrdtCode, char, 10;
		������, DueYymm, DueYymm, char, 6;
		�ŷ����ڵ�, ExchCode, ExchCode, char, 10;
	end
	CIDBT00900OutBlock2,Out(*EMPTY*),output;
	begin
		���ڵ尹��, RecCnt, RecCnt, long, 5
		���¹�ȣ, AcntNo, AcntNo, char, 20;
		�ؿܼ����ֹ���ȣ, OvrsFutsOrdNo, OvrsFutsOrdNo, char, 10;
		���θ޽�������, InnerMsgCnts, InnerMsgCnts, char, 80;
	end
	END_DATA_MAP
END_FUNCTION_MAP
