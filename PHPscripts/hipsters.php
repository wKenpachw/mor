<?
function smuzi ($n, $m){
    $result = 0;
    if(($n > 0) && ($m > 0 ) ){
        $result = intdiv($m, $n);
    }
    return $result;
}

$hip = 4;
$smuz = 31;

echo smuzi($hip, $smuz);