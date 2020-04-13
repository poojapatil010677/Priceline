<?php
extract($_GET);
//$term = "anan";
$row = 1;
$res = array();
if (($handle = fopen("data.csv", "r")) !== FALSE) {
while (($data = fgetcsv($handle)) !== FALSE)
{
  $row++;
  if(strncasecmp($data[3],$term,strlen($term))==0){
    if(in_array($data[3],$res)){
      $row++;
      continue;
    }
    else{
      $res[]=$data[3];
    }
  }
}
fclose($handle);
}
echo json_encode($res);
 ?>
