BEGIN_FUNCTION_MAP
.Feed, �ؿܼ����ֹ�, TC1, block, key=7, group=1;
    BEGIN_DATA_MAP
    InBlock,�Է�,input;
    begin
    end
    OutBlock,���,output;
    begin
		�����Ϸù�ȣ,  	lineseq,    lineseq,	long,   10;
		KEY,		    key,		key,		char,	11;
		������ID,		user,	    user,	   	char,	 8;

		����ID,           svc_id,             svc_id,	            char,    4;
		�ֹ�����,           ordr_dt,            ordr_dt,	        char,    8;
		������ȣ,           brn_cd,             brn_cd,             char,    3;
		�ֹ���ȣ,           ordr_no,            ordr_no,            long,    10;
		���ֹ���ȣ,         orgn_ordr_no,       orgn_ordr_no,       long,    10;
		���ֹ���ȣ,         mthr_ordr_no,       mthr_ordr_no,       long,    10;
		���¹�ȣ,           ac_no,              ac_no,              char,    11;
		�����ڵ�,           is_cd,              is_cd,              char,    30;
		�ŵ��ż�����,       s_b_ccd,            s_b_ccd,            char,    1;
		�����������,       ordr_ccd,           ordr_ccd,           char,    1;
		�ֹ������ڵ�,       ordr_typ_cd,        ordr_typ_cd,        char,    1;
		�ֹ��Ⱓ�ڵ�,       ordr_typ_prd_ccd,   ordr_typ_prd_ccd,   char,    2;
		�ֹ������������,   ordr_aplc_strt_dt,  ordr_aplc_strt_dt,  char,    8;
		�ֹ�������������,   ordr_aplc_end_dt,   ordr_aplc_end_dt,   char,    8;
		�ֹ�����,           ordr_prc,           ordr_prc,           double,  18.11;
		�ֹ����ǰ���,       cndt_ordr_prc,      cndt_ordr_prc,      double,  18.11;
		�ֹ�����,           ordr_q,             ordr_q,             long,    12;
		�ֹ��ð�,           ordr_tm,            ordr_tm,            char,    9;
		�����ID,           userid,             userid,             char,    8;
		�����������,       xrc_rsv_tcp_code,   xrc_rsv_tcp_code,   char,    1;
    end
    END_DATA_MAP
END_FUNCTION_MAP
