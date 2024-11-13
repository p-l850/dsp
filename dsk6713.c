#inlcude<DSK6713.h>
#include<DSK6713_LED.h>
#include<DSK6713_DIP.h>
void main(){
    DSK6713.init();
    DSK6713_LED.init();
    DSK6713_DIP.init();
    while(1){
    DSK6713_LED_toggle(0);
    if(DSK6713_DIP_get(3)==0)
        DSK6713_LED_on(3);
    else
        DSK6713_LED_off(3);
    DSK76713_waitusec(200000);
    }
}