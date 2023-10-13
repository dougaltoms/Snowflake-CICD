create or replace table test (col1 int, col2 varchar);

select col1 from test;

create or replace procedure central_default_000_cod.prc_test();

create or replace task central_default_000_cod.tsk_test();

create or replace function addone(i int)
returns int
language python
runtime_version = '3.8'
handler = 'addone_py'
as
$$
def addone_py(i):
  return i+1
$$;
