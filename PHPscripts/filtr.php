<?
function filtrArray ($arrayStrings, $prefix){
    $newArray = array();
    if (is_array($arrayStrings) && is_string($prefix)) {
        foreach ($arrayStrings as $strOfArray){
            if ( stripos($strOfArray, $prefix) === 0)  {
                array_push($newArray,$strOfArray);
                echo stripos($strOfArray, $prefix) ;
            }
        }
    }
    return $newArray;
}

$testArray = array("foo", "far", "follo", "forld");
$testPreFix = "fol";

var_dump(filtrArray($testArray, $testPreFix));

?>