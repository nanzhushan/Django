//为了不让html有js代码，通过引入方式调用js,注意引入的js一定要写在前面,因为页面读取是从上往下读

function queren()
{
var se=confirm("你确定要删除这条记录吗？");
if (se==true)
  {
  window.location.href='/delete_host/{{ list1.id }}/';
  }
else
  {
  alert("将返回主界面");

  }
}