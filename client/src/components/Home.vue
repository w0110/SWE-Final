<template>
  <body>
  <div id = "top">
    <div id = "red">
    </div>
  </div>
  <div id="header">
    <div id="header-inner">
    </div>
  </div>
  <div id="main-wrapper">
    <div id="blk-help">
      <h3>薦購服務說明</h3>
      <ul style="list-style-type:disc">
        <li>教師每學期以薦購60種(件)或新台幣60,000元為原則。</li>
        <li>講座教授、特聘教授可薦購數量/金額為本校教師的2倍。</li>
        <li>學生每月以薦購5種(件)或新台幣5,000元為原則。</li>
        <li>本系統將自動追蹤您的薦購資料處理狀態，定期email通知。</li>
        <li>薦購期刊、電子資源請填寫薦購表(請參見公布欄)。</li>
      </ul>
    </div>
    <div id="blk-board">
    <h3>公布欄</h3>
    <table id="Table" class="table-list" border="0">
      <tbody>
        <tr>
          <td class="date">2020/11/16 8:19:39</td>
        </tr>
        <tr>
          <td class="items" style="border-top: none;">
            <a onclick="javascript:window.open('http://recommend.lib.fcu.edu.tw/weblink/scripts/weblink/news.aspx?num=47&displaylang=');" href="javascript:void(0);">薦購系統E-mail自動通知功能暫停公告</a>
          </td>
        </tr>
        <tr>
          <td class="date">2020/3/17 16:28:33</td>
        </tr>
        <tr>
          <td class="items" style="border-top: none;">
            <a onclick="javascript:window.open('http://recommend.lib.fcu.edu.tw/weblink/scripts/weblink/news.aspx?num=45&displaylang=');" href="javascript:void(0);">簡體書延遲到貨公告</a>
          </td>
        </tr>
        <tr>
          <td class="date">2020/3/17 16:23:06</td>
        </tr>
        <tr>
          <td class="items" style="border-top: none;border-bottom: 1px solid #ddd;">
            <a onclick="javascript:window.open('http://recommend.lib.fcu.edu.tw/weblink/scripts/weblink/news.aspx?num=10&displaylang=');" href="javascript:void(0);">各類資源薦購額度與作業方式一覽表</a>
          </td>
        </tr>
      </tbody>
    </table>
    </div>
    <div id = "blue">
      <h1>推薦者登入 Login</h1>
      <input id="btn" type="button" value="NID登入" onclick="
              javascript:window.open('http://opendata.fcu.edu.tw/fcuOauth/Auth.aspx?client_id=637102957247.e9976f5b722a47a6af9beddfeadb70e4.recommend.lib.fcu.edu.tw&client_url=http://recommend.lib.fcu.edu.tw/weblink/scripts/weblink/oauth.aspx', '_top'
              , 'copyhistory=0' );">

      <h4>如何登錄系統</h4>
      <p>帳號：請輸入教職員/學生證號。 <br>
      密碼：請輸入NID密碼。(忘記密碼<br>
      請聯絡資訊處分機2712) <br>
      薦購服務相關問題請洽圖書館讀者 <br>
      服務組2682。
      </p>
    </div>
  </div>
<div id="bottom">
  <div id="foot">
  <div id="bottom-link">
    <a href="http://www.fcu.edu.tw/" target="_blank">逢甲大學</a> |
    <a href="https://www.fcu.edu.tw/organization/" target="_blank">本校行政單位</a> |
    <a href="https://academic.fcu.edu.tw/" target="_blank">本校教學單位</a>
  </div>
  <div id="copyright">
    <p>
    版權所有 © 逢甲大學全球資訊系統內之所有內容及版面設計 - 著作權屬於逢甲大學 |
    <a href="https://www.fcu.edu.tw/privacystatement/" target="_blank">隱私權聲明</a><br>
    地址 : 台中市 40724 西屯區文華路 100 號 | 聯絡電話 : 04-24517250 轉 2601 | 傳真 : 04-24516453
    </p>
  </div>
  </div>
</div>
</body>
</template>

<style type="text/css">
  *{
    padding: 0;
    margin: 0;
  }
  h1 {
      font-size: 22.5px;
      color: rgb(255, 255, 255);
      position: relative;
      top: 20px;
      left: 15px;
  }
  h3 {
    width: 150px;
    font-size: 22.5px;
    color: rgb(0, 0, 0);
    margin-left:30px;
    margin-top:30px;
    margin-bottom: 5px;
    padding:0px;
  }
  ul {
    margin-top: 15px;
    margin-bottom: 3em !important;
  }
  ul li{
    font-size: 15px;
    width: 400px;
    position: relative;
    left: 65px;
    margin-bottom: 20px;
    list-style-image: url("../assets/ico-li-square.png");
  }
  #btn {
      width: 87px;
      height: 34px;
      font-size: 20px;
      position: relative;
      top: 50px;
      left: 100px;
  }
  h4 {
      font-size: 18px;
      color: white;
      position: relative;
      top: 70px;
      left: 15px;
  }
  #blue p {
      font-size: 15px;
      color: white;
      position: relative;
      top: 85px;
      left: 40px;
  }
  body {
    background-color: #e9e9e9;
  }
  #top {
    width: 100%;
    height: 65px;
    background-color: #ffffff;
    border-bottom-style: solid;
    border-bottom-width: 0.2px;
    border-bottom-color: #A00000;
  }
  #header-inner{
    width: 100%;
    height: 70px;
    background-color: #e9e9e9;
    position: relative;
    z-index: 1;
    background: url("../assets/bg_header.png") center 24px no-repeat;
  }
  #red {
    width: 56px;
    height: 64px;
    background: #a00000 url("../assets/fcu_logo.png") center center no-repeat;
    position:relative;
    top: 0px;
    left: 300px;
  }
  #blue {
    width: 284px;
    height: 352px;
    background-color: #00b9cf;
    border-radius: 15px;
    position: absolute;
    top: 35px;
    left: 630px;
  }
  #img1{
      width: auto;
      height: auto;
      position: relative;
      top: 8px;
      left: 12px;
  }
  #img2{
      width: auto;
      height: auto;
      position: relative;
      top: 18px;
      left: 300px;
  }
  #main-wrapper {
    width: 950px;
    height: 570px;
    background-color: #ffffff;
    margin:0 auto;
    border-radius: 15px;
    border-style: solid;
    border-width: 0.2px;
    border-color: #D0D0D0;
    position: relative;
    z-index: 1;
  }
  #header {
    display:flex;
    flex-direction: column;
    align-items: center;
  }
  #blk-board {
    font-family:Microsoft JhengHei;
    margin-bottom: 5px;
  }
  #Table {
    padding-left: 30px;
    width: 584px;
  }
  td.date {
    font-size: 75% !important;
    color: #aaaaaa !important;
    padding: 12px 8px 0px 8px !important;
    border-top: 1px solid #dddddd;
  }
  td {
    line-height: 120%;
  }
  .items {
    font-size: 15px;
    padding: 5px 8px 12px 8px !important;
  }
  a:link {
    color: #00008b;
    text-decoration: underline;
  }
  a:hover {
    color: blue;
    text-decoration: none;
  }
  a:visited {
    color: #00008b;
    text-decoration: underline;
  }
  #copyright p {
    color: #999999;
  }
  #bottom{
    font-family:Microsoft JhengHei;
    background-color: #e9e9e9;
    display:flex;
    flex-direction: column;
    align-items: center;
  }
  #foot{
    background: url("../assets/fcu_logos.png") left top no-repeat;
    padding: 5px 0 15px 230px;
    margin-top: 15px;
    font-size: 15px;
    line-height: 150%;
  }
</style>
