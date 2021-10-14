function fieldChanged(){
    var userId = getField("user_id");
    var password = getField("password");
    var disabled = true;
    if (userId.value.length > 0 && password.value.length > 0) {
        disabled = false;
    }
    var login = getField("login");
    if (disabled) {
        login.setAttribute("disabled", "disabled");
    }
    else {
        login.removeAttribute("disabled");
    }
}
function getField(fieldName){
    var field = document.getElementById(fieldName);
    if (field == undefined) {
        throw new Error("要素が見つかりません: " + fieldName);
    }
    return field;
}
function passwdCheck(){
    var userId = getField("user_id");
    var pw = getField("password");
    var disabled = true;
    var caId = "AllJapan";
    var caPw = "home";

    //alert( "PasswdCheckが呼ばれました");

    if( userId.value != caId ){
        alert("ユーザIDが登録されていません");
        disabled = false;
     }else{
        if( pw.value != caPw ){
                alert("パスワードが違います");
                disabled = false;
        }else{
                //alert("認証をクリアしました");
                location.href=pw.value+".html";
        }
    }
    var login = getField("login");
    if (disabled) {
        login.setAttribute("disabled", "disabled");
    }
    else {
        login.removeAttribute("disabled");
    }
    return false;
}   