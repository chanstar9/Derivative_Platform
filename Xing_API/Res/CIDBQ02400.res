BEGIN_FUNCTION_MAP
	.Func,�ؿܼ��� �ֹ�ü�᳻�� �� ��ȸ,CIDBQ02400,SERVICE=CIDBQ02400,ENCRYPT,headtype=B,CREATOR=��ȣ��,CREDATE=2018/08/29 14:00:16;
	BEGIN_DATA_MAP
	CIDBQ02400InBlock1,In(*EMPTY*),input;
	begin
		���ڵ尹��, RecCnt, RecCnt, long, 5
		���¹�ȣ, AcntNo, AcntNo, char, 20;
		��й�ȣ, Pwd, Pwd, char, 8;
		�����ڵ尪, IsuCodeVal, IsuCodeVal, char, 18;
		��ȸ��������, QrySrtDt, QrySrtDt, char, 8;
		��ȸ��������, QryEndDt, QryEndDt, char, 8;
		���ϱ����ڵ�, ThdayTpCode, ThdayTpCode, char, 1;
		�ֹ������ڵ�, OrdStatCode, OrdStatCode, char, 1;
		�Ÿű����ڵ�, BnsTpCode, BnsTpCode, char, 1;
		��ȸ�����ڵ�, QryTpCode, QryTpCode, char, 1;
		�ֹ������ڵ�, OrdPtnCode, OrdPtnCode, char, 2;
		�ؿ��Ļ������ɼǱ����ڵ�, OvrsDrvtFnoTpCode, OvrsDrvtFnoTpCode, char, 1;
	end
	CIDBQ02400OutBlock1,In(*EMPTY*),output;
	begin
		���ڵ尹��, RecCnt, RecCnt, long, 5
		���¹�ȣ, AcntNo, AcntNo, char, 20;
		��й�ȣ, Pwd, Pwd, char, 8;
		�����ڵ尪, IsuCodeVal, IsuCodeVal, char, 18;
		��ȸ��������, QrySrtDt, QrySrtDt, char, 8;
		��ȸ��������, QryEndDt, QryEndDt, char, 8;
		���ϱ����ڵ�, ThdayTpCode, ThdayTpCode, char, 1;
		�ֹ������ڵ�, OrdStatCode, OrdStatCode, char, 1;
		�Ÿű����ڵ�, BnsTpCode, BnsTpCode, char, 1;
		��ȸ�����ڵ�, QryTpCode, QryTpCode, char, 1;
		�ֹ������ڵ�, OrdPtnCode, OrdPtnCode, char, 2;
		�ؿ��Ļ������ɼǱ����ڵ�, OvrsDrvtFnoTpCode, OvrsDrvtFnoTpCode, char, 1;
	end
	CIDBQ02400OutBlock2,Out(*EMPTY*),output,occurs;
	begin
		�ֹ�����, OrdDt, OrdDt, char, 8;
		�ؿܼ����ֹ���ȣ, OvrsFutsOrdNo, OvrsFutsOrdNo, char, 10;
		�ؿܼ������ֹ���ȣ, OvrsFutsOrgOrdNo, OvrsFutsOrgOrdNo, char, 10;
		FCM�ֹ���ȣ, FcmOrdNo, FcmOrdNo, char, 15;
		�ؿܼ���ü���ȣ, OvrsFutsExecNo, OvrsFutsExecNo, char, 10;
		FCM���¹�ȣ, FcmAcntNo, FcmAcntNo, char, 20;
		�����ڵ尪, IsuCodeVal, IsuCodeVal, char, 18;
		�����, IsuNm, IsuNm, char, 50;
		�ؿܼ�����簡��, AbrdFutsXrcPrc, AbrdFutsXrcPrc, double, 30.11;
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
		�ֹ�����, OrdQty, OrdQty, long, 16;
		�ؿ��Ļ��ֹ�����, OvrsDrvtOrdPrc, OvrsDrvtOrdPrc, double, 30.11;
		ü�����, ExecQty, ExecQty, long, 16;
		�ؿܼ���ü�ᰡ��, AbrdFutsExecPrc, AbrdFutsExecPrc, double, 30.11;
		�ֹ����ǰ���, OrdCndiPrc, OrdCndiPrc, double, 30.11;
		�ؿ��Ļ����簡, OvrsDrvtNowPrc, OvrsDrvtNowPrc, double, 30.11;
		ó�������ڵ�, TrxStatCode, TrxStatCode, char, 2;
		ó�������ڵ��, TrxStatCodeNm, TrxStatCodeNm, char, 40;
		��Ź������, CsgnCmsn, CsgnCmsn, double, 19.2;
		FCM������, FcmCmsn, FcmCmsn, double, 21.4;
		��������, ThcoCmsn, ThcoCmsn, double, 19.2;
		��ü�ڵ�, MdaCode, MdaCode, char, 2;
		��ü�ڵ��, MdaCodeNm, MdaCodeNm, char, 40;
		��ϴܸ���ȣ, RegTmnlNo, RegTmnlNo, char, 3;
		��ϻ����ID, RegUserId, RegUserId, char, 16;
		�ֹ��Ͻ�, OrdDttm, OrdDttm, char, 30;
		�ֹ��ð�, OrdTime, OrdTime, char, 9;
		ü������, ExecDt, ExecDt, char, 8;
		ü��ð�, ExecTime, ExecTime, char, 9;
		�ŷ��Һ��1������ݾ�, EufOneCmsnAmt, EufOneCmsnAmt, double, 19.2;
		�ŷ��Һ��2������ݾ�, EufTwoCmsnAmt, EufTwoCmsnAmt, double, 19.2;
		����û���1������ݾ�, LchOneCmsnAmt, LchOneCmsnAmt, double, 19.2;
		����û���2������ݾ�, LchTwoCmsnAmt, LchTwoCmsnAmt, double, 19.2;
		�ŷ�1������ݾ�, TrdOneCmsnAmt, TrdOneCmsnAmt, double, 19.2;
		�ŷ�2������ݾ�, TrdTwoCmsnAmt, TrdTwoCmsnAmt, double, 19.2;
		�ŷ�3������ݾ�, TrdThreeCmsnAmt, TrdThreeCmsnAmt, double, 19.2;
		�ܱ�1������ݾ�, StrmOneCmsnAmt, StrmOneCmsnAmt, double, 19.2;
		�ܱ�2������ݾ�, StrmTwoCmsnAmt, StrmTwoCmsnAmt, double, 19.2;
		�ܱ�3������ݾ�, StrmThreeCmsnAmt, StrmThreeCmsnAmt, double, 19.2;
		����1������ݾ�, TransOneCmsnAmt, TransOneCmsnAmt, double, 19.2;
		����2������ݾ�, TransTwoCmsnAmt, TransTwoCmsnAmt, double, 19.2;
		����3������ݾ�, TransThreeCmsnAmt, TransThreeCmsnAmt, double, 19.2;
		����4������ݾ�, TransFourCmsnAmt, TransFourCmsnAmt, double, 19.2;
		�ؿܿɼ���翹�౸���ڵ�, OvrsOptXrcRsvTpCode, OvrsOptXrcRsvTpCode, char, 1;
	end
	END_DATA_MAP
END_FUNCTION_MAP
