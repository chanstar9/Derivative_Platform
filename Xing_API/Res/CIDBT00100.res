BEGIN_FUNCTION_MAP
	.Func,�ؿܼ����ű��ֹ�,CIDBT00100,SERVICE=CIDBT00100,ENCRYPT,SIGNATURE,headtype=B,CREATOR=��ȣ��,CREDATE=2018/08/28 16:28:20;
	BEGIN_DATA_MAP
	CIDBT00100InBlock1,In(*EMPTY*),input;
	begin
		���ڵ尹��, RecCnt, RecCnt, long, 5
		�ֹ�����, OrdDt, OrdDt, char, 8;
		�����ڵ�, BrnCode, BrnCode, char, 7;
		���¹�ȣ, AcntNo, AcntNo, char, 20;
		��й�ȣ, Pwd, Pwd, char, 8;
		�����ڵ尪, IsuCodeVal, IsuCodeVal, char, 18;
		�����ֹ������ڵ�, FutsOrdTpCode, FutsOrdTpCode, char, 1;
		�Ÿű����ڵ�, BnsTpCode, BnsTpCode, char, 1;
		�ؿܼ����ֹ������ڵ�, AbrdFutsOrdPtnCode, AbrdFutsOrdPtnCode, char, 1;
		��ȭ�ڵ�, CrcyCode, CrcyCode, char, 3;
		�ؿ��Ļ��ֹ�����, OvrsDrvtOrdPrc, OvrsDrvtOrdPrc, double, 30.11;
		�����ֹ�����, CndiOrdPrc, CndiOrdPrc, double, 30.11;
		�ֹ�����, OrdQty, OrdQty, long, 16;
		��ǰ�ڵ�, PrdtCode, PrdtCode, char, 6;
		������, DueYymm, DueYymm, char, 6;
		�ŷ����ڵ�, ExchCode, ExchCode, char, 10;
	end
	CIDBT00100OutBlock1,In(*EMPTY*),output;
	begin
		���ڵ尹��, RecCnt, RecCnt, long, 5
		�ֹ�����, OrdDt, OrdDt, char, 8;
		�����ڵ�, BrnCode, BrnCode, char, 7;
		���¹�ȣ, AcntNo, AcntNo, char, 20;
		��й�ȣ, Pwd, Pwd, char, 8;
		�����ڵ尪, IsuCodeVal, IsuCodeVal, char, 18;
		�����ֹ������ڵ�, FutsOrdTpCode, FutsOrdTpCode, char, 1;
		�Ÿű����ڵ�, BnsTpCode, BnsTpCode, char, 1;
		�ؿܼ����ֹ������ڵ�, AbrdFutsOrdPtnCode, AbrdFutsOrdPtnCode, char, 1;
		��ȭ�ڵ�, CrcyCode, CrcyCode, char, 3;
		�ؿ��Ļ��ֹ�����, OvrsDrvtOrdPrc, OvrsDrvtOrdPrc, double, 30.11;
		�����ֹ�����, CndiOrdPrc, CndiOrdPrc, double, 30.11;
		�ֹ�����, OrdQty, OrdQty, long, 16;
		��ǰ�ڵ�, PrdtCode, PrdtCode, char, 6;
		������, DueYymm, DueYymm, char, 6;
		�ŷ����ڵ�, ExchCode, ExchCode, char, 10;
	end
	CIDBT00100OutBlock2,Out(*EMPTY*),output;
	begin
		���ڵ尹��, RecCnt, RecCnt, long, 5
		���¹�ȣ, AcntNo, AcntNo, char, 20;
		�ؿܼ����ֹ���ȣ, OvrsFutsOrdNo, OvrsFutsOrdNo, char, 10;
	end
	END_DATA_MAP
END_FUNCTION_MAP
