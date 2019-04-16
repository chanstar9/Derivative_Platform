BEGIN_FUNCTION_MAP
	.Func,해외선물 체결내역개별 조회,CIDBQ01400,SERVICE=CIDBQ01400,headtype=B,CREATOR=이호섭,CREDATE=2018/08/23 09:07:51;
	BEGIN_DATA_MAP
	CIDBQ01400InBlock1,In(*EMPTY*),input;
	begin
		레코드갯수, RecCnt, RecCnt, long, 5
		조회구분코드, QryTpCode, QryTpCode, char, 1;
		계좌번호, AcntNo, AcntNo, char, 20;
		종목코드값, IsuCodeVal, IsuCodeVal, char, 18;
		매매구분코드, BnsTpCode, BnsTpCode, char, 1;
		해외파생주문가격, OvrsDrvtOrdPrc, OvrsDrvtOrdPrc, double, 30.11;
		해외선물주문유형코드, AbrdFutsOrdPtnCode, AbrdFutsOrdPtnCode, char, 1;
	end
	CIDBQ01400OutBlock1,In(*EMPTY*),output;
	begin
		레코드갯수, RecCnt, RecCnt, long, 5
		조회구분코드, QryTpCode, QryTpCode, char, 1;
		계좌번호, AcntNo, AcntNo, char, 20;
		종목코드값, IsuCodeVal, IsuCodeVal, char, 18;
		매매구분코드, BnsTpCode, BnsTpCode, char, 1;
		해외파생주문가격, OvrsDrvtOrdPrc, OvrsDrvtOrdPrc, double, 30.11;
		해외선물주문유형코드, AbrdFutsOrdPtnCode, AbrdFutsOrdPtnCode, char, 1;
	end
	CIDBQ01400OutBlock2,Out(*EMPTY*),output;
	begin
		레코드갯수, RecCnt, RecCnt, long, 5
		주문가능수량, OrdAbleQty, OrdAbleQty, long, 16;
	end
	END_DATA_MAP
END_FUNCTION_MAP
