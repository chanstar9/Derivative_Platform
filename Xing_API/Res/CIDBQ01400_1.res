BEGIN_FUNCTION_MAP
	.Func,�ؿܼ��� ü�᳻������ ��ȸ,CIDBQ01400,SERVICE=CIDBQ01400,headtype=B,CREATOR=��ȣ��,CREDATE=2015/07/30 09:08:25;
	BEGIN_DATA_MAP
	CIDBQ01400InBlock1,In(*EMPTY*),input;
	begin
		���ڵ尹��, RecCnt, RecCnt, long, 5
		��ȸ�����ڵ�, QryTpCode, QryTpCode, char, 1;
		���¹�ȣ, AcntNo, AcntNo, char, 20;
		�����ڵ尪, IsuCodeVal, IsuCodeVal, char, 18;
		�Ÿű����ڵ�, BnsTpCode, BnsTpCode, char, 1;
		�ؿ��Ļ��ֹ�����, OvrsDrvtOrdPrc, OvrsDrvtOrdPrc, double, 25.8;
		�ؿܼ����ֹ������ڵ�, AbrdFutsOrdPtnCode, AbrdFutsOrdPtnCode, char, 1;
	end
	CIDBQ01400OutBlock1,In(*EMPTY*),output;
	begin
		���ڵ尹��, RecCnt, RecCnt, long, 5
		��ȸ�����ڵ�, QryTpCode, QryTpCode, char, 1;
		���¹�ȣ, AcntNo, AcntNo, char, 20;
		�����ڵ尪, IsuCodeVal, IsuCodeVal, char, 18;
		�Ÿű����ڵ�, BnsTpCode, BnsTpCode, char, 1;
		�ؿ��Ļ��ֹ�����, OvrsDrvtOrdPrc, OvrsDrvtOrdPrc, double, 25.8;
		�ؿܼ����ֹ������ڵ�, AbrdFutsOrdPtnCode, AbrdFutsOrdPtnCode, char, 1;
	end
	CIDBQ01400OutBlock2,Out(*EMPTY*),output;
	begin
		���ڵ尹��, RecCnt, RecCnt, long, 5
		�ֹ����ɼ���, OrdAbleQty, OrdAbleQty, long, 16;
	end
	END_DATA_MAP
END_FUNCTION_MAP
