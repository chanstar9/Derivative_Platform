BEGIN_FUNCTION_MAP
    .Func,�����������Ǹ���Ʈ��ȸ(API)(t1866),t1866,ENCRYPT,block,headtype=A;
    BEGIN_DATA_MAP
    t1866InBlock,�⺻�Է�,input;
    begin
		�α���ID,          user_id,        user_id,        char,     8;
		��ȸ����,          gb,             gb,             char,     1;
        �׷��,            group_name,     group_name,     char,    40;
		���ӿ���,          cont,           cont,           char,     1;
        ����Ű,            contkey,        cont_key,       char,    40;
    end
    t1866OutBlock,���,output;
    begin
        �������Ǽ�,        result_count,   result_count,   long,     5;
		���ӿ���,          cont,           cont,           char,     1;
        ����Ű,            contkey,        cont_key,       char,    40;
    end
    t1866OutBlock1,���1,output,occurs;
    begin
        ���������ε���,    query_index,    query_index,    char,    12;
        �׷��,            group_name,     group_name,     char,    40;
        ���������,        query_name,     query_name,     char,    40;
    end
    END_DATA_MAP
END_FUNCTION_MAP
