<?
date_default_timezone_set('UTC');
if (isset($_POST["year"] )) { 

    // Формируем массив для JSON ответа
    if (!is_numeric($_POST["year"])) $res = "ошибка!";
    else {
        $date = date("L", mktime(0, 0, 0, 1, 1, $_POST["year"]));
    
        if ($date == 1) $res = "високосный";
        elseif($date == 0) $res = "не високосный";
    }

    $result = array(
    	'year' => $res
    ); 
    //$date = date("L", mktime(0, 0, 0, 0, 0, $_POST["year"]));
    // Переводим массив в JSON
    echo json_encode($result); 
}

?>