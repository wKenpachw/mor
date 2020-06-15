<?php
// этот класс реализует проверку баланса авиалинии Phillippine Airlines
// не пытайтесь запустить его, без наших библиотек и фреймворка он не будет работать

class TAccountCheckerMabuhay extends TAccountChecker{

// этот метод должен распарсить форму логина на сайте, заполнить ее в ассоц. массив $this->http->Form
// при успешном разборе возвращает true, при ошибке (форма не найдена, сетевая ошибка, etc) - false
function LoadLoginForm(){
// $this->http - это объект-браузер. Пользуйтесь им для всех операций по загрузке
// очистить cookies
$this->http->removeCookies();
// загрузить страницу логина
// результат будет доступен как $this->http->Response['body']
$this->http->GetURL("https://www.columbia.com/account");
// ParseForm ищет в теле страницы форму по name или id (<form name="myaccountform"> в этом случае)
// и копирует значения всех полей ввода формы в массив $this->http->Form (->Form[name][value])
// возвращает boolean - найдена форма, или нет
// так же будет автоматически установлено свойство $this->http->FormURL из <form action="..">
if(!$this->http->ParseForm("dwfrm_login"))
return false;
// так вы можете изменять значения полей распарсенной формы, имитировать кнопки
$this->http->Form['dwfrm_login_username_d0zvkihmsewh'] = $this->AccountFields['veresch80@yahoo.com'];
$this->http->Form['dwfrm_login_password'] = $this->AccountFields['testcase'];
$this->http->Form['dwfrm_login_rememberme'] = 'True';
$this->http->Form['loginbutton.x'] = '15';
$this->http->Form['loginbutton.y'] = '35';
// для исследования отправляемой формы вы можете использовать: Developer Tools/Tamper Data/Web Developer/Chropath etc.
// форма успешно распарсена
return true;
}

// этот метод отправляет подготовленную форму логина на сайт
// возвращает boolean - удалось ли зайти на сайт
// при ошибке должно быть выброшено исключение с текстом и кодом ошибки
function Login(){
// отправить форму методом POST
// результат (тело страницы) будет доступен как $this->http->Response['body']
if(!$this->http->PostForm())
return false;
// метод $this->http->FindSingleNode извлекает из тела страницы значение по запросу XPath
// выражение XPath должно возвращать единственный (не много, и не 0) узел, только в этом случае оно вернет значение узла, во всех других случаях будет возвращен null
if ($message = $this->http->FindSingleNode("//*[@id=\"dwfrm_login\"]/div[1]"))
   throw new CheckException($message, ACCOUNT_INVALID_PASSWORD);
// true - успешно вошли (стоит отметить, что здесь нужно добавить условие, что авторизация была успешно пройдена, например, проверить наличие logout ссылки)
return true;
}

// этот метод должен разобрать внутреннюю страницу сайта и извлечь баланс и свойства
function Parse(){
// метод $this->SetBalance устанавливает баланс
// Balance - Current Balance
$this->SetBalance($this->http->FindSingleNode("//*[@id=\"rewards-banner-wrapper\"]/div/div[1]/div[1]/div[1]/span"));
// $this->SetProperty устанавливает значение свойства.
// первый параметр - код  свойства (без пробелов), второй - значение
// метод FindPreg ищет регулярное выражение (preg_match) внутри тела страницы,
// и возвращает первый sub-match (выражение внутри скобок) если найдено или null если не найдено
// Name
$this->SetProperty("Name", $this->http->FindPreg("//[@id=\"headerBanner\"]/div/div/ul/li[1]/ul/li[1]/a"));
// Your Membership Number
$this->SetProperty("Number", $this->http->FindSingleNode("//td[b[contains(text(), 'Your Membership Number')]]/following::td[1]"));
// Your Membership Status
$this->SetProperty("Status", $this->http->FindSingleNode("//td[b[contains(text(), 'Your Membership Status')]]/following::td[1]"));
// Flight Miles earned this year
$this->SetProperty("EarnedThisYear", $this->http->FindSingleNode("//td[a[b[contains(text(), 'Flight Miles earned this year')]]]/following::td[1]"));
// Flight Miles earned this year
$this->SetProperty("MilesNeeded", $this->http->FindSingleNode("//[@id=\"rewards-banner-wrapper\"]/div/div[1]/div[1]/div[2]/span"));
}

}
?>