function instagram() {
  //Postするデータ 
  var payload = {
  "username": "**********",
  "password": "*********"
  
};
  //Postオプション
  var post_options = {  
  muteHttpExceptions:true,//これがないとポスト時にエラー（400）をはく
  method : "post",
  payload : payload,
  followRedirects : false,
    //contentType: "application/x-www-form-urlencoded"
};
  //POSTリクエスト
  //PostするURL(上記でダメなら，http headerなどで実際にPOSTしているURLを調べる)
  var url = "https://www.instagram.com/accounts/logout/";
  var response = UrlFetchApp.fetch(url, post_options);
  //レスポンスヘッダーからcookieを取得
  var cookies = response.getAllHeaders()["Set-Cookie"];  
  Logger.log(cookies);
  //ログインで認証されたcookieはヘッダーで使用（これで，ログインを維持できる）
  var headers = { 'Cookie' : cookies };
  var get_options = {
    muteHttpExceptions:true,
    method : "get",
    headers : headers,
    followRedirects: true, //リダイレクトあり
  };
  
  //例として，ホームのページ情報を全て取得する
  var topUrl = "https://www.instagram.com/"
  var response = UrlFetchApp.fetch(topUrl, get_options);
  var content = response.getContentText("UTF-8");
  var docid='*********************************';
  var document=DocumentApp.openById(docid); //ドキュメントをIDで取得
  document.getBody().setText(content);
  Logger.log(content);
}