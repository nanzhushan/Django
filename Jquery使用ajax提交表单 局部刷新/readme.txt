简介：

注意：js可以实现ajax请求，只是用Jquery  用ajax请求 更加方便和简单

AJAX即“Asynchronous Javascript And XML”（异步JavaScript和XML），是指一种创建交互式网页应用的网页开发技术，通过在后台与服务器进行少量数据交换，

AJAX 可以使网页实现异步更新。这意味着可以在不重新加载整个网页的情况下，对网页的某部分进行更新。

Jquery是一个优秀的Javascript函数库。兼容各种浏览器使用户能更方便地处理HTML、events、实现动画效果，并且方便地为网站提供AJAX交互。

所以两者其实不能作对比，一个是技术，一个是JS库的名称。



ajax提交，采用jQuery 去实现（非常简单）不用原生的js，


提交后的内容不会像get方式一样在网址中出现.采用的是异步提交

（1）
通过 jQuery，您可以选取（查询，query） HTML 元素，并对它们执行"操作"（actions）。

基础语法： $(selector).action()

美元符号定义 jQuery

选择符（selector）"查询"和"查找" HTML 元素

jQuery 的 action() 执行对元素的操作

实例:
$(this).hide() - 隐藏当前元素
$("p").hide() - 隐藏所有 <p> 元素
$("p.test").hide() - 隐藏所有 class="test" 的 <p> 元素
$("#test").hide() - 隐藏所有 id="test" 的元素

(2)
学习网址： http://www.runoob.com/jquery/jquery-ajax-get-post.html

jQuery get() 和 post() 方法用于通过 HTTP GET 或 POST 请求从服务器请求数据。

两种在客户端和服务器端进行请求-响应的常用方法是：GET 和 POST。
GET - 从指定的资源请求数据
POST - 向指定的资源提交要处理的数据


（2.1）
jQuery $.get() 方法
$.get() 方法通过 HTTP GET 请求从服务器上请求数据。

语法：
$.get(URL,callback);
必需的 URL 参数规定您希望请求的 URL。
可选的 callback 参数是请求成功后所执行的函数名。

下面的例子使用 $.get() 方法从服务器上的一个文件中取回数据：
实例
$("button").click(function(){
  $.get("demo_test.php",function(data,status){
    alert("Data: " + data + "nStatus: " + status);
  });
});

（2.2）

jQuery $.post() 方法

$.post() 方法通过 HTTP POST 请求从服务器上请求数据。
语法:
$.post(URL,data,callback);
必需的 URL 参数规定您希望请求的 URL。
可选的 data 参数规定连同请求发送的数据。
可选的 callback 参数是请求成功后所执行的函数名。

下面的例子使用 $.post() 连同请求一起发送数据：
实例
$("button").click(function(){
  $.post("demo_test_post.html",
  {
    name:"Donald Duck",
    city:"Duckburg"
  },
  function(data,status){
    alert("Data: " + data + "nStatus: " + status);
  });
});