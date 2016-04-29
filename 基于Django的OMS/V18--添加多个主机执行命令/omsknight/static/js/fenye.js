function getQueryString(name) {
    var reg = new RegExp("(^|&)" + name + "=([^&]*)(&|$)", "i");
    var r = window.location.search.substr(1).match(reg);
    if (r != null) return unescape(r[2]); return null;
}
var curPage = getQueryString( "page" );

if( !curPage ){
    curPage  =  0;    //默认当前页是第0页
}
console.log( "---",curPage);

//自动下一页加1

function onClik(){
      curPage++;
      $(".next-page").attr( "href" , "?page="+curPage );

}

// 自动上一页减1

function onClik1(){

      curPage--;
      if(curPage <= 0) curPage = 0;
      $(".pre-page").attr( "href" , "?page="+curPage );

}