BEGIN_FUNCTION_MAP
.Feed, �ؿܿɼ� ȣ��(WOH), WOH, attr, svr=OVS, key=8, group=1;
    BEGIN_DATA_MAP
    InBlock,�Է�,input;
    begin
        �����ڵ�,       symbol,    symbol,    char,   16;
    end
    OutBlock,���,output;
    begin
		�����ڵ�         ,   symbol      ,   symbol      , char    ,   16 ;
		ȣ���ð�		 ,	 hotime		 ,	 hotime		 , char	   ,   6 ;

		�ŵ�ȣ�� 1       ,   offerho1    ,   offerho1    , double  ,   15.9;
		�ż�ȣ�� 1       ,   bidho1      ,   bidho1      , double  ,   15.9;
		�ŵ�ȣ�� �ܷ� 1  ,   offerrem1   ,   offerrem1   , long    ,   10;
		�ż�ȣ�� �ܷ� 1  ,   bidrem1     ,   bidrem1     , long    ,   10;
		�ŵ�ȣ�� �Ǽ� 1  ,   offerno1    ,   offerno1    , long    ,   10;
		�ż�ȣ�� �Ǽ� 1  ,   bidno1      ,   bidno1      , long    ,   10;
        
        �ŵ�ȣ�� 2       ,   offerho2    ,   offerho2    , double  ,   15.9;
        �ż�ȣ�� 2       ,   bidho2      ,   bidho2      , double  ,   15.9;
        �ŵ�ȣ�� �ܷ� 2  ,   offerrem2   ,   offerrem2   , long    ,   10;
        �ż�ȣ�� �ܷ� 2  ,   bidrem2     ,   bidrem2     , long    ,   10;
        �ŵ�ȣ�� �Ǽ� 2  ,   offerno2    ,   offerno2    , long    ,   10;
        �ż�ȣ�� �Ǽ� 2  ,   bidno2      ,   bidno2      , long    ,   10;

		�ŵ�ȣ�� 3       ,   offerho3    ,   offerho3    , double  ,   15.9;
		�ż�ȣ�� 3       ,   bidho3      ,   bidho3      , double  ,   15.9;
		�ŵ�ȣ�� �ܷ� 3  ,   offerrem3   ,   offerrem3   , long    ,   10;
		�ż�ȣ�� �ܷ� 3  ,   bidrem3     ,   bidrem3     , long    ,   10;
		�ŵ�ȣ�� �Ǽ� 3  ,   offerno3    ,   offerno3    , long    ,   10;
		�ż�ȣ�� �Ǽ� 3  ,   bidno3      ,   bidno3      , long    ,   10;

		�ŵ�ȣ�� 4       ,   offerho4    ,   offerho4    , double  ,   15.9;
		�ż�ȣ�� 4       ,   bidho4      ,   bidho4      , double  ,   15.9;
		�ŵ�ȣ�� �ܷ� 4  ,   offerrem4   ,   offerrem4   , long    ,   10;
		�ż�ȣ�� �ܷ� 4  ,   bidrem4     ,   bidrem4     , long    ,   10;
		�ŵ�ȣ�� �Ǽ� 4  ,   offerno4    ,   offerno4    , long    ,   10;
		�ż�ȣ�� �Ǽ� 4  ,   bidno4      ,   bidno4      , long    ,   10;

		�ŵ�ȣ�� 5       ,   offerho5    ,   offerho5    , double  ,   15.9;
		�ż�ȣ�� 5       ,   bidho5      ,   bidho5      , double  ,   15.9;
		�ŵ�ȣ�� �ܷ� 5  ,   offerrem5   ,   offerrem5   , long    ,   10;
		�ż�ȣ�� �ܷ� 5  ,   bidrem5     ,   bidrem5     , long    ,   10;
		�ŵ�ȣ�� �Ǽ� 5  ,   offerno5    ,   offerno5    , long    ,   10;
		�ż�ȣ�� �Ǽ� 5  ,   bidno5      ,   bidno5      , long    ,   10;

        �ŵ�ȣ���ѰǼ�   ,   totoffercnt ,   totoffercnt , long    ,   10;
        �ż�ȣ���ѰǼ�   ,   totbidcnt   ,   totbidcnt   , long    ,   10;
        �ŵ�ȣ���Ѽ���   ,   totofferrem ,   totofferrem , long    ,   10;
        �ż�ȣ���Ѽ���   ,   totbidrem   ,   totbidrem   , long    ,   10;
    end
    END_DATA_MAP
END_FUNCTION_MAP
