BEGIN_FUNCTION_MAP
.Feed, �ؿܼ���ü��, TC3, block, key=7, group=1;
    BEGIN_DATA_MAP
    InBlock,�Է�,input;
    begin
    end
    OutBlock,���,output;
    begin
		�����Ϸù�ȣ,  	lineseq,    lineseq,	long,   10;
		KEY,		    key,		key,		char,	11;
		������ID,		user,	    user,	   	char,	 8;

        ����ID,           svc_id,             svc_id,             char,    4;
        �ֹ�����,           ordr_dt,            ordr_dt,            char,    8;
        ������ȣ,           brn_cd,             brn_cd,             char,    3;
        �ֹ���ȣ,           ordr_no,            ordr_no,            long,    10;
        ���ֹ���ȣ,         orgn_ordr_no,       orgn_ordr_no,       long,    10;
        ���ֹ���ȣ,         mthr_ordr_no,       mthr_ordr_no,       long,    10;
        ���¹�ȣ,           ac_no,              ac_no,              char,    11;
        �����ڵ�,           is_cd,              is_cd,              char,    30;
        �ŵ��ż�����,       s_b_ccd,            s_b_ccd,            char,    1;
        �����������,       ordr_ccd,           ordr_ccd,           char,    1;
        ü�����,           ccls_q,             ccls_q,             long,    15;
        ü�ᰡ��,           ccls_prc,           ccls_prc,           double,  18.11;
        ü���ȣ,           ccls_no,            ccls_no,            char,    10;
        ü��ð�,           ccls_tm,            ccls_tm,            char,    9;
        ������մܰ�,       avg_byng_uprc,      avg_byng_uprc,      double,  18.11;
        ���Աݾ�,           byug_amt,           byug_amt,           double,  25.8;
        û�����,           clr_pl_amt,         clr_pl_amt,         double,  19.2;
        ��Ź������,         ent_fee,            ent_fee,            double,  19.2;
        FCM������,          fcm_fee,            fcm_fee,            double,  19.2;
		�����ID,           userid,             userid,             char,    8;
        ���簡��,           now_prc,            now_prc,            double,  18.11;
        ��ȭ�ڵ�,           crncy_cd,           crncy_cd,           char,    3;
        ��������,           mtrt_dt,            mtrt_dt,            char,    8;
    end
    END_DATA_MAP
END_FUNCTION_MAP
