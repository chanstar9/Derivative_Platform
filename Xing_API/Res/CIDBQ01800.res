BEGIN_FUNCTION_MAP
	.Func,�ؿܼ��� �ֹ�ü�᳻�� ��ȸ,CIDBQ01800,SERVICE=CIDBQ01800,headtype=B,CREATOR=��ȣ��,CREDATE=2018/08/28 09:16:47;
	BEGIN_DATA_MAP
	CIDBQ01800InBlock1,In(*EMPTY*),input;
	begin
		���ڵ尹��, RecCnt, RecCnt, long, 5
		���¹�ȣ, AcntNo, AcntNo, char, 20;
		��й�ȣ, Pwd, Pwd, char, 8;
		�����ڵ尪, IsuCodeVal, IsuCodeVal, char, 18;
		�ֹ�����, OrdDt, OrdDt, char, 8;
		���ϱ����ڵ�, ThdayTpCode, ThdayTpCode, char, 1;
		�ֹ������ڵ�, OrdStatCode, OrdStatCode, char, 1;
		�Ÿű����ڵ�, BnsTpCode, BnsTpCode, char, 1;
		��ȸ�����ڵ�, QryTpCode, QryTpCode, char, 1;
		�ֹ������ڵ�, OrdPtnCode, OrdPtnCode, char, 2;
		�ؿ��Ļ������ɼǱ����ڵ�, OvrsDrvtFnoTpCode, OvrsDrvtFnoTpCode, char, 1;
	end
	CIDBQ01800OutBlock1,In(*EMPTY*),output;
	begin
		���ڵ尹��, RecCnt, RecCnt, long, 5
		���¹�ȣ, AcntNo, AcntNo, char, 20;
		��й�ȣ, Pwd, Pwd, char, 8;
		�����ڵ尪, IsuCodeVal, IsuCodeVal, char, 18;
		�ֹ�����, OrdDt, OrdDt, char, 8;
		���ϱ����ڵ�, ThdayTpCode, ThdayTpCode, char, 1;
		�ֹ������ڵ�, OrdStatCode, OrdStatCode, char, 1;
		�Ÿű����ڵ�, BnsTpCode, BnsTpCode, char, 1;
		��ȸ�����ڵ�, QryTpCode, QryTpCode, char, 1;
		�ֹ������ڵ�, OrdPtnCode, OrdPtnCode, char, 2;
		�ؿ��Ļ������ɼǱ����ڵ�, OvrsDrvtFnoTpCode, OvrsDrvtFnoTpCode, char, 1;
	end
	CIDBQ01800OutBlock2,Out(*EMPTY*),output,occurs;
	begin
		�ؿܼ����ֹ���ȣ, OvrsFutsOrdNo, OvrsFutsOrdNo, char, 10;
		�ؿܼ������ֹ���ȣ, OvrsFutsOrgOrdNo, OvrsFutsOrgOrdNo, char, 10;
		FCM�ֹ���ȣ, FcmOrdNo, FcmOrdNo, char, 15;
		�����ڵ尪, IsuCodeVal, IsuCodeVal, char, 18;
		�����, IsuNm, IsuNm, char, 50;
		�ؿܼ�����簡��, AbrdFutsXrcPrc, AbrdFutsXrcPrc, double, 30.11;
		FCM���¹�ȣ, FcmAcntNo, FcmAcntNo, char, 20;
		�Ÿű����ڵ�, BnsTpCode, BnsTpCode, char, 1;
		�Ÿű��и�, BnsTpNm, BnsTpNm, char, 10;
		�����ֹ������ڵ�, FutsOrdStatCode, FutsOrdStatCode, char, 1;
		�����ڵ��, TpCodeNm, TpCodeNm, char, 50;
		�����ֹ������ڵ�, FutsOrdTpCode, FutsOrdTpCode, char, 1;
		�ŷ����и�, TrdTpNm, TrdTpNm, char, 20;
		�ؿܼ����ֹ������ڵ�, AbrdFutsOrdPtnCode, AbrdFutsOrdPtnCode, char, 1;
		�ֹ�������, OrdPtnNm, OrdPtnNm, char, 40;
		�ֹ������Ⱓ�����ڵ�, OrdPtnTermTpCode, OrdPtnTermTpCode, char, 2;
		�����ڵ��, CmnCodeNm, CmnCodeNm, char, 100;
		�����������, AppSrtDt, AppSrtDt, char, 8;
		������������, AppEndDt, AppEndDt, char, 8;
		�ؿ��Ļ��ֹ�����, OvrsDrvtOrdPrc, OvrsDrvtOrdPrc, double, 30.11;
		�ֹ�����, OrdQty, OrdQty, long, 16;
		�ؿܼ���ü�ᰡ��, AbrdFutsExecPrc, AbrdFutsExecPrc, double, 30.11;
		ü�����, ExecQty, ExecQty, long, 16;
		�ֹ����ǰ���, OrdCndiPrc, OrdCndiPrc, double, 30.11;
		�ؿ��Ļ����簡, OvrsDrvtNowPrc, OvrsDrvtNowPrc, double, 30.11;
		��������, MdfyQty, MdfyQty, long, 16;
		��Ҽ���, CancQty, CancQty, long, 16;
		�źμ���, RjtQty, RjtQty, long, 13;
		Ȯ�μ���, CnfQty, CnfQty, long, 16;
		�ݴ�Ÿſ���, CvrgYn, CvrgYn, char, 1;
		��ϴܸ���ȣ, RegTmnlNo, RegTmnlNo, char, 3;
		���������ȣ, RegBrnNo, RegBrnNo, char, 3;
		��ϻ����ID, RegUserId, RegUserId, char, 16;
		�ֹ�����, OrdDt, OrdDt, char, 8;
		�ֹ��ð�, OrdTime, OrdTime, char, 9;
		�ؿܿɼ���翹�౸���ڵ�, OvrsOptXrcRsvTpCode, OvrsOptXrcRsvTpCode, char, 1;
	end
	END_DATA_MAP
END_FUNCTION_MAP
