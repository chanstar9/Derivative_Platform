BEGIN_FUNCTION_MAP
	.Func,�ؿܼ�������ֹ�,CIDBT01000,SERVICE=CIDBT01000,ENCRYPT,SIGNATURE,headtype=B,CREATOR=�ֿ�ȣ,CREDATE=2012/04/26 14:52:30;
	BEGIN_DATA_MAP
	CIDBT01000InBlock1,In(*EMPTY*),input;
	begin
		���ڵ尹��, RecCnt, RecCnt, long, 5
		�ֹ�����, OrdDt, OrdDt, char, 8;
		������ȣ, BrnNo, BrnNo, char, 3;
		���¹�ȣ, AcntNo, AcntNo, char, 20;
		��й�ȣ, Pwd, Pwd, char, 8;
		�����ڵ尪, IsuCodeVal, IsuCodeVal, char, 18;
		�ؿܼ������ֹ���ȣ, OvrsFutsOrgOrdNo, OvrsFutsOrgOrdNo, char, 10;
		�����ֹ������ڵ�, FutsOrdTpCode, FutsOrdTpCode, char, 1;
		��ǰ�����ڵ�, PrdtTpCode, PrdtTpCode, char, 2;
		�ŷ����ڵ�, ExchCode, ExchCode, char, 10;
	end
	CIDBT01000OutBlock1,In(*EMPTY*),output;
	begin
		���ڵ尹��, RecCnt, RecCnt, long, 5
		�ֹ�����, OrdDt, OrdDt, char, 8;
		������ȣ, BrnNo, BrnNo, char, 3;
		���¹�ȣ, AcntNo, AcntNo, char, 20;
		��й�ȣ, Pwd, Pwd, char, 8;
		�����ڵ尪, IsuCodeVal, IsuCodeVal, char, 18;
		�ؿܼ������ֹ���ȣ, OvrsFutsOrgOrdNo, OvrsFutsOrgOrdNo, char, 10;
		�����ֹ������ڵ�, FutsOrdTpCode, FutsOrdTpCode, char, 1;
		��ǰ�����ڵ�, PrdtTpCode, PrdtTpCode, char, 2;
		�ŷ����ڵ�, ExchCode, ExchCode, char, 10;
	end
	CIDBT01000OutBlock2,Out(*EMPTY*),output;
	begin
		���ڵ尹��, RecCnt, RecCnt, long, 5
		���¹�ȣ, AcntNo, AcntNo, char, 20;
		�ؿܼ����ֹ���ȣ, OvrsFutsOrdNo, OvrsFutsOrdNo, char, 10;
		���θ޽�������, InnerMsgCnts, InnerMsgCnts, char, 80;
	end
	END_DATA_MAP
END_FUNCTION_MAP
