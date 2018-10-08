var rpiDhtSensor = require('rpi-dht-sensor'); 
var dht = new rpiDhtSensor.DHT22(4);  
var temp_array = new Array();  //array for storing temperature values
var hum_array = new Array();   //array for storing humidity values
var count = 0;
var sumtemp=0,sumhum=0;      

function read () 
{
  var readout = dht.read();
  var temp =(readout.temperature * 1.8) + 32;   //conversion to fahrenheit
  temp = temp.toFixed(1);                       //converting temperature to single digit after point
  var hum = readout.humidity.toFixed(1);	//converting humidity to single digit after point
  console.log(count+1 +'-' + 'Temp ' + temp + ' degF, ' + hum + '% Hum');  //displaying values on console
	temp_array[count]=temp;
	hum_array[count]=hum;
	sumtemp = sumtemp + parseFloat(temp);
	sumhum = sumhum + parseFloat(hum);            //getting sum
	count++;
	if(count < 10)				      //Getting 10 values
	{
	setTimeout(read, 10000);                      //Read function after every 10secs
	
	}
	else
	{
	console.log('Lowest Temp ' + Math.min(...temp_array) + ' degF');     //Displaying lowest, highest and average values
	console.log('Lowest Hum ' + Math.min(...hum_array) + '%');
	console.log('Highest Temp ' + Math.max(...temp_array) + ' degF');
	console.log('Highest Hum ' + Math.max(...hum_array) + '%');
	console.log('Average Temp ' + (sumtemp/count).toFixed(1) + ' degF');
	console.log('Average Hum ' + (sumhum/count).toFixed(1) + '%');
	}
	
}

read();
