BEGIN_FUNCTION_MAP
.Feed, �ؿܼ��� ���簡ü��(OVC), OVC, attr, svr=OVS, key=8, group=1;
    BEGIN_DATA_MAP
    InBlock,�Է�,input;
    begin
        �����ڵ�,       symbol,    symbol,    char,   8;
    end
    OutBlock,���,output;
    begin
		�����ڵ�         , symbol     , symbol    , char   ,   8;
		ü������(����)   , ovsdate    , ovsdate   , char   ,   8;
		ü������(�ѱ�)   , kordate    , kordate   , char   ,   8;
		ü��ð�(����)   , trdtm      , trdtm     , char   ,   6;
		ü��ð�(�ѱ�)   , kortm      , kortm     , char   ,   6;
		ü�ᰡ��         , curpr      , curpr     , double ,   15.9;
		���ϴ��         , ydiffpr    , ydiffpr   , double ,   15.9;
		���ϴ���ȣ     , ydiffSign  , ydiffSign , char   ,   1;
		�ð�			 , open		  , open	  , double ,   15.9;
		��			 , high		  , high	  , double ,   15.9;
		����			 , low 		  , low 	  , double ,   15.9;
		�����			 , chgrate	  , chgrate   , float  , 6.2;
		�Ǻ�ü�����     , trdq       , trdq      , long   ,  10;
		����ü�����     , totq       , totq      , char   ,  15;
		ü�ᱸ��		 , cgubun     , cgubun    , char   ,   1;
		�ŵ�����ü����� , mdvolume   , mdvolume  , char   ,  15;
		�ż�����ü����� , msvolume   , msvolume  , char   ,  15;
		�帶���� 		 , ovsmkend   , ovsmkend  , char   ,   8;
    end
    END_DATA_MAP
END_FUNCTION_MAP
