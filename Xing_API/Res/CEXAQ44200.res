BEGIN_FUNCTION_MAP
	.Func,EUREX �߰��ɼ� �Ⱓ�ֹ�ü����ȸ,CEXAQ44200,SERVICE=CEXAQ44200,headtype=B,CREATOR=,CREDATE=2012/11/08 17:10:28;
	BEGIN_DATA_MAP
	CEXAQ44200InBlock1,In(*EMPTY*),input;
	begin
		���ڵ尹��, RecCnt, RecCnt, long, 5
		�����Է±���, ChoicInptTpCode, ChoicInptTpCode, char, 1;
		���¹�ȣ, AcntNo, AcntNo, char, 20;
		��й�ȣ, Pwd, Pwd, char, 8;
		��ȸ������, QrySrtDt, QrySrtDt, char, 8;
		��ȸ������, QryEndDt, QryEndDt, char, 8;
		ü�ᱸ��, PrdtExecTpCode, PrdtExecTpCode, char, 1;
		�����ɼǰŷ������ڵ�, FnoTrdPtnCode, FnoTrdPtnCode, char, 2;
		�����ֹ���ȣ2, SrtOrdNo2, SrtOrdNo2, long, 10;
		���ļ�������, StnlnSeqTp, StnlnSeqTp, char, 1;
	end
	CEXAQ44200OutBlock1,In(*EMPTY*),output;
	begin
		���ڵ尹��, RecCnt, RecCnt, long, 5
		�����Է±���, ChoicInptTpCode, ChoicInptTpCode, char, 1;
		���¹�ȣ, AcntNo, AcntNo, char, 20;
		��й�ȣ, Pwd, Pwd, char, 8;
		��ȸ������, QrySrtDt, QrySrtDt, char, 8;
		��ȸ������, QryEndDt, QryEndDt, char, 8;
		ü�ᱸ��, PrdtExecTpCode, PrdtExecTpCode, char, 1;
		�����ɼǰŷ������ڵ�, FnoTrdPtnCode, FnoTrdPtnCode, char, 2;
		�����ֹ���ȣ2, SrtOrdNo2, SrtOrdNo2, long, 10;
		���ļ�������, StnlnSeqTp, StnlnSeqTp, char, 1;
	end
	CEXAQ44200OutBlock2,Out(*EMPTY*),output;
	begin
		���ڵ尹��, RecCnt, RecCnt, long, 5
		�ֹ�����, OrdQty, OrdQty, long, 16;
		ü�����, ExecQty, ExecQty, long, 16;
		��ü�����, UnercQty, UnercQty, long, 16;
		ü�ᰡ, ExecPrc, ExecPrc, double, 15.2;
	end
	CEXAQ44200OutBlock3,Out1(*EMPTY*),output,occurs;
	begin
		���¹�ȣ1, AcntNo1, AcntNo1, char, 20;
		���¸�, AcntNm, AcntNm, char, 40;
		�ֹ���, OrdDt, OrdDt, char, 8;
		�ֹ���ȣ, OrdNo, OrdNo, long, 10;
		���ֹ���ȣ, OrgOrdNo, OrgOrdNo, long, 10;
		�ֹ��ð�, OrdTime, OrdTime, char, 9;
		�����ȣ, IsuNo, IsuNo, char, 12;
		�����, IsuNm, IsuNm, char, 40;
		�Ÿű���, BnsTpNm, BnsTpNm, char, 10;
		�Ÿű���, BnsTpCode, BnsTpCode, char, 1;
		������ȣ�������ڵ�, ErxOrdprcTpCode, ErxOrdprcTpCode, char, 1;
		������ұ��и�, MrcTpNm, MrcTpNm, char, 10;
		�������������Ǳ����ڵ�, ErxPrcCndiTpCode, ErxPrcCndiTpCode, char, 1;
		�ڵ��, CodeNm, CodeNm, char, 40;
		�ֹ���, OrdPrc, OrdPrc, double, 13.2;
		�ֹ�����, OrdQty, OrdQty, long, 16;
		�����ɼǰźλ����ڵ�, FnoRjtRsnCode, FnoRjtRsnCode, char, 3;
		�ֹ����и�, OrdTpNm, OrdTpNm, char, 10;
		ü�ᱸ�и�, ExecTpNm, ExecTpNm, char, 10;
		ü�ᰡ, ExecPrc, ExecPrc, double, 13.2;
		ü�����, ExecQty, ExecQty, long, 16;
		ü��ð�, ExecTime, ExecTime, char, 9;
		ü���ȣ, ExecNo, ExecNo, long, 10;
		��ü�����, UnercQty, UnercQty, long, 16;
		�����ID, UserId, UserId, char, 16;
		��Ÿ�ü�ڵ�, CommdaCode, CommdaCode, char, 2;
		��Ÿ�ü�ڵ��, CommdaCodeNm, CommdaCodeNm, char, 40;
		IP�ּ�, IpAddr, IpAddr, char, 16;
		�ŷ���������, TrdPtnTpNm, TrdPtnTpNm, char, 20;
		�������ֹ������ڵ�, ErxOrdStatCode, ErxOrdStatCode, char, 1;
		�ڵ��0, CodeNm0, CodeNm0, char, 40;
		�ŷ��������ð�, ExchRcptTime, ExchRcptTime, char, 30;
	end
	END_DATA_MAP
END_FUNCTION_MAP
